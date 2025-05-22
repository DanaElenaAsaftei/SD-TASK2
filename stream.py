#ej2
import boto3
import json
import time

def stream(function_name, maxfunc, queue_url):
    sqs = boto3.client('sqs')
    lambda_client = boto3.client('lambda')

    while True:
        # Obtener número de mensajes en la cola
        attrs = sqs.get_queue_attributes(
            QueueUrl=queue_url,
            AttributeNames=['ApproximateNumberOfMessages']
        )
        num_msgs = int(attrs['Attributes']['ApproximateNumberOfMessages'])
        print(f"Mensajes en cola: {num_msgs}")

        # Calcular cuántos workers lanzar
        to_launch = min(num_msgs, maxfunc)
        print(f"Lanzando {to_launch} workers...")

        for _ in range(to_launch):
            lambda_client.invoke(
                FunctionName=function_name,
                InvocationType='Event',  # async
                Payload=json.dumps({
                    "queue_url": queue_url
                }).encode()
            )

        time.sleep(5)  # Espera antes de revisar de nuevo
