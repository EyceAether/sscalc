# -*- mode: python -*-
a = Analysis(['ss_calc.py'],
             pathex=['C:\\Users\\davburge\\Work\\PycharmProjects\\sscalc'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SS_StatCalc.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='wtfBD.ico')
