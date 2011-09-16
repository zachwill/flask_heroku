"""
WTForms Documentation:    http://wtforms.simplecodes.com/
Flask WTForms Patterns:   http://flask.pocoo.org/docs/patterns/wtforms/
Flask-WTF Documentation:  http://packages.python.org/Flask-WTF/

Forms for your application can be stored in this file.
"""

from flaskext.wtf import Form, SubmitField, TextField, Required, Email

class ExampleForm(Form):
    """Just a simple example form."""
    name = TextField('Name', validators=[Required()])
    email = TextField('Email', validators=[Email()])
    location = TextField('Location')
    submit = SubmitField('Submit')
