from __future__ import print_function
import json
print("Function Loading in Progress")
def lambda_handler(event, context):
    print(f"Addition of A and B is {event['sumAB']}")
    return(event)
print("Function Loaded")