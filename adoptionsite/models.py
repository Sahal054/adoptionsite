from adoptionsite import db

class Puppies(db.Model):
    __tablename__ = "puppies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner=db.relationship('Owner',backref='puppies',uselist=False)


    def __init__(self,name):
        self.name = name


    def __repr__(self):
        if self.owner:
            return f"the puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f" puppy name:{self.name} has no owner assigned "



class Owner(db.Model):
    __tablename__="owner"


    id=db.Column(db.Integer,primary_key=True)
    pup_id=db.Column(db.Integer,db.ForeignKey("puppies.id"))
    name=db.Column(db.Text)

    def __init__(self,name,pup_id):

        self.name = name
        self.pup_id=pup_id



    def __repr__(self):
        return f"the owner is {self.name}"
