from app import db
from app.models import User, ActivityDef, ActivityRec
import datetime

# run this first
#rm data-dev.sqlite
#rm -rf migrations
#
#flask db init
#flask shell
# - db.create_all()

# create the default activities

bp = ActivityDef(name='Flat Bench Press')
ex = ActivityDef(name='Back Squat')
dl = ActivityDef(name='Deadlift')
fs = ActivityDef(name='Front Squat')
oh = ActivityDef(name='Overhead Press')
db.session.add_all([bp, ex, dl, fs, oh])
db.session.commit()

u = User()
u.email = 'user@test.com'
u.username = 'Charles'
u.password_hash = 'pbkdf2:sha256:50000$oEBAvy5x$22f6446600b2c52193e2a312d4e1945fe7b8cb0a2cc820e94f8c52bb2f9a78b5' # 'test'
u.name = 'Charles'
u.location = 'United States'
u.about_me  = 'I am the test user'
u.confirmed = True

db.session.add(u)
db.session.commit()

class ExampleActivityRec:
  def __init__(self, activitydef_id, user_id, weight, reps, logged):
    ar = ActivityRec()
    ar.activitydef_id = activitydef_id
    ar.user_id = user_id
    ar.weight = weight
    ar.reps = reps
    ar.logged = logged
    db.session.add(ar)
    db.session.commit()

ExampleActivityRec(1, 2, 225, 8, datetime.datetime(2018, 5, 3))
ExampleActivityRec(1, 2, 245, 6, datetime.datetime(2018, 5, 3))
ExampleActivityRec(1, 2, 275, 4, datetime.datetime(2018, 5, 3))

ExampleActivityRec(1, 2, 225, 8, datetime.datetime(2018, 5, 6))
ExampleActivityRec(1, 2, 245, 6, datetime.datetime(2018, 5, 6))
ExampleActivityRec(1, 2, 275, 4, datetime.datetime(2018, 5, 6))

ExampleActivityRec(1, 2, 235, 8, datetime.datetime(2018, 5, 9))
ExampleActivityRec(1, 2, 255, 6, datetime.datetime(2018, 5, 9))
ExampleActivityRec(1, 2, 285, 4, datetime.datetime(2018, 5, 9))

ExampleActivityRec(1, 2, 225, 8, datetime.datetime(2018, 5, 15))
ExampleActivityRec(1, 2, 265, 6, datetime.datetime(2018, 5, 15))
ExampleActivityRec(1, 2, 285, 4, datetime.datetime(2018, 5, 15))

ExampleActivityRec(1, 2, 245, 8, datetime.datetime(2018, 5, 18))
ExampleActivityRec(1, 2, 275, 6, datetime.datetime(2018, 5, 18))
ExampleActivityRec(1, 2, 285, 4, datetime.datetime(2018, 5, 18))

ExampleActivityRec(1, 2, 245, 8, datetime.datetime(2018, 5, 21))
ExampleActivityRec(1, 2, 275, 6, datetime.datetime(2018, 5, 21))
ExampleActivityRec(1, 2, 285, 4, datetime.datetime(2018, 5, 21))

ExampleActivityRec(1, 2, 245, 8, datetime.datetime(2018, 5, 26))
ExampleActivityRec(1, 2, 255, 6, datetime.datetime(2018, 5, 26))
ExampleActivityRec(1, 2, 275, 4, datetime.datetime(2018, 5, 26))

ExampleActivityRec(1, 2, 245, 8, datetime.datetime(2018, 5, 29))
ExampleActivityRec(1, 2, 255, 6, datetime.datetime(2018, 5, 29))
ExampleActivityRec(1, 2, 285, 4, datetime.datetime(2018, 5, 29))

ExampleActivityRec(1, 2, 255, 8, datetime.datetime(2018, 6, 2))
ExampleActivityRec(1, 2, 265, 6, datetime.datetime(2018, 6, 2))
ExampleActivityRec(1, 2, 295, 4, datetime.datetime(2018, 6, 2))


ExampleActivityRec(2, 1, 305, 6, datetime.datetime(2018, 5, 4))
ExampleActivityRec(2, 1, 325, 4, datetime.datetime(2018, 5, 4))
ExampleActivityRec(2, 1, 345, 2, datetime.datetime(2018, 5, 4))

