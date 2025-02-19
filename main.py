import json
import logging
from datetime import datetime, timezone

from flask import Flask, request, jsonify

# from flask_oauth import OAuth
from db_manager import LinkDB

# oauth = OAuth()
app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG)


@app.route("/", methods=["GET"])
def hello_world():
    response = {"hello": "world"}
    return jsonify(response), 200


@app.route("/link", methods=['POST'])
def create_shortened_link():
    try:
        data = json.loads(request.data)
        modified = "modified"  # to be done
        dt = datetime.now(timezone.utc)
        modified = LinkDB().add_link(data["link"], modified, dt)
        return jsonify({"your link": modified.modified,
                        "duration": modified.duration}), 201
    except Exception as e:
        logger.error(e)
        return jsonify({"error": "The link is incorrect. Please try again later"}), 400
