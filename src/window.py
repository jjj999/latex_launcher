import tkinter as tk


def pop_text_window(text):
    root = tk.Tk()
    root.title("ltl")
    root.geometry("600x600")

    text_widget = tk.Text(root)
    text_widget.grid(column=0, 
                     row=0,
                     sticky=(tk.N, tk.S, tk.E, tk.W))
    text_widget.insert("1.0", text)
    
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()
    
    
if __name__ == "__main__":
    from latexec import Latexec
    
    latex = Latexec()
    print(latex.fig(("penguin.png", "penguin2.png")))
    pop_text_window(latex.fig(("penguin.png", "penguin2.png")))