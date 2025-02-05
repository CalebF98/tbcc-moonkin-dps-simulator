import os
from dotenv import load_dotenv
from app.simulation import compute_avg_dps
from flask import Flask, request, render_template
from app.form import SimParamsForm

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

@app.route('/', methods=['GET','POST'])
def index():
	form = SimParamsForm()
	if request.method == 'POST' and form.validate():
		sim_params = {
			'is_csd': False,
			'is_spellstrike': True,
			'is_spellfire': True
		}

		filtered = filter(lambda x: x.name != 'csrf_token', form)
		for stat in filtered:
			sim_params[stat.name] = stat.data


		dps = compute_avg_dps(**sim_params)
		return render_template('form.html', form=form, results=dps, num_fights=sim_params['num_fights'])

	return render_template('form.html', form=form)