import logging
import json
import azure.functions as func
import math

def numerical_integration_combined(lower, upper):
    def f(x):
        return abs(math.sin(x))

    def numerical_integration(lower, upper, N):
        interval_width = (upper - lower) / N
        result = 0.5 * (f(lower) + f(upper))  # Area of the first and last rectangles

        for i in range(1, N):
            x_i = lower + i * interval_width
            result += f(x_i)

        result *= interval_width
        return result

    results_dict = {}

    for i in range(0, 7):
        result = numerical_integration(lower, upper, 10**i)
        results_dict[f"result_{10**i}_intervals"] = result

    return json.dumps(results_dict, indent=2)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    lower = float(req.params.get('lower', '0'))
    upper = float(req.params.get('upper', '3.14159'))

    if not (0 <= lower <= upper):
        return func.HttpResponse("Invalid input. Lower bound must be less than or equal to upper bound.", status_code=400)

    result_json = numerical_integration_combined(lower, upper)

    return func.HttpResponse(result_json, mimetype="application/json", status_code=200)

