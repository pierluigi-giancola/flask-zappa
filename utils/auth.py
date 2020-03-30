from flask import request, jsonify, g
import jwt
import json
import functools
import app

def protected(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if ('HTTP_AUTHORIZATION' not in request.environ):
            return jsonify(auth='No auth provided'), 401
        else:
            try:
                identity = jwt.decode(request.environ['HTTP_AUTHORIZATION'][7:], app.config['JWT_SECRET_KEY'], algorithms=[app.config['JWT_ALGORITHM']], verify=False)
                g.jwt = identity
            except Exception as e:
                return jsonify(auth='Error while decoding JWT'+ str(e)), 401
        return f(*args, **kwargs)
    return decorated_function
