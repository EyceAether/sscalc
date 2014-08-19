__author__ = 'davburge'

import ss_constants
import ss_inputs
import ss_skills

def calculate():
    atBonus = getATBonus()
    for stat in ss_constants.statNames.keys():
        if stat in ss_constants.calculatedStats:
            baseAmount = getBaseAmount(stat)
            if baseAmount != 0:
                augBonus = getAugBonus(stat, atBonus)
                skillBonus = getSkillsBonus(stat)
                itemBonus = 1
                auraBonus = getAuraBonus(stat)
                getOverallBonus(stat, baseAmount, augBonus, skillBonus, itemBonus, auraBonus)
            else:
                setBonusField(stat, "")
                setFinalField(stat, "")

def getBaseAmount(stat):
    try:
        baseAmount = ss_inputs.baseInputs[stat]['initial'].get()
        if baseAmount != '':
            baseAmount = baseAmount.replace(',', '')
            if baseAmount == '.':
                baseAmount = '0'
            baseAmount = float(baseAmount)
        else:
            baseAmount = 0
    except:
        baseAmount = 1
    return baseAmount

def getATBonus():
    at = ss_inputs.augTweakLevel.get()
    it = ss_inputs.impTweakLevel.get()
    if at == "":
        at = '0'
    if it == "":
        it = '0'
    atBonus = (0.04 * int(at)) + (0.02 * int(it))
    if ss_inputs.classSkill.get() == 'engineer':
        ec = ss_inputs.classLevel.get()
        atBonus += (ss_skills.engineer['augTweak'] * int(ec))
    return atBonus + 1

def getAugBonus(stat, atBonus):
    augBonus = 0
    for aug in ss_inputs.augs:
        augStat = aug[stat].get()
        if augStat != '' and augStat != '.' and augStat != '-' and augStat != '+':
            augStat = float(augStat) / 100 # change from percentage
            if augStat > 0: # positive
                augBonus += augStat
            elif augStat < 0: # negative
                augBonus += (augStat / (1 - abs(augStat)))
    augBonus = round(augBonus, 2)
    if augBonus > 0:
        augBonus *= atBonus
        augBonus = augBonus + 1
    elif augBonus < 0:
        augBonus *= atBonus
        augBonus = augBonus / (1 - augBonus)
        augBonus += 1
    else: # If equals 0, then no bonus
        augBonus = 1
    return getAugMods(stat, round(augBonus, 2))

def getAugMods(stat, augBonus):
    shipMod = ss_inputs.shipMods[stat].get()
    if shipMod == "":
        shipMod = '0'
    shipMod = float(shipMod) / 100
    overalAugBonus = augBonus + shipMod
    return overalAugBonus

def getSkillsBonus(stat):
    overallSkillBonus = 1
    if ss_inputs.focusLevel.get() != '':
        focusBonus = getFocusBonus(stat)
        classBonus = getClassBonus(stat)

        subSkill1Bonus = 1
        subSkill2Bonus = 1
        subSkill3Bonus = 1

        # All 1s here
        subSkill_1 = ss_inputs.subSkill_1.get()
        subSkill_1Level = ss_inputs.subskill_1Level.get()
        if subSkill_1Level != '' and subSkill_1Level != '0':
            subSkill1Bonus = getSubSkillBonus(stat, subSkill_1, int(subSkill_1Level))
        # All 2s here
        subSkill_2 = ss_inputs.subSkill_2.get()
        subSkill_2Level = ss_inputs.subskill_2Level.get()
        if subSkill_2Level != '' and subSkill_2Level != '0':
            subSkill2Bonus = getSubSkillBonus(stat, subSkill_2, int(subSkill_2Level))
        # All 3s here
        subSkill_3 = ss_inputs.subSkill_3.get()
        subSkill_3Level = ss_inputs.subskill_3Level.get()
        if subSkill_3Level != '' and subSkill_3Level != '0':
            subSkill3Bonus = getSubSkillBonus(stat, subSkill_3, int(subSkill_3Level))

        overallSkillBonus = focusBonus * classBonus * subSkill1Bonus * subSkill2Bonus * subSkill3Bonus
    return round(overallSkillBonus, 2)


