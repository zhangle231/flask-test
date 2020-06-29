from movie import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(80),  unique=True, nullable=False)
    img_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Movie %r-%r>' % (self.name, self.img_url)
