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
        new_meetup = Meetup(date_meetup=date, title=title, location=location, description=description, invitations=invitations, confirmed = '', owner=current_user.first_name)
        

        no_error = True
        attendees = invitations.split(' ')
        current_user.meetups.append(new_meetup)
        for person in attendees:
            if person != current_user.email:
                user = User.query.filter_by(email=person).first()
                if user:
                    user.meetups.append(new_meetup)
                else:
                    flash('There is no account associated with \"' + person + '\". Please ensure the email invitations are in the correct format.', category='error')
                    no_error = False
        if no_error:
            db.session.add(new_meetup)
            db.session.commit()
            flash('Meetup added!', category='success')
        else:
            flash('There was an error creating this meetup. Please try again.', category='error')
    return render_template("home.html", user=current_user)

@views.route('/view_meetups', methods=['GET', 'POST']) #decorator: whenever you go to the / URL, whatever in hom() will run
@login_required
def view_meetups():
    invites = ""
    confirmation = ""
    confirmSearch = " " + str(current_user.id) + " "
    firstInv = True
    firstConf = True
    for meetup in current_user.meetups:
        invites = invites + "   "
        confirmation = confirmation + "   "
        firstInv = True
        firstConf = True
        for user in meetup.user:
            userSearch = " " + str(user.id) + " "
            if meetup.confirmed.find(userSearch)  != -1:
                if firstConf:   
                    confirmation  = confirmation + user.first_name
                    firstConf = False
                else:
                    confirmation  = confirmation + ", " + user.first_name
            else:
                if firstInv:
                    invites  = invites + user.first_name
                    firstInv = False
                else:
                    invites  = invites + ", " + user.first_name
    inviteList = invites.split("   ")
    print(inviteList)
    confirmationList = confirmation.split("   ")
    
    print(confirmSearch)
    return render_template("view_meetups.html", user=current_user, inviteList = inviteList, confirmSearch = confirmSearch, confirmationList = confirmationList)

@views.route('/confirmed', methods=['GET', 'POST'])
@login_required
def confirmed():
    invites = ""
    confirmation = ""
    confirmSearch = " " + str(current_user.id) + " "
    firstInv = True
    firstConf = True
    for meetup in current_user.meetups:
        invites = invites + "   "
        confirmation = confirmation + "   "
        firstInv = True
        firstConf = True
        for user in meetup.user:
            userSearch = " " + str(user.id) + " "
            if meetup.confirmed.find(userSearch)  != -1:
                if firstConf:   
                    confirmation  = confirmation + user.first_name
                    firstConf = False
                else:
                    confirmation  = confirmation + ", " + user.first_name
            else:
                if firstInv:
                    invites  = invites + user.first_name
                    firstInv = False
                else:
                    invites  = invites + ", " + user.first_name
    inviteList = invites.split("   ")
    print(inviteList)
    confirmationList = confirmation.split("   ")
    
    print(confirmSearch)
    return render_template("confirmed.html", user=current_user, inviteList = inviteList, confirmSearch = confirmSearch, confirmationList = confirmationList)


@views.route('/confirm-meetup', methods=['POST'])
def confirm_meetup():
    meetup = json.loads(request.data)
    meetupId = meetup['meetupId']
    meetup = Meetup.query.get(meetupId)
    if meetup:
        #db.session.update({meetup.confirmed: meetup.confirmed + " " + current_user.id})
        meetup.confirmed= meetup.confirmed + " " + str(current_user.id) + " "
        print("meetup.confirmed: " + meetup.confirmed)
        db.session.commit()
    
    return jsonify({})

@views.route('/decline-meetup', methods=['POST'])
def decline_meetup():
    meetup = json.loads(request.data)
    meetupId = meetup['meetupId']
    meetup = Meetup.query.get(meetupId)
    if meetup:
        current_user.meetups.remove(meetup)
        db.session.commit()
        flash("Meetup declined.", category = 'error')
    
    return jsonify({})