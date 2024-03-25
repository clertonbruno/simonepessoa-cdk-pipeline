def lambda_handler(event, context):
    """
    Lambda function handler.

    Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The runtime information of the Lambda function.

    Returns:
        dict: The response object containing the statusCode, headers, and body.
    """
    # ⚠️ DO NOT UPDATE AND COMMIT THIS FILE AS IT WOULD OVERWRITE ALL LAMBDA CODES ⚠️
    # ⚠️ DO NOT UPDATE AND COMMIT THIS FILE AS IT WOULD OVERWRITE ALL LAMBDA CODES ⚠️
    # ⚠️ DO NOT UPDATE AND COMMIT THIS FILE AS IT WOULD OVERWRITE ALL LAMBDA CODES ⚠️

    print(event)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": f"Hello from Lambda!. Event input for this lambda: {str(event)}",
    }
