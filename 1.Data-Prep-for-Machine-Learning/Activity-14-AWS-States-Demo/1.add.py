from __future__ import print_function
import json
print("Function Loading in Progress")
def lambda_handler(event, context):
    v1 = int(event['A'])
    v2 = int(event['B'])
    add = v1 + v2
    output = {"A" : v1, "B" : v2, "sumAB" : add} 
    return (output)
print("Function Loaded")