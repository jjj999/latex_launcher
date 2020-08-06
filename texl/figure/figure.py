from texl.figure.tex_figure import TexFigure


class Figure(TexFigure):
    
    
    def make(self):
        fragments = ["\\begin{figure}", "\t\\centering\n"]
        fragments.extend(["\t" + c.make() for c in self.contain])
        fragments.extend(["\t\\caption{}", "\t\\label{fig:}", "\end{figure}"])
        return "\n".join(fragments)