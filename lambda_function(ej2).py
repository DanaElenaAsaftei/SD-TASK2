import boto3
import time

INSULTS = ["fool", "idiot", "nerd", "dumb", "clown", "stupid"]

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    queue_url = event['queue_url']

    while True:
        # Rebem fins a 10 missatges per lot
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=1
        )

        messages = response.get("Messages", [])
        if not messages:
            print("No queden més missatges. Sortint...")
            break

        for msg in messages:
            text = msg["Body"]
            filtered = text
            for insult in INSULTS:
                filtered = filtered.replace(insult, "CENSORED").replace(insult.capitalize(), "CENSORED")

            time.sleep(2)  # Simula processament lent

            print(f"[FILTERED] Original: {text}")
            print(f"[FILTERED] Cleaned: {filtered}")

            # Eliminar de la cua
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=msg["ReceiptHandle"]
            )

    return {"status": "done"}

