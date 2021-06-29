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
		logging.debug(f'Stats provided to sim:\nIntellect: {int}\nSpell Crit: {crit_score}\nSpell Hit: {hit_score}\nSpellpower: {sp}\nHaste: {haste}\nChaotic Skyfire Diamond: {is_csd}\nSpellstrike Set: {is_spellstrike}\nSpellfire Set: {is_spellfire}')


if __name__ == '__main__':
	compute_dps(100, 150, 84, 900, 0, True, True, True)