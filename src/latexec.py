import json
import subprocess
import shutil
import os
from os.path import join, isdir, abspath, isfile

from const import *
from util import *
from image import Image
from figure import Figure
from subfigure import SubFigure
from window import pop_text_window


class Latexec:
    
    
    def __init__(self):
        self.setting:dict = None
        
        # オブジェクト生成時にsetting.jsonをロードする
        with open(PATH_MY_SETTING, "rt", encoding="utf-8") as f:
            self.setting = json.load(f)
            
    
    # マニュアルをlessで表示
    @classmethod  
    def man(cls):
        
        if not isfile(PATH_HELP):
            print("まず 'ltl setup' を実行し，セットアップを完了させてください．")
        else:
            subprocess.run(["less", PATH_HELP])
        
    
    # 初期セットアップ
    @classmethod
    def setup(cls):
        
        name = input("名前を入力してください: ")
        cls.make_ltl()                      # .ltlディレクトリの作成
        cls.configure_json(name)            # setting.jsonの編集
        
        ishelp = input("使い方を確認しますか？[y/n]: ")
        
        # 使い方をlessで表示
        if isyes(ishelp):
            subprocess.run(["less", PATH_HELP])
            
            
    @classmethod
    def make_ltl(cls):
        if isdir(PATH_MY_LTL):
            shutil.rmtree(PATH_MY_LTL)
        os.mkdir(PATH_MY_LTL)
        os.mkdir(PATH_MY_TEMP)
        
        with open("default.tex", "rt", encoding="utf-8") as rf:
            with open(PATH_DEFAULT_TEMPRATE, "wt", encoding="utf-8") as wf:
                wf.write(rf.read())
                
        with open("help.txt", "rt", encoding="utf-8") as rf:
            with open(PATH_HELP, "wt", encoding="utf-8") as wf:
                wf.write(rf.read())
        
    
    @classmethod
    def configure_json(cls, name):
        
        setting = {}
        
        setting[KEY_USER_NAME] = name
        setting[KEY_CURRENT_TEMP] = PATH_DEFAULT_TEMPRATE
        setting[KEY_TEMPS] = {}
        setting[KEY_TEMPS][KEY_DEFAULT_TEMP] = PATH_DEFAULT_TEMPRATE
        
        with open(PATH_MY_SETTING, "wt", encoding="utf-8") as f:
            f.write(json.dumps(setting, indent=4))
            
    
    # 使いたいテンプレートファイルと別名を保存
    def set_temp(self, path, name):
        
        # .ltl/temp/ にテンプレートファイルを name.tex の名前でコピー
        temp_path = join(PATH_MY_TEMP, name + TEX_EXTENSION)
        with open(path, "rt", encoding="utf-8") as rf:
            with open(temp_path, "wt", encoding="utf-8") as wf:
                wf.write(rf.read())
        
        # setting.json にテンプレートファイル情報を登録
        self.setting[KEY_TEMPS][name] = temp_path
        self.update()
        
    
    # 使用するテンプレートファイルを更新
    def use(self, name):
        self.setting[KEY_CURRENT_TEMP] = self.setting[KEY_TEMPS][name]
        self.update()
        
    
    # 新規プロジェクトの立ち上げ
    def launch(self,
               name,
               title="",
               path=None,
               temp=None):
        
        # プロジェクトディレクトリの作成
        project_root = path if path else abspath(os.getcwd())
        project = join(project_root, name)
        os.mkdir(project)
        os.mkdir(join(project, DIR_SOURCE))
        os.mkdir(join(project, DIR_FIGURE))
        os.mkdir(join(project, DIR_TABLE))
        
        # テンプレートファイルをプロジェクト内にコピー
        use_temp = self.setting[KEY_TEMPS][temp] if temp else self.setting[KEY_CURRENT_TEMP]    # 絶対パス
        tex_file = join(project, DIR_SOURCE, name + TEX_EXTENSION)
        shutil.copy(use_temp, tex_file)
        
        # テンプレートファイルのヘッダー部分を編集
        set_header(tex_file,
                   title=title,
                   author=self.setting[KEY_USER_NAME],
                   fig=join(project, DIR_FIGURE))
        
        # 現在のプロジェクトディレクトリを登録
        self.setting[KEY_CURRENT_PROJECT] = project
        self.update()
        
    
    # 現在のプロジェクトディレクトリを変更
    def start(self, d:str):
        self.setting[KEY_CURRENT_PROJECT] = abspath(d)
        self.update()
        
    
    # 画像挿入用のテンプレートコードを作成
    def fig(self, imgs:tuple, width=12, window=True) -> str:
        
        figure = Figure()
        images = [Image(width, img) for img in imgs]

        if len(imgs) == 1:
            figure.include(images[0])
        else:
            subfigures = []
            for image in images:
                subfigure = SubFigure()
                subfigure.include(image)
                subfigures.append(subfigure)
            
            figure.include(*tuple(subfigures))
        
        # 別ウィンドウで表示
        if window:
            pop_text_window(figure.make())
        # 標準出力に表示
        else:
            print(figure.make())
        
        
    # setting.jsonの書き換え
    def update(self):
        with open(PATH_MY_SETTING, "wt", encoding="utf-8") as f:
            f.write(json.dumps(self.setting, indent=4))
            
            
if __name__ == "__main__":
    pass