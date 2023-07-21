from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Meetup, User 
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
        new_meetup = Meetup(date_meetup=date, title=title, location=location, description=description, invitations=invitations, owner=current_user.id)
        flash('Meetup added!', category='success')

        no_error = True
        attendees = invitations.split(' ')
        for person in attendees:
            if person != current_user.email:
                user = User.query.filter_by(email=person).first()
                if user:
                    user.meetups.append(new_meetup)
                    print('WOOHOO')
                else:
                    flash('There is no account associated with ' + person + '. Please ensure the email invitations are in the correct format.', category='error')
                    no_error = False
        if no_error:
            current_user.meetups.append(new_meetup)
            db.session.add(new_meetup)
            db.session.commit()
        else:
            flash('There was an error creating this meetup. Please try again.', category='error')
        """if len(note) < 1:
            flash('Note is too short!', category='error')
        else:"""
            


    return render_template("home.html", user=current_user)

@views.route('/view_meetups', methods=['GET', 'POST']) #decorator: whenever you go to the / URL, whatever in hom() will run
@login_required
def view_meetups():         
    return render_template("view_meetups.html", user=current_user)
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