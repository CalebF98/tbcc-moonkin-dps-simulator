# Caleb's Fork of tbcc-moonkin-dps-simulator
This is a fork of Ceridwyn's TBC Classic Moonkin sim. I am working on improving this simulation. Here's is my current todo list:
- Rework the interface into a comfortable Tkinter GUI environment
- Switch between Wrath & Starfire sims with a simple checkbox button
- Implement mana management into the dps calculations
- Calculate stat-weights as part of the simulation results

For archival purposes, I will leave the original readme intact below:

# tbcc-moonkin-dps-simulator
This repository hosts (mainly) Jupyter notebooks which simulate Moonkin DPS for WoW - The Burning Crusade Classic

At the moment, the notebooks are separated for each gear configuration. At some point, one big notebook checking all cases (including trinkets) may summarize it all.

There are 3 notebooks. 2 to simulate a sizeable amount of fights to estimate an average DPS for the provided stats and specials (Trinkets _TBD_, Chaotic Skyfire Diamond, Spellfire and Spellstrike set bonuses). By default, it's a 90s fight length.
- dps_generator_starfire.ipynb
- dps_generator_wrath.ipynb : 

One to calculate stats coefficients :
- coefficient_calculation.ipynb 

# How to use the DPS generator :
Start the notebook in Jupyter. If you don't know how to run Jupyter, either run it there : https://nbviewer.jupyter.org/ or install Anaconda on your computer and run "jupyter notebook" in your Operating System's command prompt (cmd in windows).

Then, all you have to do to sim your gear is to fill in the stats :
- intel = 356
- crit_score = 336
- hit_score = 141
- spellpower = 835
- haste = 0

NB : Haste is not implemented yet.

And run the two first cells. You will see the DPS calculated. You can increase the number of loops to have a more accurate result.

# Todo-list :
- code each trinket
- include Spell haste
- include mana pool management

