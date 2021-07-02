import os
from dotenv import load_dotenv
from simulation import compute_avg_dps
from flask import Flask, request, render_template
from form import SimParamsForm

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/', methods=['GET','POST'])
def index():
	form = SimParamsForm()
	if request.method == 'POST' and form.validate():
		return render_template('form.html', form=form, results='Congratulations! You entered valid data.')

	return render_template('form.html', form=form)