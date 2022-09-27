from project3nobel.app import db 

class nobel1_prize(db.Model):
    __tablename__ = 'nobel1_prize'
    
    awardyear        = db.Column(db.Integer) 
    category         = db.Column(db.String(100))
    categoryfullname = db.Column(db.String(200))
    sortorder        = db.Column(db.Integer) 
    prizeamount      = db.Column(db.Integer) 
    motivation       = db.Column(db.String(1000))
    award_link       = db.Column(db.String(100))
    id               = db.Column(db.Integer)
    name             = db.Column(db.String(50))
    fullname         = db.Column(db.String(100))
    gender           = db.Column(db.String(20))
    laureate_link    = db.Column(db.String(100))
    birth_date       = db.Column(db.String(100))
    birth_citynow    = db.Column(db.String(200))
    birth_continent        = db.Column(db.String(20))
    birth_countrynow       = db.Column(db.String(20))
    birth_locationstring = db.Column(db.String(100)) 
            

    def __repr__(self):
        return '<nobel1_prize %r>' % (self.name)



class country(db.Model):
    __tablename__ = 'country'

     
    id               = db.Column(db.Integer) 
    firstname        = db.Column(db.String(100))
    surname          = db.Column(db.String(200))
    borncountry      = db.Column(db.String(100)) 
    borncountry_code  = db.Column(db.String(100)) 
    born_city         = db.Column(db.String(1000))
    gender           = db.Column(db.String(100))
    year             = db.Column(db.Integer)
    category         = db.Column(db.String(50))
    motivation       = db.Column(db.String(100))
    organization_name  = db.Column(db.String(20))
    organization_city  = db.Column(db.String(100))
    organization_country= db.Column(db.String(100))
    latitude   = db.Column(db.Float)
    longitude   = db.Column(db.Float)
    

    
    def __repr__(self):
        return '<country %r>' % (self.name)