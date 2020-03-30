from flask import jsonify
import json

def handle_error(fn):
    def decorator(*args, **kwargs):
        try:
            return jsonify(json.loads(fn(*args, **kwargs).to_json())), 200
        except Exception as e:
            return jsonify(str(e)), 500
    return decorator