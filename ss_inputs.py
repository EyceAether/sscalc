__author__ = 'davburge'

import collections
import Tkinter as tk

shipClass = None
shipMods = None
damageType = None
resistType = None

focusSkill = None
focusLevel = None

classSkill = None
classLevel = None

subSkill_1 = None
subSkill_2 = None
subSkill_3 = None
subskill_1Level = None
subskill_2Level = None
subskill_3Level = None

augTweakLevel = None
impTweakLevel = None

shieldBank = None
shieldCharge = None
energyBank = None
energyCharge = None
hull = None
speed = None
damage = None
RoF = None
range = None
vis = None

baseInputs = None

augNumber = None

augs = None


def setup():
    global shipClass
    shipClass = tk.StringVar()

    global shipMods
    shipMods = collections.OrderedDict([
        ('shieldBank', tk.StringVar()),
        ('shieldCharge', tk.StringVar()),
        ('energyBank', tk.StringVar()),
        ('energyCharge', tk.StringVar()),
        ('hull', tk.StringVar()),
        ('speed', tk.StringVar()),
        ('damage', tk.StringVar()),
        ('RoF', tk.StringVar()),
        ('range', tk.StringVar()),
        ('vis', tk.StringVar()),
        ('resist', tk.StringVar()),
        ('elecTemp', tk.StringVar()),
        ('inbuiltElec', tk.StringVar()),
    ])

    global damageType
    damageType = tk.StringVar()

    global resistType
    resistType = tk.StringVar()

    global focusSkill
    focusSkill = tk.StringVar()

    global focusLevel
    focusLevel = tk.StringVar()

    global classSkill
    classSkill = tk.StringVar()

    global classLevel
    classLevel = tk.StringVar()

    global subSkill_1
    subSkill_1 = tk.StringVar()
    global subSkill_2
    subSkill_2 = tk.StringVar()
    global subSkill_3
    subSkill_3 = tk.StringVar()

    global subskill_1Level
    subskill_1Level = tk.StringVar()
    global subskill_2Level
    subskill_2Level = tk.StringVar()
    global subskill_3Level
    subskill_3Level = tk.StringVar()

    global augTweakLevel
    augTweakLevel = tk.StringVar()
    global impTweakLevel
    impTweakLevel = tk.StringVar()

    shieldBank = {
        'initial': tk.StringVar(),
        'bonus': tk.StringVar(),
        'overall': tk.StringVar(),
    }
    shieldCharge = {
        'initial': tk.StringVar(),
        'bonus': tk.StringVar(),
        'overall': tk.StringVar(),
    }
    energyBank = {
        'initial': tk.StringVar(),
        'bonus': tk.StringVar(),
        'overall': tk.StringVar(),
    }
    energyCharge = {
        'initial': tk.StringVar(),
        'bonus': tk.StringVar(),
        'overall': tk.StringVar(),
    }
    hull = {
        'initial': tk.StringVar(),
        'bonus': tk.StringVar(),
        'overall': tk.StringVar(),
    }
    speed = {
        'initial': tk.StringVar(),
        'bonus': tk.StringVar(),
        'overall': tk.StringVar(),
    }
    damage = {
        'initial': tk.StringVar(),
        'bonus': tk.StringVar(),
        'overall': tk.StringVar(),
    }
    RoF = {
        'initial': tk.StringVar(),
        'bonus': tk.StringVar(),
        'overall': tk.StringVar(),
    }
    range = {
        'initial': tk.StringVar(),
        'bonus': tk.StringVar(),
        'overall': tk.StringVar(),
    }
    vis = {
        'initial': tk.StringVar(),
        'bonus': tk.StringVar(),
        'overall': tk.StringVar(),
    }
    resist = {
        'initial': tk.StringVar(),
        'bonus': tk.StringVar(),
        'overall': tk.StringVar(),
    }
    elecTemp = {
        'initial': tk.StringVar(),
        'bonus': tk.StringVar(),
        'overall': tk.StringVar(),
    }

    global baseInputs
    baseInputs = collections.OrderedDict([
        ('shieldBank', shieldBank),
        ('shieldCharge', shieldCharge),
        ('energyBank', energyBank),
        ('energyCharge', energyCharge),
        ('hull', hull),
        ('speed', speed),
        ('damage', damage),
        ('RoF', RoF),
        ('range', range),
        ('vis', vis),
        ('resist', resist),
        ('elecTemp', elecTemp),
    ])

    global augNumber
    augNumber = tk.StringVar()

    global augs
    augs = []

    setDefaults()


def setDefaults():
    global shipClass
    shipClass.set('lfi')
    global damageType
    damageType.set('Energy')
    global resistType
    resistType.set('Energy')
    global focusSkill
    focusSkill.set('combat_focus')
    global classSkill
    classSkill.set('berserker')
    global subSkill_1
    subSkill_1.set('0')
    global subSkill_2
    subSkill_2.set('0')
    global subSkill_3
    subSkill_3.set('0')
    global augTweakLevel
    augTweakLevel.set('0')
    global impTweakLevel
    impTweakLevel.set('0')
    global augNumber
    augNumber.set('0')

class augmenter(collections.OrderedDict):
    def __init__(self):
        collections.OrderedDict.__init__(self)
        self.update([
            ('name', tk.StringVar()),
            ('shieldBank', tk.StringVar()),
            ('shieldCharge', tk.StringVar()),
            ('energyBank', tk.StringVar()),
            ('energyCharge', tk.StringVar()),
            ('hull', tk.StringVar()),
            ('speed', tk.StringVar()),
            ('damage', tk.StringVar()),
            ('RoF', tk.StringVar()),
            ('range', tk.StringVar()),
            ('vis', tk.StringVar()),
            ('resist', tk.StringVar()),
            ('elecTemp', tk.StringVar()),
        ])