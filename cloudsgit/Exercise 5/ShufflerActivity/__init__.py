# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

def dictionary(list):
    res = {}
    for i in list:
        if(res.get(i[0])):
            res[i[0]] = res.get(i[0]) + [i[1]]
        else:
            res[i[0]] = [i[1]]
    return res

def main(input):
    list_merger = lambda list : [i for sub_list in list for i in sub_list]
    
    data_output = dictionary(list_merger(input))

    return [(k, v) for k, v in data_output.items()]
