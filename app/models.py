# coding:utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:asd123@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


# user
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)  # personal introduction
    face = db.Column(db.String(255), unique=True)  # avatar
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # register time
    uuid = db.Column(db.String(255), unique=True)  # unique identifier
    userlogs = db.relationship('Userlog', backref='user')  # foreignKey - userlog
    comments = db.relationship('Comment', backref='user')  # foreignKey - comments
    moviecols = db.relationship('Moviecol', backref='user')  # foreignKey - favorite movie

    def __repr__(self):
        return "<User %r>" % self.name


# user log
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # login time

    def __repr__(self):
        return "<Userlog %r" % self.id

# label
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # login time
    movies = db.relationship("Movie",backref = 'tag') # foreignkey - movie

    def __repr__(self):
            return "<Tag %r" % self.name

#movie
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True) #cover
    star = db.Column(db.SmallInteger)
    playnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    area = db.Column(db.String(255)) #release area
    release_time = db.Column(db.Date)
    length = db.Column(db.String(100)) #how long the movie
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # login time
    comments = db.relationship('Comment', backref='movie')  # foreignKey - comments
    moviecols = db.relationship('Moviecol', backref='movie')  # foreignKey - favorite movie

    def __repr__(self):
            return "<Movie %r" % self.title

#preview
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    logo = db.Column(db.String(255), unique=True) #cover
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # login time

    def __repr__(self):
            return "<Preview %r" % self.title

#comments
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id')) #which movie blelong to
    user_id = db.Column(db.Integer, db.ForeignKey('movie.id')) #which user blelong to
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # login time

    def __repr__(self):
            return "<Preview %r" % self.id

#favoriate
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id')) #which movie blelong to
    user_id = db.Column(db.Integer, db.ForeignKey('movie.id')) #which user blelong to
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # login time

    def __repr__(self):
            return "<Moviecol %r" % self.id

#authority
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url= db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # login time

    def __repr__(self):
            return "<Auth %r" % self.name

#role
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    auths = db.Column(db.String(600)) #auth list
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # login time

    def __repr__(self):
        return "<Role %r" % self.name
