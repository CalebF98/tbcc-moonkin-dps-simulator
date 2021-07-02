from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, NumberRange

class SimParamsForm(FlaskForm):
	intellect  = IntegerField('Intellect', 					[NumberRange(0,1000)])
	spellpower = IntegerField('Spellpower',         [NumberRange(0,1000)])
	hit        = IntegerField('Spell Hit Rating',   [NumberRange(0,202)])
	crit       = IntegerField('Spell Crit Rating',  [NumberRange(0,500)])
	haste      = IntegerField('Spell Haste Rating', [NumberRange(0,1000)])
	num_fights = IntegerField('# of fights to simulate', [NumberRange(1,2500)])