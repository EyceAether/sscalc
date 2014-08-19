__author__ = 'davburge'

import ss_constants
import ss_inputs
import ss_math
import ss_validators

import Tkinter as tk
from Tkconstants import *

class Application(tk.Frame):
    def __init__(self, master=None):
        '''Main frame of the application'''
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # Ensures that tk variables are setup before use
        ss_inputs.setup()
        # These two Widgets get deleted and reformed, start as None to prevent errors
        self.classWidget = None
        self.subskillWidget = None

        self.createWidgets()

    def createWidgets(self):
        '''Builds gui widgets'''
        self.buildShipClass()

        self.buildSkillDisplay()

        self.buildStatDisplay()

        self.buildAugDisplay()

        self.buildModDisplay()

        self.buildCalcButton()
        self.buildQuitButton()

    def buildShipClass(self):
        '''Builds the ship class radiobuttons and edit ship button'''
        shipClassLabel = tk.LabelFrame(self.master, text='Ship Type')
        shipClassLabel.grid(column=0, row=0, rowspan=2, sticky=N+S, padx=2)
        for key, value in ss_constants.ships.items():
            if key != 'all':
                radiobutton = tk.Radiobutton(shipClassLabel, text=value, variable=ss_inputs.shipClass, value=key)
                if key == 'lfi':
                    i=0
                elif key == 'hfi':
                    i=1
                elif key == 'sfr':
                    i=2
                elif key == 'ifr':
                    i=3
                elif key == 'cap':
                    i=4
                else:
                    i=-1
                radiobutton.grid(column=0, row=i, sticky=W)
        shipEditButton = tk.Button(shipClassLabel, text="Edit Ship Mods", command=self.buildShipEditDisplay)
        shipEditButton.grid(column=0, row=5)

    def buildShipEditDisplay(self):
        '''Builds edit ship popup'''
        if hasattr(self, 'shipEditWindow') and self.shipEditWindow is not None:
            self.shipEditWindow.deiconify()
        else:
            self.shipEditWindow = tk.Toplevel(self)
            self.shipEditWindow.resizable(0,0)
            self.shipEditWindow.title("Ship")
            self.shipEditWindow.protocol("WM_DELETE_WINDOW", self.shipEditWindow.withdraw)

            inbuiltStatsLabel = tk.LabelFrame(self.shipEditWindow, text="Ship Inbuilt Stats")
            inbuiltStatsLabel.grid(column=0, row=0, columnspan=2, padx=1, sticky=W+E)

            vcmd_all = (self.shipEditWindow.register(ss_validators.bonusStatValidate),
                        '%d', '%i', '%P', '%s', '%S')
            i=0
            for key, value in ss_inputs.shipMods.items():
                # Uses a percent sign for all built inbuilt elec charge
                if key == 'inbuiltElec':
                    symbol = '/sec'
                    vcmd = (self.shipEditWindow.register(ss_validators.shipStatValidate),
                            '%d', '%i', '%P', '%s', '%S')
                else:
                    symbol = '%'
                    vcmd = vcmd_all
                statLabel = tk.Label(inbuiltStatsLabel, text=ss_constants.statNames[key], padx=3)
                statLabel.grid(column=0, row=i, sticky=E)
                statEntry = tk.Entry(inbuiltStatsLabel, width=6, justify=RIGHT, textvariable=value,
                                     validate='key', validatecommand=vcmd)
                statEntry.grid(column=1, row=i)
                percentLabel = tk.Label(inbuiltStatsLabel, text=symbol, padx=3)
                percentLabel.grid(column=2, row=i)
                i+=1
            damageLabel = tk.Label(inbuiltStatsLabel, text=ss_constants.statNames['damageType'], padx=3)
            damageLabel.grid(column=0, row=i, sticky=E)
            damageMenubutton = tk.Menubutton(inbuiltStatsLabel, textvariable=ss_inputs.damageType, relief=RAISED)
            damageMenubutton.grid(column=1, columnspan=2, row=i)
            damageMenubutton.menu = tk.Menu(damageMenubutton, tearoff=0)
            damageMenubutton['menu'] = damageMenubutton.menu
            for key, value in ss_constants.elementTypes.items():
                damageMenubutton.menu.add_radiobutton(label=key, variable=ss_inputs.damageType)
            i+=1
            resistLabel = tk.Label(inbuiltStatsLabel, text=ss_constants.statNames['resistType'], padx=3)
            resistLabel.grid(column=0, row=i, sticky=E)
            resistMenubutton = tk.Menubutton(inbuiltStatsLabel, textvariable=ss_inputs.resistType, relief=RAISED)
            resistMenubutton.grid(column=1, columnspan=2, row=i)
            resistMenubutton.menu = tk.Menu(resistMenubutton, tearoff=0)
            resistMenubutton['menu'] = resistMenubutton.menu
            for key, item in ss_constants.elementTypes.items():
                resistMenubutton.menu.add_radiobutton(label=key, variable=ss_inputs.resistType)
            i+=1
            helpButton = tk.Button(self.shipEditWindow, text="Help", command=self.shipHelp)
            helpButton.grid(column=0, row=i)
            updateButton = tk.Button(self.shipEditWindow, text="Update and Close", command=self.shipEditWindow.withdraw)
            updateButton.grid(column=1, row=i, pady=2)

    def shipHelp(self):
        '''Builds help popup for ship edit popup'''
        if hasattr(self, 'helpWindow') and self.helpWindow is not None:
            self.helpWindow.deiconify()
        else:
            self.helpWindow = tk.Toplevel(self)
            self.helpWindow.resizable(0,0)
            self.helpWindow.title("Help")
            self.helpWindow.protocol("WM_DELETE_WINDOW", self.helpWindow.withdraw)

            helpMessage = tk.Message(self.helpWindow, text=ss_constants.shipHelp, justify=CENTER)
            helpMessage.grid(column=0, row=0)

    def buildSkillDisplay(self):
        '''Builds the skill display section'''
        self.skillDisplayLabel = tk.LabelFrame(self.master, text='Skills')
        self.skillDisplayLabel.grid(column=1, row=0, columnspan=3, rowspan=2, sticky=N, padx=2)

        self.buildFocusSkill()
        self.setDefaultClass()
        self.buildSubskills()
        self.buildMiscSkills()

    def buildFocusSkill(self):
        '''Builds the focus skill radiobuttons and level entry'''
        focusLabel = tk.LabelFrame(self.skillDisplayLabel, text='Focus Skill')
        focusLabel.grid(column=0, row=0, sticky=N+S)
        for key, value in ss_constants.skill_tree.items():
            radiobutton = tk.Radiobutton(focusLabel, text=value['name'], variable=ss_inputs.focusSkill,
                                         value=key, command=self.setDefaultClass)
            if key == 'combat_focus':
                i=0
            elif key =='recon_focus':
                i=1
            elif key == 'support_focus':
                i=2
            elif key == 'fleet_focus':
                i=3
            else: # Unused
                i=-1
            radiobutton.grid(column=0, columnspan=2, row=i, sticky=W)

        label = tk.Label(focusLabel, text='Level (0-22):')
        level = tk.Spinbox(focusLabel, from_=0, to=22, width=3, textvariable=ss_inputs.focusLevel)

        label.grid(column=0, row=4, sticky=W)
        level.grid(column=1, row=4, sticky=E, padx=4)

    def buildClassSkill(self):
        '''Builds the class skill radiobuttons and level entry'''
        if self.classWidget is not None:
            # Removes widget entirely to reset proper skill selection
            self.classWidget.grid_remove()
        classLabel = tk.LabelFrame(self.skillDisplayLabel, text='Class Skill')
        classLabel.grid(column=1, row=0, columnspan=3, sticky=N+S)
        for key, value in ss_constants.skill_tree[ss_inputs.focusSkill.get()].items():
            if key != 'name':
                radiobutton = tk.Radiobutton(classLabel, text=value['name'], variable=ss_inputs.classSkill,
                                             value=key, command=self.buildSubskills)
                # Chooses index based upon typical in-game listing of which skills are first
                if (key == 'berserker' or key == 'speed_demon'
                    or key == 'shield_monkey' or key == 'fleet_commander'):
                    i=0
                else:
                    i=1
                radiobutton.grid(column=0, columnspan=2, row=i, sticky=W)

        label = tk.Label(classLabel, text='Level (0-22):')
        level = tk.Spinbox(classLabel, from_=0, to=22, width=3, textvariable=ss_inputs.classLevel)

        label.grid(column=0, row=2, sticky=W)
        level.grid(column=1, row=2, sticky=E, padx=4)
        self.classWidget = classLabel
        # Runs buildSubskills() to reset subskills radiobuttons based upon new chosen first index
        self.buildSubskills()

    def buildSubskills(self):
        '''Builds the subskill radiobuttons and level entries'''
        if self.subskillWidget is not None:
            # Removes widget entirely to reset proper skill selection
            self.subskillWidget.grid_remove()
        subskillLabel = tk.LabelFrame(self.skillDisplayLabel, text='Subskills')
        subskillLabel.grid(column=4, row=0, sticky=NSEW)
        i=0
        for key, value in ss_constants.skill_tree[ss_inputs.focusSkill.get()][ss_inputs.classSkill.get()].items():
            if key != 'name':
                skill = None
                skill_level = None
                # Uses subSkill_#/subSkill_#Level to reduce variable usage
                if i==0:
                    ss_inputs.subSkill_1.set(key)
                    skillName = tk.Label(subskillLabel, text=value)
                    skillName.grid(column=0, columnspan=2, row=i, sticky=W)
                    label = tk.Label(subskillLabel, text='Level (0-20):')
                    level = tk.Spinbox(subskillLabel, from_=0, to=20, width=3, textvariable=ss_inputs.subskill_1Level)
                    label.grid(column=0, row=i+1, sticky=W)
                    level.grid(column=1, row=i+1, sticky=E, padx=4)
                elif i==2:
                    ss_inputs.subSkill_2.set(key)
                    skillName = tk.Label(subskillLabel, text=value)
                    skillName.grid(column=0, columnspan=2, row=i, sticky=W)
                    label = tk.Label(subskillLabel, text='Level (0-20):')
                    level = tk.Spinbox(subskillLabel, from_=0, to=20, width=3, textvariable=ss_inputs.subskill_2Level)
                    label.grid(column=0, row=i+1, sticky=W)
                    level.grid(column=1, row=i+1, sticky=E, padx=4)
                elif i==4:
                    ss_inputs.subSkill_3.set(key)
                    skillName = tk.Label(subskillLabel, text=value)
                    skillName.grid(column=0, columnspan=2, row=i, sticky=W)
                    label = tk.Label(subskillLabel, text='Level (0-20):')
                    level = tk.Spinbox(subskillLabel, from_=0, to=20, width=3, textvariable=ss_inputs.subskill_3Level)
                    label.grid(column=0, row=i+1, sticky=W)
                    level.grid(column=1, row=i+1, sticky=E, padx=4)
                i+=2
        self.subskillWidget = subskillLabel

    def buildMiscSkills(self):
        '''Builds aug tweak and imperial tweak inputs'''
        augTweakLabel = tk.Label(self.skillDisplayLabel, text="Aug Tweaking (0-25):")
        augTweakLabel.grid(column=0, row=1, sticky=E)
        augTweaklevel = tk.Spinbox(self.skillDisplayLabel, from_=0, to=25, width=3,
                                   textvariable=ss_inputs.augTweakLevel)
        augTweaklevel.grid(column=1, row=1, sticky=W)

        impTweakLabel = tk.Label(self.skillDisplayLabel, text="Imperial Tweaking (0-5):")
        impTweakLabel.grid(column=2, row=1, columnspan=3, padx=40, sticky=E)
        impTweaklevel = tk.Spinbox(self.skillDisplayLabel, from_=0, to=10, width=3,
                                   textvariable=ss_inputs.impTweakLevel)
        impTweaklevel.grid(column=4, row=1, padx=6, sticky=E)

    def setDefaultClass(self):
        '''Called by choosing a focus skill, resets proper pre-selected class'''
        if (ss_inputs.focusSkill.get() == 'combat_focus'):
            ss_inputs.classSkill.set('berserker')
        elif (ss_inputs.focusSkill.get() == 'recon_focus'):
            ss_inputs.classSkill.set('speed_demon')
        elif (ss_inputs.focusSkill.get() == 'support_focus'):
            ss_inputs.classSkill.set('shield_monkey')
        elif (ss_inputs.focusSkill.get() == 'fleet_focus'):
            ss_inputs.classSkill.set('fleet_commander')
        self.buildClassSkill()

    def buildStatDisplay(self):
        '''Builds stat inputs, bonus displays, and total displays'''
        displayLabel = tk.LabelFrame(self.master, text='Input and Output')
        displayLabel.grid(column=0, row=2, columnspan=2, sticky=W+E, padx=2)

        self.buildBaseInput(displayLabel)
        self.buildBonusAmount(displayLabel)
        self.buildFinalDisplay(displayLabel)

    def buildBaseInput(self, master):
        '''Builds stat inputs with validator'''
        label = tk.Label(master, text='Base Input', padx=20)
        baseInputLabel = tk.LabelFrame(master, labelwidget=label, borderwidth=0)
        baseInputLabel.grid(column=0, row=0, sticky=W+E)

        vcmd_all = (master.register(ss_validators.shipStatValidate),
                    '%d', '%i', '%P', '%s', '%S')
        i=0
        for key, value in ss_inputs.baseInputs.items():
            statName = tk.Label(baseInputLabel, text=ss_constants.statNames[key])
            statName.grid(column=0, row=i, sticky=W)

            if key == 'shieldCharge' or key == 'energyCharge' or key == 'RoF' or key == 'resist':
                width = 5
                vcmd = (master.register(ss_validators.shipDecimalValidate),
                        '%d', '%i', '%P', '%s', '%S')
                if key == 'RoF':
                    unitText = 's'
                elif key == 'shieldCharge':
                    unitText = '/s'
                elif key == 'energyCharge':
                    unitText = '/1.2s'
                elif key == 'resist':
                    unitText = '%'
                    vcmd = (master.register(ss_validators.bonusStatValidate),
                            '%d', '%i', '%P', '%s', '%S')
                else:
                    unitText = 'err'
                unit = tk.Label(baseInputLabel, text=unitText)
                unit.grid(column=2, row=i, sticky=W)
            else:
                width = 10
                vcmd = vcmd_all

            amount = tk.Entry(baseInputLabel, width=width, justify=RIGHT, textvariable=value['initial'],
                              validate='key', validatecommand=vcmd)
            # Width/5 so that larger entries span 2 columns
            amount.grid(column=1, row=i, columnspan=(width/5), sticky=W, padx=2)
            if key == 'elecTemp':
                statName.configure(text="Firing Energy:")
                statName.update()
            i+=1

    def buildBonusAmount(self, master):
        '''Builds the display for bonus amount'''
        label = tk.Label(master, text='Bonus', padx=10)
        bonusAmountLabel = tk.LabelFrame(master, labelwidget=label, borderwidth=0)
        bonusAmountLabel.grid(column=1, row=0, sticky=NW+E)
        i=0
        for key, value in ss_inputs.baseInputs.items():
            mathSign = u"\u2715" # is the multiplication sign
            if key == 'RoF':
                mathSign = u"\u00F7" # is the division sign
            symbol = tk.Label(bonusAmountLabel, text=mathSign)
            amount = tk.Entry(bonusAmountLabel, width=4, state="readonly",
                              justify=RIGHT, textvariable=value['bonus'])
            symbol.grid(column=0, row=i, sticky=W+E)
            amount.grid(column=1, row=i, sticky=E, padx=6)
            i+=1

    def buildFinalDisplay(self, master):
        '''Builds the display for the total amount'''
        label = tk.Label(master, text='Overall', padx=15)
        finalLabel = tk.LabelFrame(master, labelwidget=label, borderwidth=0)
        finalLabel.grid(column=2, row=0, sticky=W+E)
        i=0
        for key, value in ss_inputs.baseInputs.items():
            equalsSign = tk.Label(finalLabel, text="=")
            equalsSign.grid(column=0, row=i, sticky=W)

            width = 10
            if key == 'shieldCharge' or key == 'energyCharge' or key == 'RoF':
                width = 5
            amount = tk.Entry(finalLabel, width=width, justify=RIGHT, state="readonly", textvariable=value['overall'])
            # Width/5 so that larger entries span 2 columns
            amount.grid(column=1, row=i, columnspan=(width/5), sticky=W, padx=2)
            if width == 5:
                if key == 'shieldCharge':
                    unitText = '/s'
                elif key == 'energyCharge':
                    unitText = '/1.2s'
                elif key == 'RoF':
                    unitText = 's'
                else:
                    unitText = 'err'
                unit = tk.Label(finalLabel, text=unitText)
                unit.grid(column=2, row=i, sticky=W)
            i+=1

    def buildAugDisplay(self):
        '''Builds aug display section'''
        self.augDisplayLabel = tk.LabelFrame(self.master, text='Augmenters')
        self.augDisplayLabel.grid(column=2, row=2, columnspan=2, rowspan=3, sticky=NE+W, padx=2)

        self.buildAugConfig()

    def buildAugConfig(self):
        '''Builds aug number change input and freeze box'''
        self.augLabelList = []
        self.augButtonList = []
        self.augClearButtonList = []

        label = tk.Label(self.augDisplayLabel, text='Number:')
        label.grid(column=0, row=0, padx=4, sticky=E)

        self.augNumber = tk.Spinbox(self.augDisplayLabel, from_=0, to=6, width=2, state="readonly",
                           textvariable=ss_inputs.augNumber, command=self.changeAugAmount)
        self.augNumber.grid(column=1, row=0, sticky=E)

        self.freezeAugsCheck = tk.IntVar()
        checkbutton = tk.Checkbutton(self.augDisplayLabel, text="Freeze",
                                     variable=self.freezeAugsCheck, command=self.freezeAugs)
        checkbutton.grid(column=2, row=0, columnspan=2, sticky=E)

    def changeAugAmount(self):
        '''Adds or removes a set of aug edit/reset buttons'''
        if int(ss_inputs.augNumber.get()) > len(self.augButtonList):
            numberToAdd = int(ss_inputs.augNumber.get())-(len(self.augButtonList))
            for i in range(numberToAdd):
                position = len(self.augButtonList) + 1

                name = "Aug " + str(position) + ":"
                augLabel = tk.Label(self.augDisplayLabel, width=15, anchor=W, text=name)
                augLabel.grid(column=0, row=position, columnspan=3, padx=4, sticky=W)

                self.augLabelList.append(augLabel)

                editButton = tk.Button(self.augDisplayLabel, text="Edit",
                                   command=lambda: self.editAug(position))
                editButton.grid(column=3, row=position, sticky=E)

                self.augButtonList.append(editButton)

                resetButton = tk.Button(self.augDisplayLabel, text="Reset",
                                   command=lambda: self.resetAug(position))
                resetButton.grid(column=4, row=position, padx=4, sticky=W)

                self.augClearButtonList.append(resetButton)
                ss_inputs.augs.append(ss_inputs.augmenter())
        else:
            for i in range(len(self.augButtonList)-(int(ss_inputs.augNumber.get()))):
                toRemove = self.augLabelList.pop()
                toRemove.grid_remove()
                toRemove = self.augButtonList.pop()
                toRemove.grid_remove()
                toRemove = self.augClearButtonList.pop()
                toRemove.grid_remove()
                toRemove = None
                ss_inputs.augs.pop()


    def editAug(self, augNum):
        '''Edit augmenter popup'''
        augNum = augNum - 1
        if not hasattr(self, 'augWindows'):
            self.augWindows = []
        if len(self.augWindows) > augNum and self.augWindows[augNum] is not None:
            self.augWindows[augNum].deiconify()
        else:
            popup = augToplevel(master=self, augNum=augNum)
            popup.resizable(0,0)

            self.augWindows.insert(augNum, popup)

            title = ss_inputs.augs[augNum]['name'].get()
            if title == "":
                title = "Aug " + str(augNum + 1)
            popup.title(title)

            statLabel = tk.Label(popup, text=ss_constants.statNames['name'], padx=3)
            statLabel.grid(column=0, row=0, sticky=W+E)
            statEntry = tk.Entry(popup, width=15, justify=RIGHT, textvariable=ss_inputs.augs[augNum].get('name'))
            statEntry.grid(column=1, row=0, columnspan=3)

            augFrame= tk.LabelFrame(popup, text="Augmenter Stats")
            augFrame.grid(column=0, row=1, columnspan=4, padx=1, sticky=W+E)

            vcmd = (popup.register(ss_validators.bonusStatValidate),
                    '%d', '%i', '%P', '%s', '%S')
            # vcmd = (popup.register(self.bonusStatValidate),
            #         '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
            # %v = validation_type, %V =  trigger_type, %W =  widget_name
            i=1
            for key, value in ss_inputs.augs[augNum].items():
                if key != 'enabled' and key != 'name':
                    statLabel = tk.Label(augFrame, text=ss_constants.statNames[key], padx=3)
                    statLabel.grid(column=0, row=i, sticky=E)
                    statEntry = tk.Entry(augFrame, width=6, justify=RIGHT, textvariable=value,
                                         validate='key', validatecommand=vcmd)
                    statEntry.grid(column=1, row=i)
                    percentLabel = tk.Label(augFrame, text="%", padx=3)
                    percentLabel.grid(column=2, row=i)
                    i+=1
            resetButton = tk.Button(popup, text="Reset", command=lambda: self.resetAug(augNum))
            resetButton.grid(column=0, row=2)
            updateButton = tk.Button(popup, text="Update and Close", command=lambda: popup.destroy())
            updateButton.grid(column=1, row=2, columnspan=3)

    def updateAug(self, augNum):
        '''Update aug name in main frame'''
        name = ss_inputs.augs[augNum]['name'].get()
        if name == "":
            name = "Aug " + str(augNum + 1) + ":"
        self.augLabelList[augNum].configure(text=name)
        self.augLabelList[augNum].update()

    def resetAug(self, augNum):
        '''Reset all values to null for the aug required'''
        for key, value in ss_inputs.augs[augNum-1].items():
            if key != 'enabled':
                value.set("")
        self.augLabelList[augNum-1].configure(text="Aug " + str(augNum) + ":")
        self.augLabelList[augNum-1].update()

    def freezeAugs(self):
        '''Toggles the freezing of the amount of augs available and the input being disabled'''
        if self.freezeAugsCheck.get(): # frozen
            self.augNumber.configure(state=DISABLED)
            self.augNumber.update()
        else: # unfrozen
            self.augNumber.configure(state="readonly")
            self.augNumber.update()

    def buildModDisplay(self):
        '''Builds the buttons for item mods and auras'''
        modDisplayLabel = tk.LabelFrame(self.master, text='Misc. Mods')
        modDisplayLabel.grid(column=2, row=1, columnspan=3, rowspan=3, sticky=SW+SE)

        button = tk.Button(modDisplayLabel, text="Edit Item Mods", command=self.buildItemModInput)
        button.grid(column=0, row=0, sticky=E, padx=1, pady=1)

        button = tk.Button(modDisplayLabel, text="Edit Auras", command=self.buildAuraInput)
        button.grid(column=1, row=0, sticky=E, padx=1, pady=1)

    def buildItemModInput(self):
        '''Builds item mod input popup'''
        itemModPopup = tk.Toplevel(master=self)
        itemModPopup.resizable(0,0)
        itemModPopup.title("Item Mods")

        addModButton = tk.Button(itemModPopup, text="Add Item Mod", command=self.addItemMod)
        addModButton.grid(column=0, row=0, pady=2, padx=2)

        resetAllButton = tk.Button(itemModPopup, text="Reset and Remove All Mods", command=self.resetItemMods)
        resetAllButton.grid(column=1, row=0, pady=2, padx=2)

        self.modDisplayFrame = tk.LabelFrame(itemModPopup, text="Mods:")
        self.modDisplayFrame.grid(column=0, row=1, columnspan=2, padx=2, sticky=NSEW)

        message = tk.Message(self.modDisplayFrame, name='helpMessage', text='Section Disabled')
        message.grid(column=0, row=0)

    def addItemMod(self):
        for name, widget in self.modDisplayFrame.children.items():
            if name == 'helpMessage':
                if widget.grid_info():
                    widget.grid_remove()
        editModPopup = itemModToplevel(master=self)
        editModPopup.resizable(0,0)
        editModPopup.title("This function is disabled")

    def resetItemMods(self):
        for name, widget in self.modDisplayFrame.children.items():
            if name == 'helpMessage':
                widget.grid(column=0, row=0)
        pass

    def updateMods(self):
        print "test"

    def buildAuraInput(self):
        '''Builds aura input popup'''
        popup = tk.Toplevel(master=self)
        popup.resizable(0,0)
        popup.title("This function is disabled")

        message = tk.Message(master=popup, text="(July 11, 2014): This is disabled until I can make the gui for it")
        message.pack()

    def buildCalcButton(self):
        '''Builds the calculate button'''
        calcButton = tk.Button(self.master, text='Calculate', command=ss_math.calculate)
        calcButton.grid(column=0, row=4, sticky=NE, pady=2)

    def buildQuitButton(self):
        '''Builds the quit button'''
        quitButton = tk.Button(self.master, text='Quit', command=self.quit)
        quitButton.grid(column=1, row=4, sticky=NE, pady=2)

    def destroy(self):
        '''Overrides destroy due to possible exception, forces a hard quit'''
        try:
            tk.Frame.destroy(self)
        except tk.TclError or TypeError:
            pass

class augToplevel(tk.Toplevel):
    '''Extension of Tkinter.Toplevel to allow for updating an aug on destroy of the popup'''
    def __init__(self, master, augNum=None, *args, **kwargs):
        tk.Toplevel.__init__(self, master=master)
        self.master = master
        self.augNum = augNum

    def destroy(self):
        self.master.updateAug(self.augNum)
        tk.Toplevel.withdraw(self)

class itemModToplevel(tk.Toplevel):
    '''Extension of Tkinter.Toplevel to allow for updating the iteMod list on destroy of the popup'''
    def __init__(self, master, *args, **kwards):
        tk.Toplevel.__init__(self, master=master)
        self.master = master

    def destroy(self):
        self.master.updateMods()
        tk.Toplevel.withdraw(self)