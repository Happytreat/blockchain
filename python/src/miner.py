import json
import requests
from flask import Flask, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler


"""
	Miner periodically sends GET request to /mine new transactions.
"""

# Instantiate the Node
app = Flask(__name__)


def mine(port):
    print("Mining has begun...")
    node = f"localhost:{port}"
    try:
        response = requests.get(f"http://{node}/mine")

        if response.status_code == 200:
            print(response.json())
        else:
            print("Mining has failed")

        print("Mining has ended...")
        pass
    except requests.exceptions.ConnectionError:
        print(f"Node: {node} not responding")
        print("Mining has ended...")
        pass


# Periodically schedule mining for new transactions
sched = BackgroundScheduler()  # Scheduler object
sched.start()

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5001, type=int, help="port to listen on", dest="port"
    )
    parser.add_argument(
        "-n",
        "--node",
        default=5000,
        type=int,
        help="port to send request to",
        dest="node",
    )
    args = parser.parse_args()
    port = args.port
    node = args.node
    sched.add_job(mine, "interval", seconds=5, args={node})

    app.run(host="0.0.0.0", port=port)
