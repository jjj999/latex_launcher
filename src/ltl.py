import argparse

from const import *
from latexec import Latexec


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