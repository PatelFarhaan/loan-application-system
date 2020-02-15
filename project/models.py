from project import db

########################################################################################################################
#################################################* DEPARTMENT *#########################################################
########################################################################################################################
class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    dob = db.Column(db.DateTime)
    email = db.Column(db.String(64))
    amount = db.Column(db.String(64))
    gender = db.Column(db.String(64))
    address = db.Column(db.String(256))
    purpose = db.Column(db.String(1000))
    telephone = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    middle_name = db.Column(db.String(64))
########################################################################################################################