import tkinter as tk
from tkinter import messagebox



class dana_wiersz:

    def __init__(self, ramka, wiersz, nazwa, wartosc, jednostka):
        self.ramka  = ramka
        self.wiersz = wiersz
        self.nazwa  = nazwa
        self.wartosc = wartosc
        self.jednostka = jednostka
        self.lbl_nazwa     = tk.Label (master=self.ramka, text=self.nazwa)
        self.edt_wartosc   = tk.Entry (master=self.ramka, width=10)
        self.lbl_jednostka = tk.Label (master=self.ramka, text=self.jednostka)


    def wyswietl(self):

        self.lbl_nazwa.grid     (row=self.wiersz, column=0, sticky="w", padx=5, pady=1)        
        self.edt_wartosc.grid   (row=self.wiersz, column=1, sticky="w")
        self.lbl_jednostka.grid (row=self.wiersz, column=2, sticky="w", padx=5)
       
        self.edt_wartosc.insert(0, self.wartosc) # czy to coś zmienia np. zmienną wartość


    def zwroc_dana(self):
#        tak też działa
#        self.wartosc = self.edt_wartosc.get()
#        return self.wartosc
         return self.edt_wartosc.get() 

class dana_wiersz_liczb_real(dana_wiersz):
    # przysłaniam metodę
    def zwroc_dana(self):
        a = self.edt_wartosc.get()
        
        # wyjątek
        try:
            a = float(a)
            #messagebox.showinfo(title="Info", message="To jest liczba FLOAT : " + str(a))
        except ValueError as e:
            messagebox.showinfo(title="Wyjatek", message="To NIE jest liczba FLOAT : " + str(a))
        finally:
            lbl_wybor["text"] = "Zwalniam zasób"
    
        a = float(a)

        return a
    

class dana_wiersz_liczb_int(dana_wiersz):
    # przysłaniam metodę
    def zwroc_dana(self):
        a = self.edt_wartosc.get()
        
        # wyjątek
        try:
            a = int(a)
            #messagebox.showinfo(title="Info", message="To jest liczba INT : " + str(a))
        except ValueError as e:
            messagebox.showinfo(title="Wyjatek", message="To NIE jest liczba INT : " + str(a))
        finally:
            lbl_wybor["text"] = "Zwalniam zasób"

        a = int(a)

        return a


def sel():
    selection = "Wybrałeś wariant : " + str(wariant.get())
    #lbl_wybor.config(text = selection)
    lbl_wybor["text"] = selection
    # oba powyższe postawienia pod etykietę działają

# -------------- Obsługa przycisków Wyników ----------------------------------------------    
def zapisz_wyniki_txt():
    lbl_wybor["text"] = "Wyniki do pliku TXT"

def zapisz_rysunek_dxf():
    lbl_wybor["text"] = "Zapisz rysunek-DXF"

def drukuj_wyniki():
    lbl_wybor["text"] = "Drukuj wyniki"

def zobacz_rysunek():
    lbl_wybor["text"] = "Zobacz Rysunek"

# -------------- Obliczenia rozwinięcia ----------------------------------------------    
def licz():
    tmp_lancuch = ""
    tmp1 = ""
    arr_obj_dane = [ dana_Dm, dana_Dd, dana_P, dana_Beta, dana_Alfa, dana_H, dana_Ld, dana_Lm, dana_N ]
    
    for x in arr_obj_dane:
        tmp1 = x.zwroc_dana()
        if ( (type( tmp1 ) == float) or (type( tmp1 ) == int) ) :
            tmp_lancuch = tmp_lancuch + " " + str(tmp1) + "flin"
        elif  (type( tmp1 ) == str):
            tmp_lancuch = tmp_lancuch + " " + tmp1 + "str"
        else:
            tmp_lancuch = tmp_lancuch + "Typ: inny" 
        
    lbl_wybor["text"] = tmp_lancuch

# -------------- KONIEC - Obliczenia rozwinięcia ----------------------------------------------

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

# Pierwszą ramkę podzielę na 2 podramki - Pole RADIO i pozostałe DANE
fr_dane.columnconfigure(0, minsize=300,weight=1)
fr_dane.rowconfigure   (0, minsize=80,weight=1)
fr_dane.rowconfigure   (1, minsize=220,weight=1)

# Wygląd tych 2 podramek w ramce fr_dane
fr_dane_a = tk.Frame(master=fr_dane, relief= tk.GROOVE, borderwidth=2)
fr_dane_b = tk.Frame(master=fr_dane, relief= tk.GROOVE, borderwidth=2)

