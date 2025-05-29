from stream import stream

stream(
    function_name="InsultFilterLambda",  
    maxfunc=5,                          
    queue_url="https://sqs.us-east-1.amazonaws.com/375257933091/insults-queue"  
)

