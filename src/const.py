import os
from os.path import join, abspath, dirname, expanduser


# コマンド名
COMMAND_TYPE = "command"

COMMAND_MANUAL = "man"          # マニュアルを表示
COMMAND_SETUP = "setup"           # セットアップ

COMMAND_SET_TEMP = "set"        # テンプレートファイルと別名をセット
                                # >> ltl set temp.tex report
                                #       # temp.texをreportという名前で登録

COMMAND_USE_TEMP = "use"        # 現在のテンプレートファイルをセット

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


# 固定のパス

PATH_MY_LTL = abspath(join(expanduser("~"), ".ltl"))
PATH_MY_SETTING = join(PATH_MY_LTL, "setting.json")
PATH_HELP = join(PATH_MY_LTL, "help.txt")
PATH_MY_TEMP = join(PATH_MY_LTL, "temp")
PATH_DEFAULT_TEMPRATE = join(PATH_MY_TEMP, "defualt.tex")

# プロジェクトのディレクトリ構成
DIR_SOURCE = "src"
DIR_FIGURE = "fig"
DIR_TABLE = "table"


# setting.jsonの変数名
KEY_USER_NAME = "name"                      # ユーザー名，著者名に使う
KEY_CURRENT_PROJECT = "current_projct"      # 現在のプロジェクト，プロジェクトディレクトリのパスを取得するため
KEY_CURRENT_TEMP = "current_temp"           # 現在指定中のテンプレートファイル
KEY_TEMPS = "temps"                         # 設定してあるテンプレートファイルと登録名
KEY_DEFAULT_TEMP = "default"                # デフォルトのテンプレートの登録名


# その他定数
TEX_EXTENSION = ".tex"