#ej3
from lithops import FunctionExecutor, Storage

INSULTS = ["fool", "idiot", "nerd", "dumb", "clown", "stupid"]

# Funció MAP corregida per Lithops
def map_function(bucket, key):
    storage = Storage()
    data = storage.get_object(bucket, key).decode('utf-8')

    count = 0
    for insult in INSULTS:
        count += data.lower().count(insult)
        data = data.replace(insult, "CENSORED").replace(insult.capitalize(), "CENSORED")

    censored_key = f"censored/{key}"
    storage.put_object(bucket, censored_key, data.encode('utf-8'))

    return count


# REDUCE
def reduce_function(results):
    return sum(results)

# Bucket
bucket_name = 'insult-files'
storage = Storage()
inputs = [(bucket_name, obj['Key']) for obj in storage.list_objects(bucket_name) if not obj['Key'].startswith("censored/")]


# Executor
with FunctionExecutor(runtime_memory=1024) as fexec:
    fexec.map_reduce(map_function, inputs, reduce_function)
    result = fexec.get_result()

print(f"Total insults censored: {result}")
