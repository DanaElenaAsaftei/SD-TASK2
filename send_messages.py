import boto3

queue_url = "https://sqs.us-east-1.amazonaws.com/375257933091/insults-queue"

messages = [
    "You are a dumb clown.",
    "What an idiot move.",
    "He's such a nerd.",
    "Only a fool would do that.",
    "That's just dumb.",
    "You are a clown and a fool."
]

sqs = boto3.client('sqs', region_name='us-east-1')

for msg in messages:
    sqs.send_message(QueueUrl=queue_url, MessageBody=msg)

print("Mensajes enviados correctamente.")
