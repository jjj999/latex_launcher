import argparse
import sys

from const import *
from util import *
from latexec import Latexec


if len(PATH_ENV_BIN) == 0:
    print("WARNING\n-------\n", 
          "環境変数にパスが登録されていません．利用するには，",
          "ダウンロードしたリポジトリ内の [win/unix]/bin/ ",
          "のパスを環境変数に登録してください．", sep="")
    sys.exit(-1)
    
elif len(PATH_ENV_BIN) > 1:
    print("WARNING\n-------\n",
          "環境変数内に latex_launcher を含むパスが複数存在します．",
          "正常に利用するためには，環境変数内に latex_launcher という",
          "文字列を含むパスを1つだけに限定してください．", sep="")
    
else:
    # 文字列に変更
    PATH_ENV_BIN = PATH_ENV_BIN[0]
    

class ArgumentError(Exception):
    """不正な引数が指定された時raise"""
    pass


parser = argparse.ArgumentParser()

parser.add_argument("command",
                    nargs="*",
                    help="指定されたコマンドを実行")

# -, --がついていれば自動的にオプション引数と判断する
parser.add_argument("-p",
                    "--path",
                    nargs="?",
                    default=None,
                    const=None,
                    help="プロジェクトのパス名")

parser.add_argument("--temp",
                    nargs="?",
                    default=None,
                    const=None,
                    help="テンプレートファイルの登録名")

parser.add_argument("--title",
                    nargs="?",
                    default="",
                    const="",
                    help="作成する文書のタイトル")

parser.add_argument("-w",
                    "--window",
                    action="store_true",
                    help="生成したテンプレートコードを別ウィンドウで表示")


# ここからが処理
args = parser.parse_args()
if len(args.command) == 0:
    raise ArgumentError("不正な引数が指定されました．使い方を調べるには 'ltl man' を実行してください．")

command = args.command[0]
num_args = len(args.command) - 1


if command == COMMAND_SETUP:
    Latexec.setup()

elif command == COMMAND_MANUAL:
    Latexec.man()

else:
    latex = Latexec()
    
    if command == COMMAND_SET_TEMP and num_args == 2:
        latex.set_temp(args.command[1], args.command[2])
        
    elif command == COMMAND_USE_TEMP and num_args == 1:
        latex.use(args.command[1])
        
    elif command in (COMMAND_LAUNCH, COMMAND_LAUNCH_SHORT) and num_args == 1:
        latex.launch(args.command[1], args.title, args.path, args.temp)
        
    elif command == COMMAND_FIGURE and num_args > 0:
        latex.fig(tuple(args.command[1:]), window=args.window)
        
    elif command == COMMAND_START and num_args == 1:
        latex.start(args.command[1])
        
    else:
        raise ArgumentError("不正な引数が指定されました．使い方を調べるには 'ltl man' を実行してください．")