from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True, unique=False)
    lastname = db.Column(db.String(120), index=True, unique=False)
    accel = db.relationship('Accel', backref='user', lazy='dynamic')
    gps = db.relationship('GPS', backref='user', lazy='dynamic')
   
    def __repr__(self):
        return '<User %r>' % (self.lastname) #onlyfordebug

class Accel(db.Model):
    timestamp = db.Column(db.DateTime, primary_key = True)
    module = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Accel %r>' % (self.module)


class GPS(db.Model):
    timestamp = db.Column(db.DateTime, primary_key = True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    user_id = db.Column(db.Float, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<GPS %r>' % (self.altitude)


