import sys
import os
from pathlib import Path

# Simula il path del progetto usando la directory corrente
sys.path.insert(0, str(Path(os.path.abspath('.'))))

from util_py.resouces_handler import collect_folder_file

# Import delle funzioni base da PyInstaller per definire i vari step della build
from PyInstaller.building.build_main import Analysis, PYZ, EXE

# -------------------------------------------------------
# 1) Definizione dei dati da includere (es. cartelle, immagini, assets)
#    Qui prendo tutta la cartella "assets" e i suoi file
datas = collect_folder_file('assets')

# -------------------------------------------------------
# 2) Lista dei moduli nascosti da includere esplicitamente
#    Perché PyInstaller non li trova da solo, es. import dinamici
hidden_imports = [
    "PIL._tkinter_finder",  # necessario per ImageTk e tkinter
    "PIL.ImageTk",
    "PIL.ImageDraw",
    "import_pyinstaller",   # il tuo file di import se lo usi ancora
]

# -------------------------------------------------------
# 3) Analisi del codice
#    Qui PyInstaller scansiona il tuo script principale e i suoi moduli
a = Analysis(
    ["tris_main.py"],   # file di partenza principale
    pathex=["."],       # path di ricerca (qui cartella corrente)
    binaries=[],        # file binari esterni da includere (se ce ne sono)
    datas=datas,        # assets e dati da includere
    hiddenimports=hidden_imports,  # i moduli nascosti da includere
    hookspath=[],       # percorsi di hook personalizzati (spesso vuoto)
    runtime_hooks=[],   # script da eseguire all'avvio (raro)
    excludes=[],        # moduli da escludere se vuoi (raramente usato)
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,        # se usi cifratura del pacchetto (quasi mai)
)

# -------------------------------------------------------
# 4) Creazione archivio Python "PYZ"
#    Qui PyInstaller crea un archivio compresso con i bytecode Python
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# -------------------------------------------------------
# 5) Creazione dell'eseguibile
#    Qui PyInstaller mette insieme tutto in un unico file eseguibile
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="my_tris",   # nome eseguibile generato
    debug=False,        # True se vuoi log di debug (utile per test)
    bootloader_ignore_signals=False,
    strip=False,        # True per rimuovere simboli debug (più leggero)
    upx=True,           # True per comprimere con UPX (se lo hai installato)
    console=True,       # True se vuoi il terminale (False se GUI pura)
)
