from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Meetup, User 
import json
from datetime import datetime

views = Blueprint('views', __name__) # define blueprint for our application


@views.route('/', methods=['GET', 'POST']) #decorator: whenever you go to the / URL, whatever in hom() will run
@login_required
def overview():
    return render_template("overview.html", user=current_user)

@views.route('/create', methods=['GET', 'POST']) #decorator: whenever you go to the / URL, whatever in hom() will run
@login_required
def create():
    if request.method == 'POST':
        meetup_date = request.form.get('date')
        date = datetime.strptime(meetup_date, '%Y-%m-%dT%H:%M')   
        title = request.form.get('title')
        location = request.form.get('location')
        description = request.form.get('description')
        invitations = request.form.get('invitations')  
        invitations = invitations.strip()
        if invitations.find(current_user.email) == -1:     
            invitations = current_user.email + " " + invitations
        attendees = invitations.split(' ')
        invitations = " " + invitations + " "
        new_meetup = Meetup(date_meetup=date, title=title, location=location, description=description, invitations=invitations, confirmed = '', declined = '', owner=current_user.id)
        
        no_error = True
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
    return render_template("create.html", user=current_user)

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
    confirmationList = confirmation.split("   ")
    #cache.clear()

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
    confirmRemove = ' ' + str(current_user.id) + ' '
    if meetup:
        meetup.confirmed = meetup.confirmed.replace(confirmRemove, '', 1)
        current_user.meetups.remove(meetup)
        meetup.invitations = meetup.invitations.replace(current_user.email + ' ', '', 1)
        if meetup.declined == "":
            meetup.declined = current_user.first_name
        else:
            meetup.declined = meetup.declined + ", " + current_user.first_name
        db.session.commit()
        flash("\"" + meetup.title + "\" meetup declined.", category = 'error')
    
    return jsonify({})

@views.route('/delete-meetup', methods=['POST'])
def delete_meetup():
    meetup = json.loads(request.data)
    meetupId = meetup['meetupId']
    meetup = Meetup.query.get(meetupId)
    if meetup:
        flash("\"" + meetup.title + "\" meetup deleted.", category = 'error')
        db.session.delete(meetup)
        db.session.commit()
    
    return jsonify({})

@views.route('/new-owner', methods=['POST'])
def new_owner():
    meetup = json.loads(request.data)
    meetupId = meetup['meetupId']
    meetup = Meetup.query.get(meetupId)
    owner = json.loads(request.data)
    ownerEmail = owner['newOwner']
    ownerEmail = ownerEmail.strip()
    print(ownerEmail)
    user = User.query.filter_by(email=ownerEmail).first()
    invited = False
    print("MeetupId: " + str(meetup.id))
    if user:
        for userMeetups in user.meetups:
            print("userMeetups.id: " + str(userMeetups.id))
            if userMeetups.id == meetupId:
                invited = True
                break
        if invited:
            meetup.owner = user.id
            db.session.commit()
            flash('Ownership of \"' + meetup.title + '\" has successfully been transferred to ' + user.first_name + ".", category = 'success')
        else:
            flash(user.email + " is not invited to the meetup. They must be invited before you can transfer ownership.", category = 'error')
    else:
        flash('There is no user registered with email \"' + ownerEmail + "\".", category = 'error')
    
    return jsonify({})

@views.route('/invite-users', methods=['POST'])
def invite_users():
    meetup = json.loads(request.data)
    meetupId = meetup['meetupId']
    meetup = Meetup.query.get(meetupId)
    invites = json.loads(request.data)
    fullInvites = invites['invites']
    fullInvites = fullInvites.strip()
    newAttendees = fullInvites.split(' ')
    no_error = True
    for newPerson in newAttendees:
        user = User.query.filter_by(email=newPerson).first()
        if user:
            print("User found!")
            if meetup.invitations.find(" " + newPerson + " ") == -1:
                print("User not present!")
                arr = meetup.declined.split(', ')
                print(arr)
                if user.first_name in arr:
                    arr.remove(user.first_name)
                    print(arr)
                    if arr: # if arr isn't empty, put meetup.declined back together
                        first = True
                        for names in arr:
                            if first:
                                meetup.declined = names
                                first = False
                            else:
                                meetup.declined = meetup.declined + ", " + names
                    else:
                        meetup.declined = ''
                        print("cleared declined")
                user.meetups.append(meetup)
                meetup.invitations = meetup.invitations + newPerson + " "
            else:
                flash("\"" + user.first_name + "\" is already invited to this meetup. Please only add users that are not already invited. ", category='error')
                no_error = False
        else: 
            flash('There is no account associated with \"' + newPerson + '\". Please ensure the email invitations are in the correct format.', category='error')
            no_error = False
    if no_error:
        print("User sent!")
        db.session.commit()
        flash('Invitations sent!', category='success')
    else:
        flash('There was an error sending the invitations. Please try again.', category='error')
    return jsonify({})