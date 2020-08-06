from os.path import join

import PyInstaller.__main__

PyInstaller.__main__.run(["--name=texl",
                          "--onefile",
                          join("texl", "texl.py")])