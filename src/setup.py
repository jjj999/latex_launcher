import os
from os.path import abspath, join, dirname, expanduser
import shutil
import subprocess
import json

from const import *
from util import isyes, set_key


def setup():
    
    """セットアップを行なう
    
    アプリケーションを動かすためのセットアップを行なう．
    セットアップでユーザーが入力したデータはホームディレクトリ下の
    .ltlディレクトリのsetting.jsonに保存される．
    """
    
    name = input("名前を入力してください: ")
    istemp = input("デフォルトのテンプレートファイルを使用しますか？[y/n]: ")
    
    if not isyes(istemp):
        print("""
              テンプレートファイルをデフォルトに設定しませんでした．後ほど set コマンドを用いて
              自身のテンプレートファイルを指定することが出来ます．指定しない場合，プロジェクト作成時，
              空のtexファイルが生成されます．詳しくは man コマンドでマニュアルを表示し，参照してください．
              """)
    
    ishelp = input("使い方を確認しますか？[y/n]: ")
    
    # 使い方をlessで表示
    if isyes(ishelp):
        subprocess.run(["less", PATH_HELP])
    
    # .ltlディレクトリの作成
    if os.path.isdir(PATH_MY_LTL):
        shutil.rmtree(PATH_MY_LTL)
    shutil.copytree(PATH_DEFAULT_LTL, PATH_MY_LTL)
    
    # setting.jsonの編集
    with open(PATH_MY_SETTING, "rt") as f:
        setting = json.load(f)
    
    setting[KEY_USER_NAME] = name
    setting[KEY_ALWAYS_USE_TEMP] = isyes(istemp)
    
    with open(PATH_MY_SETTING, "wt") as f:
        f.write(json.dumps(setting, indent=4))
        
        
if __name__ == "__main__":
    setup()