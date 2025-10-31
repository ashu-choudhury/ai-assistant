# -*- mode: python ; coding: utf-8 -*-

block_cipher = None  # Disable encryption unless you explicitly need it

a = Analysis(
    ['jarvis.py'],
    pathex=['.'],  # Add current directory for relative imports
    binaries=[],
    datas=[
        # Add any static data here if used by Jarvis
        # Example: ('assets/', 'assets/')
    ],
    hiddenimports=[
        # Explicitly include hidden imports to avoid overhead
        # Example: 'speech_recognition', 'pyttsx3.drivers.sapi5'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Exclude heavy, unused libraries (saves space)
        'tkinter',
        'numpy',
        'matplotlib',
        'PIL',
        'pytest',
        'test',
        'unittest',
        'email',
        'http',
        'xml',
    ],
    noarchive=False,     # Leave as False for better load time
    optimize=2,          # Maximum Python bytecode optimization
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='jarvis',
    debug=False,
    bootloader_ignore_signals=True,
    strip=True,             # Removes debug symbols to reduce binary size
    upx=True,               # Compress binaries with UPX
    upx_exclude=[],         # You can add binaries here that crash with UPX
    console=False,          # GUI app (change to True if console needed)
    disable_windowed_traceback=True,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='jarvis.ico'       # Optional: add an icon for branding
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=True,             # Strip extra binary metadata
    upx=True,
    upx_exclude=[],
    name='jarvis'
)
