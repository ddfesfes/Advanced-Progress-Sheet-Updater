# -*- mode: python ; coding: utf-8 -*-

import os

appdata_path = os.path.join(os.getenv("APPDATA"), "Python", "Python312")

a = Analysis(
    ['main.py'],
    datas=[(os.path.join(appdata_path, 'site-packages', 'google_api_python_client-2.145.0.dist-info', '*'),
            'google_api_python_client-2.145.0.dist-info')]
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='ProgressSheetUpdater.exe',
    debug=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=True,
    icon='icon.ico'
)