import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas
from tkinter import font as tkFont
import PIL
from PIL import ImageTk, Image, ImageDraw

# ==== Początek Grafika funkcje =====

# --- PIL
image1 = PIL.Image.new('RGB', (640, 480), 'white')
draw = ImageDraw.Draw(image1)

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    
tk.Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
    
tk.Canvas.create_circle_arc = _create_circle_arc

#--- funkcje do rysownania myszką 

def save():
    global image_number
    filename = f'image_{image_number}.png'   # image_number increments by 1 at every save
    image1.save(filename)
    image_number += 1


def activate_paint(e):
    global lastx, lasty
    canvas1.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    canvas1.create_line((lastx, lasty, x, y), width=1)
    #  --- PIL
    draw.line((lastx, lasty, x, y), fill='black', width=1)
    lastx, lasty = x, y
#--- Koniec - funkcje do rysownania myszką 

#--- Koniec Grafika funkcje ------

class dana_wiersz:

    def __init__(self, ramka, wiersz, nazwa, wartosc, jednostka):
        self.ramka  = ramka
        self.wiersz = wiersz
        self.nazwa  = nazwa
        self.wartosc = wartosc
        self.jednostka = jednostka
        self.lbl_nazwa     = tk.Label (master=self.ramka, font=msssrf10, text=self.nazwa)
        self.edt_wartosc   = tk.Entry (master=self.ramka, width=10, font=msssrf10)
        self.lbl_jednostka = tk.Label (master=self.ramka, text=self.jednostka, font=msssrf10)


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

# -------------- Obsługa przycisków Wyników ------------------------------------------    
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

# -------------- KONIEC - Obliczenia rozwinięcia -------------------------------------

window = tk.Tk()

#helv10 = tkFont.Font(family='Helvetica', size=11, weight='bold')
msssrf10 = tkFont.Font(family='MS Sans Serif', size=11, weight='bold')

window.title("Rozwinięcia 2")

selection="START"

#Podział całego okna na 4 równe ramki
window.columnconfigure([0,2], minsize=335, weight=1 )
window.rowconfigure   ([0,1], minsize=335, weight=1 )

fr_dane    = tk.Frame(master=window, relief= tk.FLAT, borderwidth=2)
fr_obrazek = tk.Frame(master=window, relief= tk.GROOVE, borderwidth=2)
fr_wyniki  = tk.Frame(master=window, relief= tk.GROOVE, borderwidth=2)
fr_info    = tk.Frame(master=window, relief= tk.FLAT, borderwidth=2)

fr_rys_proby = tk.Frame(master=window, relief= tk.GROOVE, borderwidth=2)

# Tworzę 4 podstawowe ramki
fr_dane.grid    (row=0, column=0, sticky="nsew")
fr_obrazek.grid (row=0, column=1, sticky="nsew")
fr_wyniki.grid  (row=1, column=0, sticky="nsew")
fr_info.grid    (row=1, column=1, sticky="nsew")

fr_rys_proby.grid    (row=0, column=2, sticky="nsew")

# Pierwszą ramkę podzielę na 2 podramki - Pole RADIO i pozostałe DANE
fr_dane.columnconfigure(0, minsize=335,weight=1)
fr_dane.rowconfigure   (0, minsize=80,weight=1)
fr_dane.rowconfigure   (1, minsize=220,weight=1)

# Wygląd tych 2 podramek w ramce fr_dane
fr_dane_a = tk.Frame(master=fr_dane, relief= tk.GROOVE, borderwidth=2)
fr_dane_b = tk.Frame(master=fr_dane, relief= tk.GROOVE, borderwidth=2)

# Tworzę 2 podramki w ramce fr_dane
fr_dane_a.grid (row=0, column=0, sticky="nsew")
fr_dane_b.grid (row=1, column=0, sticky="nsew")

# ---- podramka   fr_dane_a   w ramce   fr_dane   - zawartość

# Pole RADIO w ramce fr_dane i podramce fr_dane_a - wybór - Płaszcz, Króciec
wariant = tk.IntVar()

w1 = tk.Radiobutton(master=fr_dane_a, text="Rozwinięcie króćca"  , font=msssrf10, justify = tk.LEFT, padx = 5, variable=wariant, value=1, command=sel)
w2 = tk.Radiobutton(master=fr_dane_a, text="Rozwinięcie płaszcza", font=msssrf10, justify = tk.LEFT, padx = 5, variable=wariant, value=2, command=sel)

w1.grid(row=0, column=0, sticky="w")
w2.grid(row=1, column=0, sticky="w")

#Etykieta pokazująca wynik wyboru pola RADIO
lbl_wybor = tk.Label(master=fr_dane_a, text=selection)
lbl_wybor.grid(row=2, column=0, sticky="w")

# ---- Koniec podramki   frame_dane_a   w ramce   fr_dane

# ==== Początek podramka   fr_dane_b   w ramce   fr_dane   - zawartość DANE ===================

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
btn_licz  = tk.Button(fr_dane_b, font=msssrf10, text="Licz", width=10, height=1, command= licz )
btn_licz.grid  (row=8, column=3, sticky="nsew", padx = 10 )

