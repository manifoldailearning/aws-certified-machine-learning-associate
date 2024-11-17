from __future__ import print_function
import json
print("Function Loading in Progress")
def lambda_handler(event, context):
    A = event['A']
    A = A + 1
    output = {"A": A}
    return (output)
print("Function Loaded")