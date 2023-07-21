from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Meetup 
import json
from datetime import datetime

views = Blueprint('views', __name__) # define blueprint for our application

@views.route('/', methods=['GET', 'POST']) #decorator: whenever you go to the / URL, whatever in hom() will run
@login_required
def home():
    if request.method == 'POST':
        meetup_date = request.form.get('date')
        date = datetime.strptime(meetup_date, '%Y-%m-%dT%H:%M')   
        title = request.form.get('title')
        location = request.form.get('location')
        description = request.form.get('description')
        invitations = request.form.get('invitations')
        owner = request.form.get('owner')
        new_meetup = Meetup(date_meetup=date, title=title, location=location, description=description, invitations=invitations, owner=owner)
        db.session.add(new_meetup)
        db.session.commit()
        flash('Meetup added!', category='success')

        """if len(note) < 1:
            flash('Note is too short!', category='error')
        else:"""
            


    return render_template("home.html", user=current_user)
"""
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})"""