#-- Koniec podramki frame_dane_b w ramce 1 -   fr_dane -----------------------------------


# ==== Początek ramka 2 - fr_obrazek ================
# ramka 2 fr_obrazek 
canvas = Canvas(fr_obrazek, width = 318, height = 330)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("dane_rura_rura.jpg"))  
canvas.create_image(2, 2, anchor="nw", image=img) 
# ---- koniec ramka 2 - fr_obrazek -------------------


# ==== Początek ramka 2a - fr_rys_proby ================
# ramka 2a fr_rys_proby 

# zmienne do rysowania myszką
lastx, lasty = None, None
image_number = 0

lastx, lasty = None, None
image_number = 0

canvas1 = Canvas(fr_rys_proby, width = 300, height = 300, bg='white')  
canvas1.grid  (row=0, column=0, sticky="nsew", padx = 15, pady = 2 )

canvas1.bind('<1>', activate_paint)
#canvas1.pack(expand=YES, fill=BOTH)

btn_save = tk.Button(master= fr_rys_proby, text="save", command=save)
#btn_save.pack()
btn_save.grid  (row=1, column=0, sticky="nsew", padx = 15, pady = 2 )




canvas1.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)
canvas1.create_circle_arc(100, 120, 48, fill="green", outline="", start=45, end=140)
canvas1.create_circle_arc(100, 120, 48, fill="green", outline="", start=275, end=305)
canvas1.create_circle_arc(100, 120, 45, style="arc", outline="white", width=6, start=270-25, end=270+25)
canvas1.create_circle(150, 40, 20, fill="#BBB", outline="")

canvas1.create_line((0, 0, 150, 200), width=3)

# ---- koniec ramka 2 - fr_obrazek -------------------



# ==== Początek podramek   fr_wyniki_a i fr_wyniki_b w   ramce   fr_wyniki  ==================
# Trzecią (WYNIKI - Lewy-Dolny Róg) ramkę podzielę na 2 podramki - Edytor i Button (potem może 4 buttony)
fr_wyniki.columnconfigure(0, minsize=335, weight=1)
fr_wyniki.rowconfigure   (0, minsize=245,weight=1)
fr_wyniki.rowconfigure   (1, minsize= 55,weight=1)

# Wygląd tych 2 podramek w ramce fr_wyniki
fr_wyniki_a = tk.Frame(master=fr_wyniki, relief= tk.GROOVE, borderwidth=2)
fr_wyniki_b = tk.Frame(master=fr_wyniki, relief= tk.GROOVE, borderwidth=2)

# Tworzę 2 podramki w ramce fr_wyniki
fr_wyniki_a.grid (row=0, column=0, sticky="nsew")
fr_wyniki_b.grid (row=1, column=0, sticky="nsew")

# -- podramka   fr_wyniki_a   w ramce   fr_wyniki --
# Pole Eytor w ramce fr_wyniki i podramce fr_wyniki_a

wyniki_edit = tk.Text(master=fr_wyniki_a, height=14, width=35)
wyniki_edit.grid(row=0, column=0, padx=4, pady=4, sticky="nsew")

# -- podramka   fr_wyniki_b   w ramce   fr_wyniki
# Btoony = przyciski w ramce fr_wyniki i podramce fr_wyniki_b

btn_zapisz_wyniki_txt  = tk.Button(fr_wyniki_b, text="Zapisz Wyniki = TXT", font=msssrf10, width=20, height=1, command= zapisz_wyniki_txt )
btn_zapisz_rysunek_dxf = tk.Button(fr_wyniki_b, text="Zapisz rysunek-DXF", font=msssrf10, width=20, height=1, command= zapisz_rysunek_dxf )
btn_drukuj_wyniki      = tk.Button(fr_wyniki_b, text="Drukuj Wyniki", font=msssrf10, width=20, height=1, command= drukuj_wyniki )
btn_zobacz_rysunek     = tk.Button(fr_wyniki_b, text="Zobacz Rysunek", font=msssrf10, width=20, height=1, command= zobacz_rysunek )

btn_zapisz_wyniki_txt.grid  (row=0, column=0, sticky="nsew")
btn_zapisz_rysunek_dxf.grid (row=0, column=1, sticky="nsew")
btn_drukuj_wyniki.grid      (row=1, column=0, sticky="nsew")
btn_zobacz_rysunek.grid     (row=1, column=1, sticky="nsew")

# ---- Koniec podramek    frame_wyniki_a i frame_wyniki_b    w ramce 3 -   fr_wyniki -------------------------

# ==== Początek ramka 2a - fr_rys_proby ====================

canvas = Canvas(fr_obrazek, width=318, height=330, bg='white')

# ---- Koniec ramki    fr_rys_proby   -------------------------

# ==== Początek ramka 4 - fr_info ====================
# dane g i ro w ramce fr_info
# g
dana_g = dana_wiersz_liczb_real   ( fr_info, 0, "g =", "10", "[mm]")
dana_g.wyswietl()

# ro
dana_ro = dana_wiersz_liczb_real   ( fr_info, 1, "ro =", "7860", "[kg/m3]")
dana_ro.wyswietl()

# ---- Koniec ramka 4 -   fr_info -------------------


window.mainloop()

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
  