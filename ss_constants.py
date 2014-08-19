__author__ = 'davburge'

import collections

ships = {
    'lfi': "Light Fighter",
    'hfi': "Heavy Fighter",
    'sfr': "Support Freighter",
    'ifr': "Industrial Freighter",
    'cap': "Capital Ship",
    'all': "All",
}

skill_tree = {
    'combat_focus': {
        'name': "Combat Focus",
        'berserker': {
            'name': "Berserker",
            'impervious_armor': "Impervious Armor",
            'ordinance_supremacy': "Ordinance Supremacy",
            'arsenal_expertise': "Arsenal Expertise"
        },
        'sniper': {
            'name': "Sniper",
            'stalking': "Stalking",
            'sharpshooting': "Sharpshooting",
            'efficiency': "Efficiency"
        }
    },
    'recon_focus': {
        'name': "Recon Focus",
        'speed_demon': {
            'name': "Speed Demon",
            'speedy_movement': "Speedy Movement",
            'speedy_firing': "Speedy Firing",
            'dogfighting': "Dogfighting",
        },
        'seer': {
            'name': "Seer",
            'psionic_shrouding': "Psionic Shrouding",
            'psychic_sight': "Psychic Sight",
            'shadow_ambush': "Shadow Ambush",
        }
    },
    'support_focus': {
        'name': "Support Focus",
        'shield_monkey': {
            'name': "Shield Monkey",
            'shield_boosting': "Shield Boosting",
            'shield_manipulation': "Shield Manipulation",
            'shield_transference': "Shield Transference",
        },
        'engineer': {
            'name': "Engineer",
            'drone_mastery': "Drone Mastery",
            'beam_mastery': "Beam Mastery",
            'damage_control': "Damage Control",
        }
    },
    'fleet_focus': {
        'name': "Fleet Focus",
        'fleet_commander': {
            'name': "Fleet Commander",
            'slave_mastery': "Slave Mastery",
            'radiation_expert': "Radiation Expert",
            'flight_controller': "Flight Controller"
        },
        'gunner': {
            'name': "Gunner",
            'big_guns': "Big Guns",
            'destruction': "Destruction",
            'missile_mastery': "Missile Mastery",
        }
    },
}

calculatedStats = [
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
    'elecTemp',
    'resist',
]

statNames = {
    'name': "Name:",
    'shieldBank': "Shield:",
    'shieldCharge': "Shield Charge:",
    'energyBank': "Energy:",
    'energyCharge': "Energy Charge:",
    'hull': "Hull:",
    'speed': "Speed:",
    'damage': "Damage:",
    'RoF': "Rate of Fire:",
    'range': "Range:",
    'vis': "Vis:",
    'elecTemp': "Elec Tempering:",
    'resist': "Resistance:",
    'inbuiltElec': "Inbuilt Elec:",
    'damageType': "Damage Type:",
    'resistType': "Resist Type:",
}

#This dictionary is reversed item: key order due to the way the menus work for choosing resists/damage types
elementTypes = collections.OrderedDict([
    ("Energy", 'energy'),
    ("Laser", 'laser'),
    ("Heat", 'heat'),
    ("Physical", 'phys'),
    ("Radiation", 'rad'),
    ("Surgical", 'surg'),
    ("Mining", 'mine'),
    ("Transference", 'trans'),
])

shipHelp = "This includes hull inbuilt bonus (As listed on the ship tab when buying a ship) as well as " \
               "any inbuilt bonuses in items (OL and Diffusers too) that do not have the star label (*). " \
               "Add all of the same stat bonuses together.\n\ne.g. if you have a cloak with +5% speed and a " \
               "shield with +35% speed, enter in +40%.\n\nFor negative bonuses, make sure to do " \
               "Bonus/(1+Bonus) before adding to other bonuses. Sorry for the inconvenience."