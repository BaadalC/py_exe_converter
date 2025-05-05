# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ["C:/Users/809561/OneDrive - Land O'Lakes, Inc/Documents/GitHub/vtask/GetJobLog/jobinfo_watchlistupdate.py"],
    pathex=[],
    binaries=[],
    datas=[("C:/Users/809561/OneDrive - Land O'Lakes, Inc/Documents/GitHub/vtask/GetJobLog/LandOLakes.png", '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='jobinfo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\809561\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\win10toast\\data\\python.ico'],
)
