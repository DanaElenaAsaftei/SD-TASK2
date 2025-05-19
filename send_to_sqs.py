import boto3

# URL de la cola
queue_url = 'https://sqs.us-east-1.amazonaws.com/375257933091/insults-queue'

# Crear cliente SQS
sqs = boto3.client('sqs', region_name='us-east-1')


# Lista de mensajes de prueba
texts = [
    "You are a fool",
    "Idiot! Fix it already!",
    "Hello world",
    "Such a nerdy mistake",
    "What a dumb error",
    "Don't be a clown"
]
