from app.ext import db

class Userok(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user=db.Column(db.String(88))
    age=db.Column(db.String(44))
    addr=db.Column(db.String(88))
    
    def save(self):
        db.session.add(self)
        db.session.commit()