# Tworzę 2 podramki w ramce fr_dane
fr_dane_a.grid (row=0, column=0, sticky="nsew")
fr_dane_b.grid (row=1, column=0, sticky="nsew")

#-- Podramka fr_dane_a w Ramce fr_dane - zawartość

# Pole RADIO w ramce fr_dane i podramce fr_dane_a - wybór - Płaszcz, Króciec
wariant = tk.IntVar()

w1 = tk.Radiobutton(master=fr_dane_a, text="Rozwinięcie króćca",   justify = tk.LEFT, padx = 5, variable=wariant, value=1, command=sel)
w2 = tk.Radiobutton(master=fr_dane_a, text="Rozwinięcie płaszcza", justify = tk.LEFT, padx = 5, variable=wariant, value=2, command=sel)

w1.grid(row=0, column=0, sticky="w")
w2.grid(row=1, column=0, sticky="w")

#Etykieta pokazująca wynik wyboru pola RADIO
lbl_wybor = tk.Label(master=fr_dane_a, text=selection)
lbl_wybor.grid(row=2, column=0, sticky="w")

#-- Koniec podramki frame_dane_a w Ramce fr_dane

#-- Podramka fr_dane_b w Ramce fr_dane - zawartość DANE

# Dm
dana_Dm = dana_wiersz_liczb_real  ( fr_dane_b, 0 , "Dm =", "300", "[mm]")
dana_Dm.wyswietl()
#lbl_wybor["text"] = dana_Dm.zwroc_dana()

# Dd
dana_Dd = dana_wiersz_liczb_real   ( fr_dane_b, 1 , "Dd =", "800", "[mm]")
dana_Dd.wyswietl()

# P
dana_P = dana_wiersz_liczb_real    ( fr_dane_b, 2 , "P =", "200", "[mm]")
dana_P.wyswietl()

#Beta
dana_Beta = dana_wiersz_liczb_real ( fr_dane_b, 3 , "BETA =", "90", "["+chr(176)+"]")
dana_Beta.wyswietl()

#Alfa
dana_Alfa = dana_wiersz_liczb_real ( fr_dane_b, 4 , "alfa =", "0", "["+chr(176)+"]")
dana_Alfa.wyswietl()

# H
dana_H = dana_wiersz_liczb_real    ( fr_dane_b, 5 , "H =", "700", "[mm]")
dana_H.wyswietl()

# Ld
dana_Ld = dana_wiersz_liczb_real   ( fr_dane_b, 6 , "Ld =", "1000", "[mm]")
dana_Ld.wyswietl()

# Lm
dana_Lm = dana_wiersz_liczb_real   ( fr_dane_b, 7 , "Lm =", "350", "[mm]")
dana_Lm.wyswietl()

# Lm
dana_N = dana_wiersz_liczb_int     ( fr_dane_b, 8 , "N =", "24", "[-]")
dana_N.wyswietl()

# Button - przycisk LICZ
btn_licz  = tk.Button(fr_dane_b, text="Licz", width=10, height=1, command= licz )
btn_licz.grid  (row=8, column=3, sticky="nsew", padx = 10 )

#-- Koniec podramki frame_dane_b w Ramce fr_dane

#-- Podramka fr_wyniki_a w Ramce fr_wyniki
# Trzecią (WYNIKI - Lewy-Dolny Róg) ramkę podzielę na 2 podramki - Edytor i Button (potem może 4 buttony)
fr_wyniki.columnconfigure(0, minsize=300, weight=1)
fr_wyniki.rowconfigure   (0, minsize=245,weight=1)
fr_wyniki.rowconfigure   (1, minsize= 55,weight=1)

# Wygląd tych 2 podramek w ramce fr_wyniki
fr_wyniki_a = tk.Frame(master=fr_wyniki, relief= tk.GROOVE, borderwidth=2)
fr_wyniki_b = tk.Frame(master=fr_wyniki, relief= tk.GROOVE, borderwidth=2)

# Tworzę 2 podramki w ramce fr_wyniki
fr_wyniki_a.grid (row=0, column=0, sticky="nsew")
fr_wyniki_b.grid (row=1, column=0, sticky="nsew")


#-- Podramka fr_wyniki_a w Ramce fr_wyniki cd.
# Pole Eytor w ramce fr_wyniki i podramce fr_wyniki_a

wyniki_edit = tk.Text(master=fr_wyniki_a, height=14, width=35)
wyniki_edit.grid(row=0, column=0, padx=4, pady=4, sticky="nsew")

