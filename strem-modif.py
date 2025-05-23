import boto3
import json
import time
from math import ceil

def stream(function_name, maxfunc, queue_url):

    region = 'us-east-1'  # La meja regió AWS

    sqs = boto3.client('sqs', region_name=region)
    lambda_client = boto3.client('lambda', region_name=region)


    C = 0.5     # Capacitat per worker (1 msg / 2s)
    Tr = 10     # Temps objectiu de resposta (en segons)

    last_count = 0
    last_time = time.time()

    while True:
        now = time.time()

        # Backlog actual
        attrs = sqs.get_queue_attributes(
            QueueUrl=queue_url,
            AttributeNames=['ApproximateNumberOfMessages']
        )
        B = int(attrs['Attributes']['ApproximateNumberOfMessages'])

        # Taxa d’arribada
        delta_t = now - last_time
        λ = max((B - last_count) / delta_t, 0)

        # Fórmula d’escalat
        N = ceil((B + λ * Tr) / C)
        N = min(N, maxfunc)

        if N > 0 and B > 0:
            print(f"[Scaler] → Lançant {N} workers...")
            for _ in range(N):
                lambda_client.invoke(
                    FunctionName=function_name,
                    InvocationType='Event',
                    Payload=json.dumps({
                        "queue_url": queue_url
                    }).encode()
                )
        else:
            print(f"[Scaler] → No s'han llençat Lambdas.")

        print(f"[Scaler] Backlog B: {B}, λ: {λ:.2f} msg/s → N = {N} workers")

        last_count = B
        last_time = now

        time.sleep(5)
