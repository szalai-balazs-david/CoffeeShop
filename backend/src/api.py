import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)
# db_drop_and_create_all()


@app.route('/drinks', methods=['GET'])
def app_get_drinks():
    drinks = Drink.query.all()
    data = []
    for drink in drinks:
        data.append(drink.short())
    return jsonify({
        'success': True,
        'drinks': data
    })


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def app_get_drinks_detail():
    drinks = Drink.query.all()
    data = []
    for drink in drinks:
        data.append(drink.long())
    return jsonify({
        'success': True,
        'drinks': data
    })


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def app_post_drinks():
    data = request.json
    if 'title' not in data:
        abort(422)
    if 'recipe' not in data:
        abort(422)
    drink = Drink()
    drink.title = data['title']
    drink.recipe = data['recipe']
    drink.insert()
    return jsonify({
        'success': True,
        'drinks': [drink.long()]
    })


@app.route('/drinks/<id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def app_patch_drinks(drink_id):
    data = request.json
    if 'title' not in data:
        abort(422)
    if 'recipe' not in data:
        abort(422)

    drink = Drink.query.get(drink_id)
    if drink is None:
        abort(404)

    drink.title = data['title']
    drink.recipe = data['recipe']

    drink.update()

    return jsonify({
        'success': True,
        'drinks': [drink.long()]
    })


@app.route('/drinks/<id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def app_delete_drinks(drink_id):
    drink = Drink.query.get(drink_id)
    if drink is None:
        abort(404)

    drink.delete()

    return jsonify({
        'success': True,
        'drinks': drink_id
    })


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422


@app.errorhandler(501)
def not_implemented(error):
    return jsonify({
                    "success": False,
                    "error": 501,
                    "message": "not implemented"
                    }), 501


@app.errorhandler(404)
def not_found(error):
    return jsonify({
                    "success": False,
                    "error": 404,
                    "message": "not found"
                    }), 404


@app.errorhandler(AuthError)
def not_found(error):
    # ToDo: revide if I need separate 401 and 403 or I can extract the status code from error
    return jsonify({
                    "success": False,
                    "error": 501,
                    "message": "not found"
                    }), 501
