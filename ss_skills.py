__author__ = 'davburge'

#Stealth?
#Crits
#Recoil?
#Firing Energy?
#Shadow Ambush (Seer)

stats = [
    'shieldBank',
    'shieldCharge',
    'energyBank',
    'energyCharge',
    'hull',
    'speed',
    'damage',
    'RoF',
    'range',
    'vis',
    'multifire',
    'docking',
    'firingEnergy',
    'hostility',
    'resist',
    'physDamage',
    'ethDamage',
]

unused_stats = [
    'tracking',
    'weaponHold',
    'projVelocity',
    'equipSize',
    'critChance',
    'critResist',
    'critDamage',
    'radar',
    'thrust',
    'agility',
    'stealth',
    'docking',
    'defDroneOps',
    'offDroneOps',
    'lastDroneOps',
]

resists = [
    'energy',
    'laser',
    'heat',
    'phys',
    'rad',
    'surj',
    'mine',
    'trans',
    'all',
]

# Berserker Skills

impervious_armor = {
    'resist':0.05,
    'speed':-0.02
}
ordinance_supremacy = {
    'energyBank':0.04,
    'damage':0.01
}
arsenal_expertise = {
    'multifire':0.05,
    'weaponHold':0.025,
    'damage':0.01
}

# Sniper Skills

stalking = {
    'tracking':0.06,
    'stealth':0.03,
    'damage':0.02
}
sharpshooting = {
    'range':0.06,
    'damage':0.01,
    'critChange':0.01,
    'projVeloc':0.05,
    'recoil':0.05
}
efficiency = {
    'damage':0.05,
    'recoil':0.025
}

# Speed Demon Skills

speedy_movement = {
    'speed':0.02,
    'thrust':0.03
}
speedy_firing = {
    'RoF':0.03,
    'damage':0.02,
    'critChance':0.01
}
dogfighting = {
    'damage':0.02,
    'tracking':0.02,
    'turning':0.02,
    'range':-0.02
}

# Seer Skills

psionic_shrouding = {
    'stealth':0.05,
    'critResist':0.05,
}
psychic_sight = {
    'radar':0.1,
    'critDamage':0.05,
    'damage':0.02,
}
shadow_ambush = {
    'critChance':0.01, # May be 0.03. There is a +2% crit Chance when unseen by target on top of this
    'damage':0.02,
}

# Shield Monkey Skills

shield_boosting = {
    'shieldBank':0.025,
    'shieldCharge':0.025,
}
shield_manipulation = {
    'damage':0.015,
    'shieldCharge':0.01,
    'slaves': {
        'damage':0.03,
    }
}
shield_transference = {
    'transDamage':0.065,
    'transResist':0.04,
}

# Engineer Skills

drone_mastery = {
    'defDroneOps':0.01,
    'offDroneOps':0.01,
    'lastDroneOps':0.01,
}
beam_mastery = {
    'beamPower':0.05,
    'beamRange':0.05,
}
damage_control = {
    'resist':0.02,
    'critResist':0.02,
}

# Fleet Commander Skills

slave_mastery = {
    'slaves': {
        'shieldBank':0.0015,
        'energyBank':0.0015,
        'speed':0.0015,
        'turning':0.0015,
        'damage':0.0015,
        'shieldCharge':0.0015,
        'energyCharge':0.0015,
        'thrust':0.0015,
        'vis':0.0015,
        'hull':0.0015,
        'weight':0.0015,
        'tracking':0.0015,
        'radar':0.0015,
        'range':0.0015,
    }
}
radiation_expert = {
    'radDamage':0.1,
    'wildSlaves':0.03,
}
flight_controller = {
    'fighters':0.02,
    'numFighters':0.05,
}

# Gunner Skills

big_guns = {
    #TODO: FIX THIS SHIT
    #So this skill is only cap ships
    #Wiki states: +3% Damage, +1% Mining for only cap ships
    #And +2% for other ship classes
    'damage':0.03,
    'mineDamage':0.01,
    'otherDamage':0.02,
}
destruction = {
    #TODO: FIX THIS SHIT
    #Wtf does this skill even mean?
}
missile_mastery = {
    'missileDamage':0.025,
}

#TODO: Finish Adv. Subskills

# General Subskills

shake_it_off = 0
strategic_deployment = 0
centered = 0
slave_PhD = 0
resilient = 0
droney = 0

# Focus Subskills

big_banker = 0
expansionist = 0
really_super = 0
extra_tweaked = 0

# Berserker Subskill

berserker_classic = 0
weapons_master = 0
berserking_berseker = 0
eye_for_an_eye = 0

# Sniper Subskill

long_scope = 0
quick_scope = 0
grooved_bore = 0
marksman = 0

# Speed Demon Subskill

