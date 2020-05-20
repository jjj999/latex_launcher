

def isyes(s:str) -> bool:
    """文字列がyesを表すものか調べる．
    
    Parameters
    ----------
    s : str
        調べたい文字列．
        
    Returns
    -------
    bool
        yesを表す文字列ならTrueを返す．
    """
    
    if s in ("y", "Y", "yes", "YES", "Yes"):
        return True
    else:
        return False

def touch(path:str) -> None:
    """空のファイルを作成
    
    Parameters
    ----------
    path : str
        ファイルのパス
    """
    with open(f, "wt") as f:
        pass


def isinclude(child:str, parent:str) -> bool:
    """文字列が内部に含まれているか調べる．
    
    Parameters
    ----------
    child : str
        基準となる文字列．
    parent : str
        調べたい文字列．
    
    Returns
    -------
    bool
        parentにchildが含まれていればTrueを返す．
    """
    
    if parent.split(child)[0] == parent:
        return False
    else:
        return True


def set_header(tex:str, 
               title:str="", 
               author:str="", 
               fig:str="") -> None:
    """texファイルのタイトルと著者をセットする．
    
    Parameters
    ----------
    tex : str
        texファイルのパス．
    title : str, default ""
        セットしたいタイトル．
    author : str, default ""
        セットしたい著者名．
    fig : str, default ""
        画像ディレクトリのパス
        
    Notes
    -----
    * 適切に処理を行なうためにはtexファイルは
        "\\title{}"
        "\\author{}"
        "\\graphicspath{}"
      の空白のタグを持っている必要がある．
    """
    
    
    with open(tex, "rt") as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if isinclude("\\title{}", line) and title:
            lines[i] = "\\title{{{}}}\n".format(title)
        elif isinclude("\\author{}", line) and author:
            lines[i] = "\\author{{{}}}\n".format(author)
        elif isinclude("\\graphicspath{}", line) and fig:
            lines[i] = "\\graphicspath{{{{{}}}}}".format(fig)
            
    with open(tex, "wt") as f:
        f.writelines(lines)