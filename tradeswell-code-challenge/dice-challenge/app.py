from flask import Flask, request
from src.dice_calculator import DiceCalculator
import os, json

app = Flask(__name__)

@app.route('/run_tasks', methods=['GET', 'POST'])
def run_tasks():
    data = request.get_json()['pkg']
    result = []
    for job in data:
        dc = DiceCalculator(job)
        dc.compute_graph()
        result.append({"roll-result" : dc.random_value,
                         "roll-min" : dc.min_value,
                         "roll-max" : dc.max_value
                        })
                        
    return json.dumps(result)


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)


