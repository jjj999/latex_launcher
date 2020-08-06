from texl.figure.tex_figure import TexFigure


class SubFigure(TexFigure):
    
    def make(self):
        framents = []
        framents.extend(["\\begin{subfigure}{0.8\columnwidth}", "\t\t\\centering"])
        framents.extend(["\t\t" + c.make() for c in self.contain])
        framents.extend(["\t\t\\caption{}", "\t\t\\label{fig:}", "\t\end{subfigure}\n"])
        return "\n".join(framents)