import json
import logging
import random
import string
from datetime import datetime, timezone, timedelta

from flask import Flask, request, jsonify

# from flask_oauth import OAuth
from db_manager import LinkDB

# oauth = OAuth()
app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG)


def _unique_generator(size=10, chars=string.ascii_uppercase + string.digits) -> str:
    return ''.join(random.choice(chars) for _ in range(size))


@app.route("/", methods=["GET"])
def hello_world():
    response = {"hello": "world"}
    return jsonify(response), 200


@app.route("/link/create", methods=['POST'])
def create_shortened_link():
    try:
        data = json.loads(request.data)
        modified = "https://opop.com/" + _unique_generator()
        dt = datetime.now(timezone.utc)
        expiration = datetime.now(timezone.utc) + timedelta(days=3)
        modified = LinkDB().add_link(data["link"], modified, dt, expiration)
        return jsonify({"your_link": modified.modified,
                        "duration_till": modified.expiration}), 201
    except Exception as e:
        logger.error(e)
        return jsonify({"error": "The link is incorrect. Please try again later"}), 400
