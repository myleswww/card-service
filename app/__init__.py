import os
from flask import Flask, request, jsonify
from . import card_db
app = Flask(__name__, instance_relative_config=True)

def create_app(test_config=None):
    #create and configure app
    
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
    
    
    card_db.init_app(app)
    
    return app



@app.route('/records', methods=['GET', 'POST'])
def api_all():
    db = card_db.get_db()
    if request.method == 'POST':
        card_id = request.args.get('card_id')
        date_time = request.args.get('date_time')
        db.execute(
            'INSERT INTO card_scans (card_id, scan_timestamp) VALUES (?, ?)',
            (card_id, date_time))
        db.commit()
    



    