# -*- coding: utf-8 -*-
from g4g import db


class Opportunity(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.Text(500))

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User', backref=db.backref('opportunities', lazy='dynamic'))

    def __init__(self, title, description, owner):
        self.title = title
        self.username = description
        self.owner = owner

    def __repr__(self):
        return '<Opportunity %r>' % self.title
