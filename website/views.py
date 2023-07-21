from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Meetup 
import json

views = Blueprint('views', __name__) # define blueprint for our application

@views.route('/', methods=['GET', 'POST']) #decorator: whenever you go to the / URL, whatever in hom() will run
@login_required
def home():
    if request.method == 'POST':
        date_meetup = request.form.get('meetup_time')
        title = request.form.get('meetup_time')
        location = request.form.get('meetup_time')
        description = request.form.get('meetup_time')
        invitations = request.form.get('meetup_time')
        owner = request.form.get('meetup_time')
        new_meetup = Meetup(date_meetup=date_meetup, title=title, location=location, description=description, invitations=invitations, owner=owner)
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