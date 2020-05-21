import os
from os.path import join, abspath, dirname, expanduser
import re


# プロジェクトリポジトリ名
PROJECT_NAME = "latex_launcher"

# コマンド名
COMMAND_TYPE = "command"

COMMAND_MANUAL = "man"          # マニュアルを表示
COMMAND_SETUP = "setup"           # セットアップ

COMMAND_SET_TEMP = "set"        # テンプレートファイルと別名をセット
                                # >> ltl set temp.tex report
                                #       # temp.texをreportという名前で登録

COMMAND_USE_TEMP = "use"        # 現在のテンプレートファイルをセット

COMMAND_REMOVE_TEMP = "rm"      # 指定されたテンプレートファイルを.ltlから削除する
                                # 現在のテンプレートを削除した場合，デフォルトを代わりに設定する

COMMAND_LAUNCH = "launch"       # プロジェクトの生成，引数としてプロジェクト名をとる
COMMAND_LAUNCH_SHORT = "l"      
OPTION_PATH = "--path"          # 指定したパス下にプロジェクトディレクトリを作成
OPTION_PATH_SHORT = "-p"
OPTION_TEMP = "--temp"          # テンプレートファイルを指定
OPTION_TITLE = "--title"        # 文書のタイトル

COMMAND_START = "start"         # 指定したディレクトリを現在のプロジェクトディレクトリに変更する

COMMAND_FIGURE = "fig"          # 画像挿入時のテンプレートを生成, 引数は画像ファイル名
OPTION_WINDOW = "--window"      # テンプレートコードを別ウィンドウで表示
OPTION_WINDOW_SHORT = "-w"


# 環境変数に登録してあるパスから解析されるパス
PATH_ENV_BIN = [path for path in os.environ["PATH"].split(":") if re.search(PROJECT_NAME, path)]
PATH_ENV_RES = ""
PATH_ENV_DEFAULT_TEMPRATE = ""
PATH_ENV_HELP = ""
if len(PATH_ENV_BIN) == 1:
    PATH_ENV_RES = abspath(join(PATH_ENV_BIN[0], "..", "res"))
    PATH_ENV_DEFAULT_TEMPRATE = join(PATH_ENV_RES, "default.tex")
    PATH_ENV_HELP = join(PATH_ENV_RES, "help.txt")


# 固定のパス
PATH_MY_LTL = abspath(join(expanduser("~"), ".ltl"))
PATH_MY_SETTING = join(PATH_MY_LTL, "setting.json")
PATH_HELP = join(PATH_MY_LTL, "help.txt")
PATH_MY_TEMP = join(PATH_MY_LTL, "temp")
PATH_DEFAULT_TEMPRATE = join(PATH_MY_TEMP, "defualt.tex")

# プロジェクトのディレクトリ構成
DIR_SOURCE = "src"
DIR_FIGURE = "fig"
DIR_DATA = "data"


# setting.jsonの変数名
KEY_USER_NAME = "name"                      # ユーザー名，著者名に使う
KEY_CURRENT_PROJECT = "current_projct"      # 現在のプロジェクト，プロジェクトディレクトリのパスを取得するため
KEY_CURRENT_TEMP = "current_temp"           # 現在指定中のテンプレートファイル
KEY_TEMPS = "temps"                         # 設定してあるテンプレートファイルと登録名
KEY_DEFAULT_TEMP = "default"                # デフォルトのテンプレートの登録名


# エラー送出メッセージ
ERROR_INCORRECT_SYNTAX = "不正な引数が指定されました．使い方を調べるには 'ltl man' を実行してください．"
ERROR_REMOVE_DEFAULT_TEMP = "デフォルトテンプレートは削除出来ません．"

# その他定数
TEX_EXTENSION = ".tex"