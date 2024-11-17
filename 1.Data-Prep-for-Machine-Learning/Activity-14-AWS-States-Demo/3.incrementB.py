from __future__ import print_function
import json
print("Function Loading in Progress")
def lambda_handler(event, context):
    B = event['B']
    B = B + 1
    output = {"B": B}
    return (output)
print("Function Loaded")