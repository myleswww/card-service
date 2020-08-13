# -*- coding: utf-8 -*-
import os
from flask import Flask, request, jsonify
from . import card_db
import logging
<<<<<<< Updated upstream
=======
import json
>>>>>>> Stashed changes
app = Flask(__name__, instance_relative_config=True)


def create_app(test_config=None):
    '''create and configure app'''
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )
    
    if test_config is None:
        #load the instance config
        app.config.from_pyfile('config.py', silent=True)
    else:
        #load test config
        app.conig.from_mapping(test_config)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    try:
        card_db.init_app(app)
    except KeyError:
        logging.exception('There was a database key error' )
        raise
    
    return app



@app.route('/records', methods=['GET', 'POST'])
def api_all():
    db = card_db.get_db()
    if request.method == 'POST':

        card_id = request.json.get('card_id')
        date_time = request.json.get('date_time')
        print(card_id)
        print(date_time)

        db.execute(
            "INSERT INTO card_scans (card_id, scan_timestamp) VALUES (?, ?)",
            [card_id, date_time]
        )

        db.execute()
        db.close()
    



    