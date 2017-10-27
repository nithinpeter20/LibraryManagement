# app/models.py
"""
A script to create models 
"""

#### Libraries
# Standard library

# Third-party libraries
import urllib.request
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask.ext.bcrypt import Bcrypt

# Local imports
from app import db
from app import login_manager

bcrypt = Bcrypt()

class Users(UserMixin, db.Model):
    """
    This create a User Table which contain list of registered users
    """
    __tablename__ = 'Users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True)
    username = db.Column(db.String(60), index=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    
    @property
    def password(self):
        """
        prevent password being accessed
        """
        raise AttributeError('password is not readable')
        return self. password

    @password.setter
    def password(self, password):
        """
        Set password to hashed password
        """
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """
        Check if password matches
        """
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Users: {}>'.format(self.username)


#Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    """
    Function to load user
    """
    return Users.query.get(int(user_id))


class BookPhotos(db.Model):
    """
    Create Photos table
    """
    __tablename__ = "Book_Photos"
    image_id = db.Column(db.Integer, primary_key=True)
    image_name =  db.Column(db.String(60), index=True)
    path = db.Column(db.LargeBinary, index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('Books.book_id'))

    def __repr__(self):
        return '<BookPhotos: {}>'.format(self.name)

class Books(db.Model):
    """
    Create Books table
    """
    __tablename__ = "Books"
    book_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    author = db.Column(db.String(60), index=True)
    publication_date = db.Column(db.Date, index=True)
    rating = db.Column(db.Float, index=True)
    review = db.Column(db.TEXT, index=True)
    book_count = db.Column(db.Integer, index=True)
    image = db.relationship('BookPhotos', backref='Book_Photos',lazy='dynamic')

    def __repr__(self):
        return '<Books: {}>'.format(self.name)    