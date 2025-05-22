import boto3
#ej2
queue_url = "https://sqs.us-east-1.amazonaws.com/058264277608/insult-queue"

messages = [
    "You are a dumb clown.",
    "What an idiot move.",
    "He's such a nerd.",
    "Only a fool would do that.",
    "That's just dumb.",
    "You are a clown and a fool."
]

sqs = boto3.client('sqs')

for msg in messages:
    sqs.send_message(QueueUrl=queue_url, MessageBody=msg)

print("Mensajes enviados correctamente.")
