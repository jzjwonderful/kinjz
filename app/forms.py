#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""declarate form class"""

from flask_wtf import Form
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired
from 

class KinForm(Form):
    pk1 = StringField(validators=[DataRequired()])
    pk2 = StringField(validators=[DataRequired()])
    submit = SubmitField(label='PK')
