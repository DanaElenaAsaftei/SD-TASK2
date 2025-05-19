import json
import time

INSULTS = ["fool", "idiot", "nerd", "dumb", "clown"]

def lambda_handler(event, context):
    for record in event['Records']:
        text = record['body']
        filtered = text
        for insult in INSULTS:
            filtered = filtered.replace(insult, "CENSORED").replace(insult.capitalize(), "CENSORED")

        # Simula procesamiento lento para observar escalado
        time.sleep(2)

        print(f"[FILTERED] Original: {text}")
        print(f"[FILTERED] Cleaned: {filtered}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Messages processed successfully')
    }

