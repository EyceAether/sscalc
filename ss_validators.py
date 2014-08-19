__author__ = 'davburge'

import re
percentRegex = re.compile('(^[-+]?[0]?[.]{1}[\d]*|^[-+]?[123456789]{1,}[\d]*[.]?[\d]*|^[-+0]{1}|^[-+]?[0]?)\Z')
# Floats with +- signs, no leading 0 unless +-0.### or 0.###
bankRegex = re.compile('(^[123456789]{1,}[\d]*)\Z')
# Only ints, no leading 0
decimalRegex = re.compile('(^[123456789]{1,}[\d]*[.]?[\d]*|^[0]?[.]{1}[\d]*|^[0]{1})\Z')
# Floats, no leading 0 unless 0.###
auraRegex = re.compile('([-+]?[0]?[.]{1}[\d]*[%]?|[-+]?[123456789]{1,}[\d]*[.]?[\d]*[%]?|[-+]?[0]?)\Z')
# + or - floats that may be percentages

def shipStatValidate(action, index, value_if_allowed, prior_value, text):
    if action == '0': # If Delete then allow
        return True
    if bankRegex.match(value_if_allowed) is not None:
        return True
    else:
        return False

def shipDecimalValidate(action, index, value_if_allowed, prior_value, text):
    if action == '0': # If Delete then allow
        return True
    if decimalRegex.match(value_if_allowed) is not None:
        return True
    else:
        return False

# def validate(self, action, index, value_if_allowed,
#                    prior_value, text, validation_type, trigger_type, widget_name):
def bonusStatValidate(action, index, value_if_allowed, prior_value, text):
    if action == '0': # If Delete then allow
        return True
    if percentRegex.match(value_if_allowed) is not None:
        return True
    else:
        return False

def auraValidate(action, index, value_if_allowed, prior_value, text):
    if action == '0': # If Delete then allow
        return True
    if auraRegex.match(value_if_allowed) is not None:
        return True
    else:
        return False
