from simulation import compute_avg_dps
from flask import Flask, request
app = Flask(__name__, static_folder='public')

@app.get('/')
def index():
	#result = compute_avg_dps(1000, 100, 150, 84, 900, 0, True, True, True)
	#return f'Simulated 1000 fights, average dps: {result}'
	return app.send_static_file('form.html')

@app.post('/')
def simulate():
	return request.form