ExampleActivityRec(2, 1, 305, 6, datetime.datetime(2018, 5, 7))
ExampleActivityRec(2, 1, 325, 4, datetime.datetime(2018, 5, 7))
ExampleActivityRec(2, 1, 345, 2, datetime.datetime(2018, 5, 7))

ExampleActivityRec(2, 1, 315, 6, datetime.datetime(2018, 5, 10))
ExampleActivityRec(2, 1, 335, 4, datetime.datetime(2018, 5, 10))
ExampleActivityRec(2, 1, 355, 2, datetime.datetime(2018, 5, 10))

ExampleActivityRec(2, 1, 315, 6, datetime.datetime(2018, 5, 16))
ExampleActivityRec(2, 1, 345, 4, datetime.datetime(2018, 5, 16))
ExampleActivityRec(2, 1, 355, 2, datetime.datetime(2018, 5, 16))

ExampleActivityRec(2, 1, 325, 6, datetime.datetime(2018, 5, 19))
ExampleActivityRec(2, 1, 345, 4, datetime.datetime(2018, 5, 19))
ExampleActivityRec(2, 1, 365, 2, datetime.datetime(2018, 5, 19))

ExampleActivityRec(2, 1, 325, 6, datetime.datetime(2018, 5, 23))
ExampleActivityRec(2, 1, 345, 4, datetime.datetime(2018, 5, 23))
ExampleActivityRec(2, 1, 365, 2, datetime.datetime(2018, 5, 23))

ExampleActivityRec(2, 1, 315, 6, datetime.datetime(2018, 5, 27))
ExampleActivityRec(2, 1, 335, 4, datetime.datetime(2018, 5, 27))
ExampleActivityRec(2, 1, 355, 2, datetime.datetime(2018, 5, 27))

ExampleActivityRec(2, 1, 335, 6, datetime.datetime(2018, 5, 30))
ExampleActivityRec(2, 1, 355, 4, datetime.datetime(2018, 5, 30))
ExampleActivityRec(2, 1, 365, 2, datetime.datetime(2018, 5, 30))

ExampleActivityRec(2, 1, 335, 4, datetime.datetime(2018, 6, 3))
ExampleActivityRec(2, 1, 365, 4, datetime.datetime(2018, 6, 3))
ExampleActivityRec(2, 1, 385, 2, datetime.datetime(2018, 6, 3))


ExampleActivityRec(3, 1, 355, 3, datetime.datetime(2018, 5, 5))
ExampleActivityRec(3, 1, 375, 2, datetime.datetime(2018, 5, 5))

ExampleActivityRec(3, 1, 365, 4, datetime.datetime(2018, 5, 8))
ExampleActivityRec(3, 1, 375, 2, datetime.datetime(2018, 5, 8))

ExampleActivityRec(3, 1, 365, 3, datetime.datetime(2018, 5, 11))
ExampleActivityRec(3, 1, 385, 2, datetime.datetime(2018, 5, 11))

ExampleActivityRec(3, 1, 365, 4, datetime.datetime(2018, 5, 17))
ExampleActivityRec(3, 1, 385, 2, datetime.datetime(2018, 5, 17))

ExampleActivityRec(3, 1, 325, 6, datetime.datetime(2018, 5, 20))
ExampleActivityRec(3, 1, 375, 4, datetime.datetime(2018, 5, 20))

ExampleActivityRec(3, 1, 385, 2, datetime.datetime(2018, 5, 24))
ExampleActivityRec(3, 1, 395, 1, datetime.datetime(2018, 5, 24))

ExampleActivityRec(3, 1, 375, 2, datetime.datetime(2018, 5, 28))
ExampleActivityRec(3, 1, 385, 2, datetime.datetime(2018, 5, 28))

ExampleActivityRec(3, 1, 335, 6, datetime.datetime(2018, 6, 1))
ExampleActivityRec(3, 1, 375, 2, datetime.datetime(2018, 6, 1))

ExampleActivityRec(3, 1, 365, 3, datetime.datetime(2018, 6, 4))
ExampleActivityRec(3, 1, 385, 2, datetime.datetime(2018, 6, 4))