#-- Podramka fr_wyniki_b w Ramce fr_wyniki
# Btoony = przyciski w ramce fr_wyniki i podramce fr_wyniki_b

btn_zapisz_wyniki_txt  = tk.Button(fr_wyniki_b, text="Zapisz Wyniki = TXT", width=20, height=1, command= zapisz_wyniki_txt )
btn_zapisz_rysunek_dxf = tk.Button(fr_wyniki_b, text="Zapisz rysunek-DXF", width=20, height=1, command= zapisz_rysunek_dxf )
btn_drukuj_wyniki      = tk.Button(fr_wyniki_b, text="Drukuj Wyniki", width=20, height=1, command= drukuj_wyniki )
btn_zobacz_rysunek     = tk.Button(fr_wyniki_b, text="Zobacz Rysunek", width=20, height=1, command= zobacz_rysunek )

btn_zapisz_wyniki_txt.grid  (row=0, column=0, sticky="nsew")
btn_zapisz_rysunek_dxf.grid (row=0, column=1, sticky="nsew")
btn_drukuj_wyniki.grid      (row=1, column=0, sticky="nsew")
btn_zobacz_rysunek.grid     (row=1, column=1, sticky="nsew")

#-- Koniec podramki frame_wyniki_b w Ramce fr_wyniki

window.mainloop()

"""
https://stackoverflow.com/questions/58119470/button-label-text-vs-textvariable

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tvar = tk.StringVar(value="Hi")

def swaptext():
    if tvar.get() == 'Hi':
        tvar.set('There')
    else:
        tvar.set('Hi')

my_button = ttk.Button(root, textvariable=tvar, command=swaptext)
my_button.pack()

root.mainloop()
"""




"""
def main():
    lbl_wybor["text"] = ent_Dm.get() # wyswietlam daną Dm - tekst

    
if __name__ == "__main__" :
    main()
"""

"""

  Dm := StrToFloat(rurarura.Edit_Dm.Text) ; Średnica rury mniejszej (króćca)
  Dd := StrToFloat(rurarura.Edit_Dd.Text) ; Średnica rury większej (płaszcza)
  P  := StrToFloat(rurarura.Edit_P.Text)  ; Przesunięcie osi rury mniejszej (króćca)
  Beta := StrToFloat(rurarura.Edit_Beta.Text)  ; Kąt pochylenia rury mniejszej (króćca) - np. dla kąta 45 stopni i 30 minut - wpisz 45.5
    OldBeta := Beta ; // zapamietuje Beta (do wydruku wyników) przed przeliczeniem na radiany
  Alfa := StrToFloat(rurarura.Edit_Alfa.Text)  ; Kąt umiejscowienia spawu na rurze mniejszej (na króćcu) - np. dla kąta 45 stopni i 30 minut - wpisz 45.5
  H  := StrToFloat(rurarura.Edit_H.Text)  ; Wysokość rury mniejszej (króćca)
  Ld := StrToFloat(rurarura.Edit_Ld.Text) ; Długość rury większej (płaszcza)
  Lm := StrToFloat(rurarura.Edit_Lm.Text) ; Odległość osi rury mniejszej (króćca) od początku rury większej (płaszcza)
  N  := StrToInt(rurarura.Edit_N.Text) ; Podział obwodu rozwinięcia na N odcinków

  g  := StrToFloat(rurarura.Edit_g.Text) ;
  ro := StrToFloat(rurarura.Edit_ro.Text) ;
"""  
# Próby
"""
dana_probna = dana_wiersz  ( fr_dane_b, 2 , "Dana probna jakas 1 =", "0.123", "[mm]")
dana_probna.wyswietl()
dana_probna2 = dana_wiersz ( fr_obrazek, 0 , "Dana probna jakas 2 =", "321,04163", "[mm]")
dana_probna2.wyswietl()
lbl_wybor["text"] = dana_probna2.zwroc_dana()
"""



"""
    lbl_wybor["text"] = dana_Dm.zwroc_dana() + " " + dana_Dd.zwroc_dana() + " " + dana_P.zwroc_dana() + " " + \
                        dana_Beta.zwroc_dana() + " " + dana_Alfa.zwroc_dana() + " " + dana_H.zwroc_dana() + " " + \
                        dana_Ld.zwroc_dana() + " " + dana_Lm.zwroc_dana() + " " + dana_N.zwroc_dana()
"""
#    lbl_wybor["text"] = dana_Dm.edt_wartosc.get() +"  " + dana_Dd.edt_wartosc.get() + " " + dana_P.edt_wartosc.get()
