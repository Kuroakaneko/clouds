# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(input):
    word_separator = lambda x : (x,1)
    return list(map(word_separator, input.lower().replace('\r','').replace('b\\','').split()))

