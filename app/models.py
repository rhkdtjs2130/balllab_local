from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    username = db.Column(db.String(120), unique=False, nullable=False)
    birth = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    password_date = db.Column(db.Date, nullable=False, server_default="2022-09-20")
    point = db.Column(db.Integer, nullable=False, server_default="0")
    user_type = db.Column(db.Integer, nullable=False, server_default="0")
    agreement = db.Column(db.Integer, nullable=False, server_default="1")
    agreement_option = db.Column(db.Integer, nullable=False, server_default="1")
    register_date = db.Column(db.Date, nullable=False, server_default="2022-09-21")
    
class BuyPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(150), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    username = db.Column(db.String(120), unique=False, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    product = db.Column(db.String(120), nullable=False)
    area = db.Column(db.String(120), nullable=False)
    date = db.Column(db.Date, unique=False, nullable=False)
    time = db.Column(db.String(120), unique=False, nullable=False)
    buy = db.Column(db.Integer, nullable=False, server_default="0")
    
class ReserveCourt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    area = db.Column(db.String(120), unique=False, nullable=False)
    time = db.Column(db.String(120), unique=False, nullable=False)
    court = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.String(150), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    username = db.Column(db.String(120), unique=False, nullable=False)
    buy = db.Column(db.Integer, nullable=False, server_default="0")
    mul_no = db.Column(db.String(120), unique=False, server_default="0")
    qr_path = db.Column(db.String(120), unique=False)
    
class PayDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mul_no = db.Column(db.String(120), unique=False, nullable=False, server_default="NA")
    goodname = db.Column(db.String(120), unique=False)
    date = db.Column(db.Date, nullable=True)
    area = db.Column(db.String(120), unique=False, nullable=True)
    time = db.Column(db.String(120), nullable=True)
    price = db.Column(db.Integer, unique=False, nullable=False)
    used_point = db.Column(db.Integer, nullable=False, unique=False)
    recvphone = db.Column(db.String(120), unique=False, nullable=False)
    pay_date = db.Column(db.DateTime, nullable=False)
    pay_type = db.Column(db.String(120), nullable=False)
    pay_state = db.Column(db.String(120), nullable=False)
    
class DoorStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(120), nullable=False, server_default='0')
    
class ReservationStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(120), nullable=False, server_default='0')
    