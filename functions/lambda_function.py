import os

# Initialize resources
FOO = os.getenv("FOO")

def dynamodb_handler(event, context):
    print(event)
    return "Successfull"