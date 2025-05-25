# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ["C:/Users/809561/OneDrive - Land O'Lakes, Inc/Documents/GitHub/vtask/LOL_VtaskDEV_errorhandle/Final_create_Vtasks_ER.py"],
    pathex=[],
    binaries=[],
    datas=[("C:/Users/809561/OneDrive - Land O'Lakes, Inc/Documents/GitHub/vtask/LOL_VtaskDEV_errorhandle/.env", '.'), ("C:/Users/809561/OneDrive - Land O'Lakes, Inc/Documents/GitHub/vtask/LOL_VtaskDEV_errorhandle/requirements.txt", '.'), ("C:/Users/809561/OneDrive - Land O'Lakes, Inc/Documents/GitHub/vtask/LOL_VtaskDEV_errorhandle/secret.txt", '.')],
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
    name='vtas_dev',
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
)