master_scout = 0
acrobat = 0
fighter_ace = 0
lucky_devil = 0

# Seer Subskill

wraith = 0
clairvoyant = 0
assassin = 0
brooding_gaze = 0

# Shield Monkey Subskill

funky_monkey = 0
flying_monkey = 0
tanky_monkey = 0
enveloping_monkey = 0

# Engineer Subskill

mechanical_engineer = 0
computer_engineer = 0
electrical_engineer = 0
civil_engineer = 0
# I'm one of those ^

# Fleet Commander Subskill

fleet_protector = 0
fleet_admiral = 0
wild_man = 0
advanced_flight_controller = 0

# Gunner Subskill

advanced_targeting_computers = 0
automated_reloading = 0
mass_destruction = 0
gunboat_diplomat = 0

# Combat Focus

berserker = {
    'multifire':None,
    'hostility':0.02,
    'damage':0.03,
    'equipSize':-0.01,
    'impervious_armor': impervious_armor,
    'ordinance_supremacy': ordinance_supremacy,
    'arsenal_expertise': arsenal_expertise,
}

sniper = {
    'damage':0.04,
    'elecTemp':0.025,
    'physDamage':0.05,
    'stalking': stalking,
    'sharpshooting': sharpshooting,
    'efficiency': efficiency,
}

# Recon Focus

speed_demon = {
    'speed':0.02,
    'RoF':0.03,
    'docking':0.1,
    'elecTemp':-0.01,
    'speedy_movement': speedy_movement,
    'speedy_firing': speedy_firing,
    'dogfighting': dogfighting,
}

seer = {
    'damage':0.02,
    'ethDamage':0.01,
    'radar':0.03,
    'stealth':0.02,
    'psionic_shrouding': psionic_shrouding,
    'psychic_sight': psychic_sight,
    'shadow_ambush': shadow_ambush,
}

# Support Focus

shield_monkey = {
    'shieldBank':0.05,
    'shieldCharge':0.03,
    'shield_boosting': shield_boosting,
    'shield_manipulation': shield_manipulation,
    'shield_transference': shield_transference,
}

engineer = {
    'shieldBank':0.005,
    'energyBank':0.005,
    'speed':0.005,
    'turning':0.005,
    'damage':0.005,
    'shieldCharge':0.005,
    'energyCharge':0.005,
    'thrust':0.005,
    'tracking':0.005,
    'docking':0.005,
    'RoF':0.005,
    'radar':0.005,
    'range':0.005,
    'elecTemp':-0.005,
    'firingEnergy':-0.005,
    'augTweak':0.005,
    'drone_mastery': drone_mastery,
    'beam_mastery': beam_mastery,
    'damage_control': damage_control,
}

# Fleet Focus

fleet_commander = {
    'auraPower':0.04,
    'slave_mastery': slave_mastery,
    'radiation_expert': radiation_expert,
    'flight_controller': flight_controller,
}

gunner = {
    'multifire':None,
    'weaponHold':0.05,
    'damage':0.02,
    'big_guns': big_guns,
    'destruction': destruction,
    'missile_mastery': missile_mastery,
}

# Focus Skills

combat_focus = {
    'shipClass': {
        'hfi': {
            'shieldBank':0.03,
            'damage':0.01
        },
        'all': {
            'shieldBank':0.01,
            'equipSize':-0.02,
        }
    },
    'berserker': berserker,
    'sniper': sniper
}
recon_focus = {
    'shipClass': {
        'lfi': {
            'agility':0.1,
            'thrust':0.1,
            'radar':0.05,
            'hull':0.015,
        },
        'all': {
            'agility':0.05,
            'thrust':0.05,
        }
    },
    'speed_demon': speed_demon,
    'seer': seer
}
support_focus = {
    'shipClass': {
        'sfr': {
            'hull':0.09,
            'weight':-0.02,
        },
        'ifr': {
            'hull':0.09,
            'weight':-0.02,
        },
        'hfi': {
            'hull':0.04
        },
        'cap': {
            'hull':0.04
        },
        'all': None
    },
    'shield_monkey': shield_monkey,
    'engineer': engineer
}
fleet_focus = {
    'shipClass': {
        'cap': {
            'non-offensive-stats':0.02,
            'hull':0.08
        },
        'hfi': {
            'basic-stats':0.01,
            'hull':0.04
        },
        'sfr': {
            'basic-stats':0.01,
            'hull':0.04
        },
        'ifr': {
            'basic-stats':0.01,
            'hull':0.04
        },
        'all': None
    },
    'fleet_commander': fleet_commander,
    'gunner': gunner
}

# Skill Tree

skill_tree = {
    'combat_focus': combat_focus,
    'recon_focus': recon_focus,
    'support_focus': support_focus,
    'fleet_focus': fleet_focus,
}