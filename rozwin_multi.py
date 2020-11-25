import tkinter as tk

def sel():
    selection = "Wybrałeś wariant : " + str(wariant.get())
    #lbl_wybor.config(text = selection)
    lbl_wybor["text"] = selection
    # oba powyższe postawienia pod etykietę działają

def mnozenie():
    wynik_mnoz = float( ent_dana1.get() ) * float( ent_dana2.get() )
    #lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    lbl_wybor["text"] = f"{round(wynik_mnoz,2)}"

    
window = tk.Tk()
window.title("Rozwinięcia 2")

selection="START"

#Podział całego okna na 4 równe ramki
window.columnconfigure([0,1], minsize=300, weight=1 )
window.rowconfigure   ([0,1], minsize=300, weight=1 )

fr_dane    = tk.Frame(master=window, relief= tk.FLAT, borderwidth=2)
fr_obrazek = tk.Frame(master=window, relief= tk.GROOVE, borderwidth=2)
fr_wyniki  = tk.Frame(master=window, relief= tk.GROOVE, borderwidth=2)
fr_info    = tk.Frame(master=window, relief= tk.FLAT, borderwidth=2)

# Tworzę 4 podstawowe ramki
fr_dane.grid    (row=0, column=0, sticky="nsew")
fr_obrazek.grid (row=0, column=1, sticky="nsew")
fr_wyniki.grid  (row=1, column=0, sticky="nsew")
fr_info.grid    (row=1, column=1, sticky="nsew")

# Pierwszą ramkę podzielę na 2 podramki - Pole radio i pozostałe dane
fr_dane.columnconfigure(0, minsize=300,weight=1)
fr_dane.rowconfigure   (0, minsize=80,weight=1)
fr_dane.rowconfigure   (1, minsize=220,weight=1)

# Wygląd tych 2 podramek w ramce fr_dane
fr_dane_a = tk.Frame(master=fr_dane, relief= tk.GROOVE, borderwidth=2)
fr_dane_b = tk.Frame(master=fr_dane, relief= tk.GROOVE, borderwidth=2)

# Tworzę 2 podramki w ramce fr_dane
fr_dane_a.grid (row=0, column=0, sticky="nsew")
fr_dane_b.grid (row=1, column=0, sticky="nsew")

#-- Podramka fr_dane_a w Ramce fr_dane

# Pole Radio w ramce fr_dane i podramce fr_dane_a - wybór - Płaszcz, Króciec
wariant = tk.IntVar()

w1 = tk.Radiobutton(master=fr_dane_a, text="Rozwinięcie króćca",   justify = tk.LEFT, padx = 5, variable=wariant, value=1, command=sel)
w2 = tk.Radiobutton(master=fr_dane_a, text="Rozwinięcie płaszcza", justify = tk.LEFT, padx = 5, variable=wariant, value=2, command=sel)

w1.grid(row=0, column=0, sticky="w")
w2.grid(row=1, column=0, sticky="w")

#Etykieta pokazująca wynik wyboru pola Radio
lbl_wybor = tk.Label(master=fr_dane_a, text=selection)
lbl_wybor.grid(row=2, column=0, sticky="w")

#-- Koniec podramki frame_dane_a w Ramce fr_dane

#-- Podramka fr_dane_b w Ramce fr_dane
lbl_dana1 = tk.Label      (master=fr_dane_b, text="Dana 1 =")
ent_dana1 = tk.Entry      (master=fr_dane_b, width=10)
lbl_dana1_jedn = tk.Label (master=fr_dane_b, text="[mm]")

lbl_dana1.grid(row=0, column=0, sticky="w", padx=5, pady=5)
ent_dana1.grid(row=0, column=1, sticky="w")
lbl_dana1_jedn.grid(row=0, column=2, sticky="w", padx=5)

lbl_dana2 = tk.Label      (master=fr_dane_b, text="Dana 2 =")
ent_dana2 = tk.Entry      (master=fr_dane_b, width=10)
lbl_dana2_jedn = tk.Label (master=fr_dane_b, text="[mm]")

lbl_dana2.grid(row=1, column=0, sticky="e", padx=5, pady=5)
ent_dana2.grid(row=1, column=1, sticky="w")
lbl_dana2_jedn.grid(row=1, column=2, sticky="w", padx=5)

#-- Koniec podramki frame_dane_b w Ramce fr_dane


window.mainloop()