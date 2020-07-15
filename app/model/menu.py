from app import my_db

class Menu(my_db.Model):
    id   = my_db.Column(my_db.Integer, primary_key=True)
    pid  = my_db.Column(my_db.Integer)
    name = my_db.Column(my_db.String(50))
    url  = my_db.Column(my_db.String(50))

    def __repr__(self):
        return 'menu id:%r, pid:%r, name:%r, url:%r' % (self.id, self.pid, self.name, self.url)
