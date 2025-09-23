import flask
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

@app.route('/add', methods=['GET', 'POST'])
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        new_event = Event(
            title=form.title.data,
            description=form.description.data,
            date=form.date.data
        )
        db.session.add(new_event)
        db.session.commit()
        flash('Event added successfully.', 'success')
        return redirect(url_for('index'))
    return render_template('add_event.html', form=form)