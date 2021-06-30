import numpy
import pandas as pd
import sys
import logging

logging.basicConfig(
	stream=sys.stdout,
	level=logging.DEBUG,
	format='%(asctime)s - %(levelname)s - %(message)s'
)

def compute_dps(int, crit_score, hit_score, sp, haste, 
	is_csd, is_spellstrike, is_spellfire):
		msg = f'Stats provided to sim:\n\tIntellect: {int}\n\tSpell Crit: {crit_score}\n\tSpell Hit: {hit_score}\n\tSpellpower: {sp}\n\tHaste: {haste}\n\tChaotic Skyfire Diamond: {is_csd}\n\tSpellstrike Set: {is_spellstrike}\n\tSpellfire Set: {is_spellfire}'
		logging.debug(msg)
		


if __name__ == '__main__':
	compute_dps(100, 150, 84, 900, 0, True, True, True)