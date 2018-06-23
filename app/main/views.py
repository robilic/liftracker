from flask import Flask, render_template, session, redirect, url_for, abort, flash, request,\
    current_app, make_response, jsonify
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
from sqlalchemy import func
from sqlalchemy.sql import label
from datetime import datetime
from . import main
from .forms import EditProfileForm, NameForm, ActivityRecForm
from .. import db
from ..models import Role, User, ActivityRec, ActivityDef

import logging
#from ..decorators import admin_required, permission_required

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    activityrecs = current_user.activityrecs
    return render_template('index.html', name=current_user.name, activityrecs=activityrecs)

@main.route('/activity/record',  methods=['GET', 'POST'])
@login_required
def record_activity():
    if 'activitydef_id' not in session:
        session['activitydef_id'] = 1
    if 'logged' not in session:
        session['logged'] = datetime.now().strftime('%Y-%m-%d')

    form = ActivityRecForm(activitydef_id=session['activitydef_id'], logged=datetime.strptime(session['logged'], '%Y-%m-%d'))

    activity_choices = []
    activity_list = ActivityDef.query.all()

    for i in activity_list:
        activity_choices.append((i.id, i.name))

    form.activitydef_id.choices = activity_choices

    if form.validate_on_submit():
        session['activitydef_id'] = form.activitydef_id.data
        session['logged'] = form.logged.data.strftime('%Y-%m-%d')
        new_activityrec = ActivityRec(weight=form.weight.data, reps=form.reps.data, 
                                logged=form.logged.data, activitydef_id=form.activitydef_id.data,
                                user_id=current_user.id)
        db.session.add(new_activityrec)
        db.session.commit()
        current_app.logger.info('Valid activityrec submitted')
        current_app.logger.info('form.activitydef_id.data = %s, activitydef_id = %s, logged = %s' % (form.activitydef_id.data, session['activitydef_id'], session['logged']))
        return redirect(url_for('.record_activity'))

    current_app.logger.info('Invalid activityrec submitted')
    current_app.logger.info('form.activitydef_id.data = %s, activitydef_id = %s, logged= %s' % (form.activitydef_id.data, session['activitydef_id'], session['logged']))

    return render_template('record_activity.html', form=form)

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    personal_records = db.session.query(ActivityRec, ActivityDef.name, ActivityRec.logged, label('weight', db.func.max(ActivityRec.weight))).join(ActivityDef, ActivityDef.id==ActivityRec.activitydef_id).group_by(ActivityRec.activitydef_id).all()
    return render_template('user.html', user=user, prs=personal_records)

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))

    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)

@main.route('/bubble-chart-data-test', methods=['GET'])
@login_required
def bubble_chart_data_test():
    foobar = []
    foobar.append({"x": "2018-06-01", "y": 20, "r": 3})
    foobar.append({"x": "2018-06-03", "y": 25, "r": 3})
    foobar.append({"x": "2018-06-05", "y": 35, "r": 3})
    foobar.append({"x": "2018-06-06", "y": 37, "r": 3})
    foobar.append({"x": "2018-06-09", "y": 40, "r": 3})
    foobar.append({"x": "2018-06-10", "y": 43, "r": 3})

    foobaz = []
    foobaz.append({"x": "2018-06-01", "y": 40, "r": 3})
    foobaz.append({"x": "2018-06-03", "y": 50, "r": 3})
    foobaz.append({"x": "2018-06-05", "y": 60, "r": 3})
    foobaz.append({"x": "2018-06-06", "y": 65, "r": 3})
    foobaz.append({"x": "2018-06-09", "y": 71, "r": 3})
    foobaz.append({"x": "2018-06-10", "y": 74, "r": 3})

    d = [foobaz, foobar]
    return jsonify(d)

@main.route('/bubble-chart-data', methods=['GET'])
@login_required
def bubble_chart_data():
    activity_count = ActivityDef.query.count()
    reply = []

    for a_id in range(1, activity_count+1):
        foo = db.session.query(ActivityRec, ActivityRec.weight.label('weight'), ActivityRec.reps.label('reps'), ActivityRec.logged.label('logged'), ActivityRec.activitydef_id.label('activitydef_id')).filter_by(activitydef_id=a_id)
        d=[]
        for f in foo:
            r = (15 if (f.reps > 15) else (f.reps))
            d.append({"x": f.logged.strftime("%Y-%m-%d"), "y": f.weight, "r": r })
        reply.append(d)

    return jsonify(reply)

