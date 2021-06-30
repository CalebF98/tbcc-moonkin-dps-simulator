import numpy
import pandas as pd
import sys
import logging

logging.basicConfig(
	stream=sys.stdout,
	level=logging.INFO,
	format='%(asctime)s - %(levelname)s - %(message)s'
)

def compute_avg_dps(num_fights, intellect, crit_score, hit_score, spellpower, haste, is_csd, is_spellstrike, is_spellfire):
    msg = f'Stats provided to sim:\n\tIntellect: {intellect}\n\tSpell Crit: {crit_score}\n\tSpell Hit: {hit_score}\n\tSpellpower: {spellpower}\n\tHaste: {haste}\n\tChaotic Skyfire Diamond: {is_csd}\n\tSpellstrike Set: {is_spellstrike}\n\tSpellfire Set: {is_spellfire}'
    logging.info(msg)
    balance_of_power = 4 # +4% Hit
    focused_starlight = 4 # +4% crit for SF and Wrath
    moonkin_form = 5 # +5% Crit
    improved_mf = 10 # +10% Moonfire crit 
    starlight_wrath = True # reduce cast time by 0.5s
    vengeance = True # +100% Crit damange
    lunar_guidance = True # Spellpower bonus = 24% of total intellect
    moonfury = 1.1 # +10% damage
    wrath_of_cenarius = 1.2 # +20% Spellpower for SF | +10% SpellPower for Wrath
    fight_length = 90 # in seconds

    # Sets bonuses
    spellfire = is_spellfire # SP bonus = +7% of total intellectlect
    spellstrike = is_spellstrike # 5% chance to have +92sp for 10s - No ICD
    windhawk = False # 8MP/5 KEK

    # Meta GEM - Chaotic Skyfire Diamond
    csd_equiped = is_csd

    # Special Trinkets
    eye_of_mag = False # Grants 170 increased spell damage for 10 sec when one of your spells is resisted.
    silver_crescent = False # Use: Increases damage and healing done by magical spells and effects by up to 155 for 20 sec. (2 Min Cooldown)
    scryer_gem = False # Use: Increases spell damage by up to 150 and healing by up to 280 for 15 sec. (1 Min, 30 Sec Cooldown)
    quagmirran = False # Equip: Your harmful spells have a chance to increase your spell haste rating by 320 for 6 secs. (Proc chance: 10%, 45s cooldown)
    essence_sapphi = False #  Use: Increases damage and healing done by magical spells and effects by up to 130 for 20 sec. (2 Min Cooldown)
    
    # Translating stats to %
    # At level 70, 22.1 Spell Critical Strike Rating increases your chance to land a Critical Strike with a Spell by 1%
    # At level 70, 12.6 Spell Hit Rating increases your chance to Hit with Spells by 1%. Hit cap is 202 FLAT (not including talents & buffs).
    # Druids receive 1% Spell Critical Strike chance for every 79.4 points of intellectlect.

    # Moonfire base damage : 305 to 357 Arcane damage and then an additional 600 Arcane damage over 12 sec.
    MF_coeff = 0.15
    MF_coeff_dot = 0.52
    # Starfire base damage : 605 to 711 Arcane damage -> 658 on average
    SF_coeff = 1
    SF_average_damage = 658
    MF_average_damage = 331
    MF_average_dot_damage = 600
    partial_coeff = 0.5 # For the moment, let's say that in average, partials get 50% damage reduction
    sf_cast_time = 3
    sf_cast_time_ng = 2.5

    # Improved CotE
    curse_of_the_elements = 1.13
    
    # Apply spell haste coefficients here
    # 15.77 Spell Haste Rating increases casting speed by 1%
    # % Spell Haste at level 70 = (Haste Rating / 15.77)
    # New Casting Time = Base Casting Time / (1 + (% Spell Haste / 100))
    spell_haste = haste / 15.77
    sf_cast_time = 3 / (1 + (spell_haste/100))
    sf_cast_time_ng = 2.5 / (1 + (spell_haste/100))
    # print("SF Cast time : " + str(sf_cast_time))
    # print("SF NG Cast time : " + str(sf_cast_time_ng))

    # Spell power calculation for fight SP + lunar guidance 
    if lunar_guidance:
        spellpower = spellpower + 0.24 * intellect
    if spellfire:
        spellpower = spellpower + 0.08 * intellect
    
    # Hit chance
    # 12.6 Spell Hit Rating -> 1%
    hit_chance = min(99, 83 + (hit_score/12.6) + balance_of_power )
    logging.debug(f'Hit chance is : {hit_chance}')

    # Crit chance
    # At level 70, 22.1 Spell Critical Strike Rating -> 1%
    # Druids receive 1% Spell Critical Strike chance for every 79.4 points of intellectlect.
    MF_crit_percent = crit_score/22.1 + intellect/79.4 + improved_mf + moonkin_form + focused_starlight 
    SF_crit_percent =  crit_score/22.1 + intellect/79.4 +  + moonkin_form + focused_starlight 

    logging.debug(f'Moonfire crit chance is : {MF_crit_percent}')
    logging.debug(f'Starfire crit chance is : {SF_crit_percent}')
    logging.debug(f'Spellpower is  : {spellpower}')
    
    # Crit coeff
    if csd_equiped:
        crit_coeff = 2.09
    else:
        crit_coeff = 2
    
    # Spellstrike bonus:
    if spellstrike:
        spellstrike_bonus = 92
    else:
        spellstrike_bonus = 0
    
    # Prepare and launch the simulations
    loop_size = num_fights # number of fights simulated
    logging.info(f'Calculating average dps of {loop_size} fights, hang tight...')
    average_dps = 0
    n = 0
    while n < loop_size:
        n = n +1
        logging.info(f'Simulating fight #{n}...')
        # Initialization
        total_damage_done = 0
        damage = 0
        fight_time = 0
        spellstrike_uptime = 0
        ff_uptime = 0
        mf_uptime = 0
        is_ff_up = False
        is_mf_up = False
        is_ng = False
        spellstrike_proc = False
        ng_proc = False
        # Time to kick ass and chew bubble gum
        while fight_time <= fight_length:
            loop_duration = 1 #GCD - can't be less, it's the rule !
            damage = 0
            if spellstrike_proc:
                fight_spell_power = spellpower + spellstrike_bonus
            else:
                fight_spell_power = spellpower
           
            # if FF not up, cast FF
            if not is_ff_up:
                logging.debug('Casting Faerie Fire !')
                is_crit = False # can't crit on FF
                damage = 0 # and no damage applied
                if(numpy.random.randint(1, high = 101, size = 1) <= hit_chance):
                    is_hit = True
                    ff_uptime = 40
                    is_ff_up = True
                    # Test if spellstrike is proc
                    spellstrike_proc = (numpy.random.randint(1, high = 101, size = 1) <= 10)
                else:
                    is_hit = False
                    logging.debug('Faerie Fire -> Resist !')
                loop_duration = 1 #GCD
            # if Moonfire not up, cast Moonfire
            else:
                if not is_mf_up:
                    logging.debug('Casting Moonfire !')
                    loop_duration = 1 #GCD because we cast a spell
                    # Is it a hit ?
                    if(numpy.random.randint(1, high = 101, size = 1) <= hit_chance):
                        is_hit = True
                        # Is it a crit ?
                        is_crit = (numpy.random.randint(1, high = 101, size = 1) <= MF_crit_percent)
                        # Is it a partial ?
                        if(numpy.random.randint(1, high = 101, size = 1) <= hit_chance):
                            damage = MF_average_damage + MF_coeff * fight_spell_power * partial_coeff
                        else:
                            damage = MF_average_damage + MF_coeff * fight_spell_power
                        # Apply damage
                        if is_crit:
                            damage = damage * crit_coeff
                        # DoT :
                        damage = damage + MF_average_dot_damage + (MF_coeff_dot * fight_spell_power * min(12, (fight_length - fight_time - 1))/12)
                        # There is a Hit ! update model
                        is_mf_up = True
                        mf_uptime = 12
                    else:
                        is_hit = False
                        logging.debug('Moonfire -> Resist ! ')
                else:
                    # Cast Starfire
                    logging.debug('Casting Starfire !')
                    # Is it a hit ?
                    if(numpy.random.randint(1, high = 101, size = 1) <= hit_chance):
                        is_hit = True
                        # Is it a crit ?
                        is_crit = (numpy.random.randint(1, high = 101, size = 1) <= SF_crit_percent)
                        # Is it a partial ?
                        if(numpy.random.randint(1, high = 101, size = 1) > hit_chance):
                            logging.debug('Partial hit !')
                            damage = (SF_average_damage + (SF_coeff * fight_spell_power * wrath_of_cenarius * partial_coeff )) * moonfury
                            # logging.info("Damage done : " + str(damage))
                        else:
                            damage = (SF_average_damage + (SF_coeff * fight_spell_power * wrath_of_cenarius )) * moonfury
                            logging.debug(f'Damage done : {damage}')
                        if is_crit:
                            damage = damage * crit_coeff
                    else:
                        is_hit = False
                        logging.debug('Starfire -> Resist ! ')
                    if is_ng:
                        loop_duration = sf_cast_time_ng
                    else:
                        loop_duration = sf_cast_time
                    is_ng = False # Consume NG once SF is cast

                # if there's a hit, we check Spellstrike proc

                # Update time and model
                fight_time = fight_time + loop_duration
                ff_uptime = ff_uptime - loop_duration
                mf_uptime = mf_uptime - loop_duration
                # Check the timer on buffs / debuffs
                spellstrike_uptime = spellstrike_uptime - loop_duration
                if spellstrike_uptime <= 0:
                    spellstrike_proc = False

                if mf_uptime <= 0:
                    is_mf_up = False
                if ff_uptime <= 0:
                    is_ff_up = False
                # @TODO if trinket available, activate   
                # Update nature's grace
                if is_crit:
                    is_ng = True
                total_damage_done = total_damage_done + damage * curse_of_the_elements

                # If there is a Hit, Check if spellstrike is proc or refreshed :
                if is_hit: 
                    if numpy.random.randint(1, high = 11, size = 1) == 10:
                        spellstrike_proc = True
                        spellstrike_uptime = 10
                        logging.debug('Spellstrike proc !!!')

                # Print output
                logging.debug(f'Loop Duration: {loop_duration}')
                logging.debug(f'Loop Damage: {damage}')

        dps = total_damage_done / fight_time # We use fight_time here in case SF lands after the fight_length mark
        logging.debug(f'Damage done for fight #{n}: {total_damage_done:.2f} ({dps:.2f})')
        average_dps = average_dps + (total_damage_done/fight_time)

    average_dps = average_dps / loop_size # We have an sum of dps for every fight, now to divide by # of fights
    logging.info(f'Average DPS: {average_dps}')

    return average_dps


if __name__ == '__main__':
    result = compute_avg_dps(1000, 100, 150, 84, 900, 0, True, True, True)
    print(result)