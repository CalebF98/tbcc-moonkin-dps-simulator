from simulation import compute_avg_dps
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	result = compute_avg_dps(1000, 100, 150, 84, 900, 0, True, True, True)
	return f'Simulated 1000 fights, average dps: {result}'