def getFocusBonus(stat):
    focusBonus = 1
    focusLevel = int(ss_inputs.focusLevel.get())
    try: # check if class type in focus skill
        shipClassStats = ss_skills.skill_tree[ss_inputs.focusSkill.get()]['shipClass'][ss_inputs.shipClass.get()]
        try: # check if stat has bonus and apply
            focusBonus += (focusLevel * shipClassStats[stat])
            return focusBonus
        except KeyError: # no bonuses to this stat
            return focusBonus
    except KeyError: # use all class type
        shipClassStats = ss_skills.skill_tree[ss_inputs.focusSkill.get()]['shipClass']['all']
        if shipClassStats is None: # no bonuses to this ship
            return 1
        else:
            try:
                focusBonus += (focusLevel * shipClassStats[stat])
                return focusBonus
            except KeyError: # no bonuses to this stat
                return 1

def getClassBonus(stat):
    classBonus = 1
    classLevel = ss_inputs.classLevel.get()
    if classLevel != '':
        classLevel = int(classLevel)
        try:
            classStat = ss_skills.skill_tree[ss_inputs.focusSkill.get()][ss_inputs.classSkill.get()][stat]
            classBonus += (classLevel * classStat)
        except KeyError:
            pass
        if stat == 'damage':
            try:
                damageType = ss_constants.elementTypes[ss_inputs.damageType.get()] + "Damage"
                classStat = ss_skills.skill_tree[ss_inputs.focusSkill.get()][ss_inputs.classSkill.get()][damageType]
                classBonus += (classLevel * classStat)
            except KeyError:
                pass
        elif stat == 'resist':
            try:
                resistType = ss_constants.elementTypes[ss_inputs.resistType.get()] + "Resist"
                classStat = ss_skills.skill_tree[ss_inputs.focusSkill.get()][ss_inputs.classSkill.get()][resistType]
                classBonus += (classLevel * classStat)
            except KeyError:
                pass
    return classBonus

def getSubSkillBonus(stat, subSkill, subSkillLevel):
    subSkillBonus = 1
    try:
        subSkillStat = ss_skills.skill_tree[ss_inputs.focusSkill.get()][ss_inputs.classSkill.get()][subSkill][stat]
        subSkillBonus += (subSkillLevel * subSkillStat)
    except KeyError:
        pass
    if stat == 'damage':
        try:
            damageType = ss_constants.elementTypes[ss_inputs.damageType.get()] + "Damage"
            subSkillStat = ss_skills.skill_tree[ss_inputs.focusSkill.get()][ss_inputs.classSkill.get()][subSkill][damageType]
            subSkillBonus += (subSkillLevel * subSkillStat)
        except KeyError:
            pass
    elif stat == 'resist':
        try:
            resistType = ss_constants.elementTypes[ss_inputs.resistType.get()] + "Resist"
            subSkillStat = ss_skills.skill_tree[ss_inputs.focusSkill.get()][ss_inputs.classSkill.get()][subSkill][resistType]
            subSkillBonus += (subSkillLevel * subSkillStat)
        except KeyError:
            pass
    return subSkillBonus

def getAuraBonus(stat):
    '''Returns a tuple of (isPercent, amount)'''
    return (True, 0)

def getOverallBonus(stat, baseAmount, augBonus, skillBonus, itemBonus, auraBonus):
    overallBonus = augBonus * skillBonus * itemBonus

    if stat == 'energyCharge':
        baseAmount += getInbuiltElec()

    if auraBonus[0] == True and auraBonus[1] != 0:
        overallBonus *= auraBonus[1]

    if stat == 'resist':
        baseAmount = baseAmount / 100
        if baseAmount > 0:
            baseAmount = 1 - baseAmount
            finalStat = baseAmount / overallBonus
            finalStat = 1 - finalStat
        else:
            finalStat = baseAmount / overallBonus
        overallBonus = "???"
        finalStat *= 100
        finalStat = str(round(finalStat, 2)) + "%"
    elif stat == 'RoF':
        finalStat = baseAmount / overallBonus
        finalStat = str(round(finalStat, 3))
    else:
        finalStat = baseAmount * overallBonus
        finalStat = str(round(finalStat, 3))

    if auraBonus[0] == False:
        finalStat += float(auraBonus)

    setBonusField(stat, overallBonus)
    setFinalField(stat, finalStat)

def getInbuiltElec():
    addElec = ss_inputs.shipMods['inbuiltElec'].get()
    if addElec != '':
        addElec = addElec.replace(',', '')
        addElec = float(addElec)
        addElec *= 1.2
        return addElec
    else:
        return 0

def setBonusField(stat, bonus):
    ss_inputs.baseInputs[stat]['bonus'].set(str(bonus))

def setFinalField(stat, final):
    ss_inputs.baseInputs[stat]['overall'].set(final)