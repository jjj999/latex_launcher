import json
import subprocess
import shutil
import os
from os.path import join, isdir, abspath, isfile

import pyperclip

from texl.const import *
from texl.util import *
from texl.figure.image import Image
from texl.figure.figure import Figure
from texl.figure.subfigure import SubFigure


#   コマンドの処理に対応するクラス
class Latexec:
    
    
    def __init__(self):
        self.setting:dict = None
        
        # オブジェクト生成時にsetting.jsonをロードする
        with open(PATH_MY_SETTING, "rt", encoding="utf-8") as f:
            self.setting = json.load(f)

    
    #   .texlディレクトリの構築
    #   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    #   NOTE
    #   .texlの構成を変更する場合はここを編集する．
    @classmethod
    def make_texl(cls, path_res):
        if isdir(PATH_MY_TEXL):
            shutil.rmtree(PATH_MY_TEXL)
        os.mkdir(PATH_MY_TEXL)
        os.mkdir(PATH_MY_TEMP)
        
        # ダウンロードしたリポジトリ内のデフォルトテンプレートをコピー
        with open(join(path_res, "default.tex"), "rt", encoding="utf-8") as rf:
            with open(PATH_DEFAULT_TEMPRATE, "wt", encoding="utf-8") as wf:
                wf.write(rf.read())
                
        # ダウンロードしたリポジトリ内のhelp.txtをコピー
        with open(join(path_res, "help.txt"), "rt", encoding="utf-8") as rf:
            with open(PATH_HELP, "wt", encoding="utf-8") as wf:
                wf.write(rf.read())
        
    
    #   setting.jsonの構築
    #   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    #   NOTE
    #   初期のsetting.jsonの内容を変更する場合はここを編集する．
    @classmethod
    def configure_json(cls, name):
        
        setting = {}
        
        setting[KEY_USER_NAME] = name
        setting[KEY_CURRENT_TEMP] = PATH_DEFAULT_TEMPRATE
        setting[KEY_CURRENT_PROJECT] = None
        setting[KEY_TEMPS] = {}
        setting[KEY_TEMPS][KEY_DEFAULT_TEMP] = PATH_DEFAULT_TEMPRATE
        
        with open(PATH_MY_SETTING, "wt", encoding="utf-8") as f:
            f.write(json.dumps(setting, indent=4))
            

    #   setting.jsonの書き換え
    #   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    #   NOTE
    #   setting.jsonの情報を更新する操作があった場合に最後に呼び出す．
    def update(self):
        with open(PATH_MY_SETTING, "wt", encoding="utf-8") as f:
            f.write(json.dumps(self.setting, indent=4))
            
    
    #   コマンド用メソッド
    #   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    #   各コマンドに対応するメソッドを定義していく
    #
    #   NOTE
    #   *   setting.jsonの情報が必要ない場合はクラスメソッドとして定義する．
    
    #   マニュアルをlessで表示
    @classmethod  
    def man(cls):
        
        if not isfile(PATH_HELP):
            print("まず 'texl setup' を実行し，セットアップを完了させてください．")
        else:
            subprocess.run(["less", PATH_HELP])
    
            
    #   初期セットアップ
    @classmethod
    def setup(cls):
        
        name = input("名前を入力してください: ")
        if not os.path.exists(PATH_MY_TEXL):
            cls.make_texl()
            
        cls.configure_json(name)            # setting.jsonの編集
        
        ishelp = input("使い方を確認しますか？[y/n]: ")
        
        # 使い方をlessで表示
        if isyes(ishelp):
            subprocess.run(["less", PATH_HELP])
            
    
    #   使いたいテンプレートファイルと別名を保存
    def set_temp(self, path, name):
        
        # .texl/temp/ にテンプレートファイルを name.tex の名前でコピー
        temp_path = join(PATH_MY_TEMP, name + TEX_EXTENSION)
        with open(path, "rt", encoding="utf-8") as rf:
            with open(temp_path, "wt", encoding="utf-8") as wf:
                wf.write(rf.read())
        
        # setting.json にテンプレートファイル情報を登録
        self.setting[KEY_TEMPS][name] = temp_path
        self.update()
        
    
    #   使用するテンプレートファイルを更新
    def use(self, name):
        self.setting[KEY_CURRENT_TEMP] = self.setting[KEY_TEMPS][name]
        self.update()
        
        
    #   指定されたテンプレートファイルを.texlから削除
    def rm(self, name):
        f_name = self.setting[KEY_TEMPS].pop(name)
        os.remove(f_name)
        
        # 現在のテンプレートに設定されている場合はデフォルトに変更
        if self.setting[KEY_CURRENT_TEMP] == f_name:
            self.setting[KEY_CURRENT_TEMP] = PATH_DEFAULT_TEMPRATE
            
        self.update()
        
    
    #   新規プロジェクトの立ち上げ
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
        os.mkdir(join(project, DIR_DATA))
        
        # テンプレートファイルをプロジェクト内にコピー
        use_temp = self.setting[KEY_TEMPS][temp] if temp else self.setting[KEY_CURRENT_TEMP]    # 絶対パス
        tex_file = join(project, DIR_SOURCE, name + TEX_EXTENSION)
        shutil.copy(use_temp, tex_file)
        
        # テンプレートファイルのヘッダー部分を編集
        set_header(tex_file,
                   title=title,
                   author=self.setting[KEY_USER_NAME],
                   fig=PATH_RELATIVE_FIG)
        
        # 現在のプロジェクトディレクトリを登録
        self.setting[KEY_CURRENT_PROJECT] = project
        self.update()
        
    
    #   現在のプロジェクトディレクトリを変更
    def start(self, d:str):
        self.setting[KEY_CURRENT_PROJECT] = abspath(d)
        self.update()
        
    
    #   画像挿入用のテンプレートコードを作成
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
        
        pyperclip.copy(figure.make())
            
            
if __name__ == "__main__":
    pass