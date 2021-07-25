import sys
import logging

logging.basicConfig(
	stream=sys.stdout,
	level=logging.DEBUG,
	format='%(asctime)s - %(levelname)s - %(message)s'
)

class Simulation:
	def __init__(self, length=90, int=100, crit=50, hit=50, sp=500, haste=0):
		self.params = {
			'fight_length': length,
			'intellect': int,
			'crit_rating': crit,
			'hit_rating': hit,
			'spellpower': sp,
			'haste_rating': haste
		}

	def get_params(self):
		for stat in self.params:
			yield (stat, self.params[stat])
	
	def get_avg_dps(self, num_fights):
		sum = 0
		for i in range(num_fights):
			sum += self._simulate_fight()
		return sum / num_fights
			
	def _simulate_fight(self):
		debug_msg = 'Simulating new fight\nSimulation Parameters:'
		for stat, val in self.get_params():
			debug_msg += f'\n\t{stat}: {val}'
		logging.debug(debug_msg)
		dps = 10
		return dps
	

if __name__ == '__main__':
	testSim = Simulation(200,165,164,900,20)
	x = testSim.get_avg_dps(1000)
	logging.info(f'Average dps of 1000 fights: {x}')
