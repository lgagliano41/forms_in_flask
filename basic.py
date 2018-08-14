from flask import Flask, render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateTimeField,
                    RadioField,SelectField,
                    TextField,TextAreaField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class InfoForm(FlaskForm):

    breed = StringField('What breed are you?',validators=[DataRequired])
    neutered = BooleanField('Have you been neutered?')
    mood = RadioField('Please choose your mood:',
                        choices=[('mood_one','Happy'),('mood_two','excited')])
    food_choice = SelectField(u'Pick your favorite food:',
                        choices=[('chi','chicken'),('bf','beef'),
                            ('fish','Fish')])
    feedback = TextAreaField()
    submit =SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed']= form.breed.Data
        session['neutered']= form.neutered.Data
        session['mood']= form.mood.Data
        session['food']= form.food.choice.Data
        session['feedback']= form.feedback.Data

        return redirect(url_for('thankyou'))

    return render_template('index.html',form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__=='__main__':
    app.run(debug=True)
