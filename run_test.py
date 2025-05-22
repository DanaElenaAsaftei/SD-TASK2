from stream import stream
stream(
    function_name="insultWorker",
    maxfunc=5,
    queue_url="https://sqs.us-east-1.amazonaws.com/058264277608/insult-queue"
)
#ej2
