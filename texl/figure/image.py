from texl.figure.tex_figure import TexFigure


class Image(TexFigure):
    
    def __init__(self, 
                 width,         # 画像の幅(cm)
                 path):         # 画像の絶対パス(latexecオブジェクトで渡す)
        super().__init__()
        self.width = width
        self.path = path
    
    def make(self):
        return "\\includegraphics[width={0}cm]{{{1}}}\n".format(self.width, self.path)