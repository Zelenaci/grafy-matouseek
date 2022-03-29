import pylab as pl
import tkinter as tk

from pylab import linspace, pi, plot,sin,cos, show,grid,legend
from os.path import basename, splitext
from tkinter import *

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Grafy"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Grafy")
        self.lbl.pack()
        self.btnVypsat = tk.Button(self, text="Načíst ze souboru", command=self.zeSouboru)
        self.btnVypsat.pack()
        self.lbl3 = tk.Label(self, text="Frekvence")
        self.lbl3.pack()
        self.entryF  = tk.Entry(self)
        self.entryF.pack()
        self.lbl4 = tk.Label(self, text="Amplituda")
        self.lbl4.pack()
        self.entryA  = tk.Entry(self)
        self.entryA.pack()
        self.btnGraf = tk.Button(self, text="Načíst graf", command=self.graf)
        self.btnGraf.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

    def quit(self, event=None):
        super().quit()
    
    def graf(self):
        self.f = int(self.entryF.get())
        self.a = int(self.entryA.get())

        try:
            t = pl.linspace(1, 10 / self.f, self.f * 10000)
            x = self.a * (pl.cos(2 * pi * self.f * t))
        except ZeroDivisionError:
            print('takhle by to neslo klukoune, zadej tam tu frekvenci')

        pl.plot(t, x)
        pl.title("výkon")
        pl.xlabel("t[s]")
        pl.ylabel("u[V],i[A], p[W]")
        pl.show()

    def zeSouboru(self):
        f = open("soubor-win.txt", "r")
        x = []
        y = []
        while 1:
            radek = f.readline()
            if radek =="":
                break
            cisla = radek.split()
            x.append(float(cisla[0]))
            y.append(float(cisla[1]))
        f.close()
        pl.figure()
        pl.plot(x,y)
        pl.grid(True)
        pl.show()

app = Application()
app.mainloop()