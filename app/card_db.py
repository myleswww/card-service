# -*- coding: utf-8 -*-

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
from pathlib import Path

def get_db():
    '''Gets the database, fix line 13, it is causing a key value error'''

    data_folder = Path("/home/pi/card-scan-service/instance/") #make a path using pathlib

    file_to_open = data_folder / "app.sqlite" #the database file.

    if 'db' not in g:
        g.db = sqlite3.connect(
            file_to_open,
            detect_types=sqlite3.PARSE_DECLTYPES
            )
        g.db.row_factory = sqlite3.Row
        
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    
    if db is not None:
        db.close()
        
def init_db():
    db = get_db()
    
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        
@click.command('init-db')
@with_appcontext
def init_db_command():
    '''clear existing data and create new tables'''
    init_db()
    click.echo('Initialized the database')
    
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)