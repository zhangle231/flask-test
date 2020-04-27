import sqlalchemy

from sqlalchemy import create_engine

engine = create_engine('sqlite:///foo.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String

from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  fullname = Column(String)
  nickname = Column(String)
  def __repr__(self):
    return "<User(name='%s', fullname='%s', nickname='%s')>" % (
           self.name, self.fullname, self.nickname)

class Address(Base):
  __tablename__ = 'addresses'
  id = Column(Integer, primary_key=True)
  email_address = Column(String, nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship("User", back_populates="addresses")

  def __repr__(self):
    return "<Address(email_address='%s')>" % self.email_address


User.addresses = relationship("Address", order_by=Address.id, back_populates="user")

Base.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

session.add(ed_user)

session.commit()

our_user = session.query(User).filter_by(name='ed').first()

print(our_user)

our_user.nickname = 'eddie'

print(session.dirty)

session.commit()

for instance in session.query(User).order_by(User.id):
  print(instance.name,instance.fullname)


jack = User(name='jack',fullname='Jack Bean',nickname='gjffdd')
jack.addresses = [
                Address(email_address='jack@google.com'),
                Address(email_address='j25@yahoo.com')]

print(jack.addresses)

print(jack.addresses[1].user)

#session.add(jack)
#session.commit()

jack = session.query(User).filter_by(name='jack').one()
print(jack)
print(jack.addresses)

for u,a in session.query(User, Address).filter(User.id==Address.user_id)\
                                       .filter(Address.email_address=='jack@google.com').all():
  print(u)
  print(a)

print('--------------')

jack = session.query(User).join(Address).filter(Address.email_address=='jack@google.com').all()
print(jack)

print('------------')

query = session.query(User,Address).select_from(Address).join(User)
for a in query:
  print(a)
