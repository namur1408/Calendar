from flask import Blueprint, render_template, flash, redirect, request, url_for
from datetime import datetime
from db_config import db
from forms import EventForm
from models import Event

app = Blueprint('app', __name__)

@app.route('/')
def __index__():
    events = Event.query.order_by(Event.date).all()
    return render_template('index.html', events=events)
