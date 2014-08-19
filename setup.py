# __author__ = 'davburge'
#
# from distutils.core import setup
# import py2exe, sys, os
#
# sys.argv.append('py2exe')
#
# setup(
#     options={'py2exe': {'bundle_files': 2, 'compressed': True}},
#     windows=[{
#                  'script': "ss_calc.py",
#                  "icon_resources": [(1, "wtfBD.ico")]
#              }],
#     zipfile=None,
# )

# #py -3.4 -m py2exe.build_exe -b 2 -c ss_calc.py
use_in_terminal = 'pyinstaller -n "SS_StatCalc" -F -i wtfBD.ico ss_calc.py'
print(use_in_terminal)
