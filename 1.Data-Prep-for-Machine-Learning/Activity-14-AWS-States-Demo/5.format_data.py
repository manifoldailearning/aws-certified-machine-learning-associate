from __future__ import print_function
import json
print("Function Loading in Progress")
def lambda_handler(event, context):
    output = {"A":event[0]['A'], "B":event[1]['B']}
    return(output)
print("Function Loaded")