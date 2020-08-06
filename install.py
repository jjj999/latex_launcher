import platform
import shutil
import os
import sys
import subprocess

import PyInstaller.__main__

sys.path.append(os.getcwd())
import texl.latexec
from texl.util import isinclude


def conf_dir(path_exe):
    shutil.move(path_exe, texl.PATH_MY_TEXL)
    shutil.rmtree(os.path.join(os.getcwd(), "build"))
    shutil.rmtree(os.path.join(os.getcwd(), "dist"))
    os.remove(os.path.join(os.getcwd(), "texl.spec"))
    
    
def conf_sys():
    home = os.path.expanduser("~")
    
    if platform.system() == "Linux":
        
        registered = False
        bashrc = os.path.join(home, ".bashrc")
        
        with open(bashrc, "rt") as f:
            line = ""
            while True:
                line = f.readline()
                if not line:
                    break
                
                if isinclude(".texl", line):
                    registered = True
                    
        if not registered:
            with open(bashrc, "at") as f:
                adding = ['',
                        '# set PATH so it includes .texl if it exists',
                        'if [ -d "$HOME/.texl" ] ; then',
                        '    PATH="$HOME/.texl:$PATH"',
                        'fi']
                f.write("\n".join(adding))
            
            subprocess.run(["bash", bashrc])
            print(os.environ["PATH"])


if __name__ == "__main__":
    
    path_exe = os.path.join(os.getcwd(), "dist", "texl")
    texl.latexec.Latexec.make_texl(os.path.join(os.getcwd(), "res"))

    PyInstaller.__main__.run(["--name=texl",
                            "--onefile",
                            os.path.join("texl", "_cmd.py")])
    if platform.system() == "Windows":
        path_exe += ".exe"
    
    conf_dir(path_exe)
    conf_sys()