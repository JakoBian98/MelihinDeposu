from tkinter import messagebox
import pandas as pd
import requests
import tkinter as tk
API_KEY = "1a1315170c0b1a9bfe38c9893a4c9c65"
şehirler = ["İstanbul", "Ankara", "London", "Antalya", "Bursa", "Tokyo", "Sydney", "Dubai"]

df = pd.DataFrame(columns=[
    "Şehir", "Ülke", "Sıcaklık", "Hissedilen", "Min Sıcaklık", "Max Sıcaklık",
    "Nem", "Basınç", "Rüzgar", "Hava", "Açıklama"
])
def hava_durumu_getir():
    global df
    sehir = entry_sehir.get()
    if not sehir:
        messagebox.showwarning("Uyarı", "Lütfen bir şehir girin.")
        return
    url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={API_KEY}&units=metric&lang=tr"
    try:
        veri = requests.get(url).json()
        if veri.get("cod") != 200:
            messagebox.showerror("Hata", f"Şehir bulunamadı: {sehir}")
            return
        yeni_veri = pd.DataFrame([{
            "Şehir": veri["name"],
            "Ülke": veri["sys"]["country"],
            "Sıcaklık": veri["main"]["temp"],
            "Hissedilen": veri["main"]["feels_like"],
            "Min Sıcaklık": veri["main"]["temp_min"],
            "Max Sıcaklık": veri["main"]["temp_max"],
            "Nem": veri["main"]["humidity"],
            "Basınç": veri["main"]["pressure"],
            "Rüzgar": veri["wind"]["speed"],
            "Hava": veri["weather"][0]["main"],
            "Açıklama": veri["weather"][0]["description"]
        }])
        df = pd.concat([df, yeni_veri], ignore_index=True)
    except Exception as e:
        messagebox.showerror("Hata", f"Veri alınamadı: {e}")
def göster():
    global df
    pencere2 = tk.Toplevel()
    pencere2.title("Tüm Veriler")
    tk.Label(pencere2, text=df.to_string(), font=("Arial", 12)).pack()
def küçük():
    global df
    filtre = df.loc[df["Sıcaklık"] > 20]
    pencere2 = tk.Toplevel()
    pencere2.title("Sıcaklığı 20'den Büyük Olanlar")
    tk.Label(pencere2, text=filtre.to_string(), font=("Arial", 12)).pack(pady=10)
def küçük2():
    global df
    filtre = df.loc[df["Min Sıcaklık"] > 10]
    pencere2 = tk.Toplevel()
    pencere2.title("Min Sıcaklığı 10'dan Büyük Olanlar")
    tk.Label(pencere2, text=filtre.to_string(), font=("Arial", 14)).pack(pady=10)
def istatistik():
    global df
    istatistik_ = df.describe()
    pencere2 = tk.Toplevel()
    pencere2.title("İstatistikler")
    tk.Label(pencere2, text=istatistik_.to_string(), font=('Arial', 14)).pack(pady=10)
def ortalama1():
    global df
    ortalama = df.groupby("Ülke")["Sıcaklık"].mean()
    pencere2 = tk.Toplevel()
    pencere2.title("Sıcaklık Ortalaması")
    tk.Label(pencere2, text=ortalama.to_string(), font=('Arial', 14)).pack()
def ortalama2():
    global df
    ortalama = df.groupby("Ülke").agg({
        "Sıcaklık": "mean",
        "Nem": "mean",
        "Rüzgar": "mean"
    })
    pencere2 = tk.Toplevel()
    pencere2.title("Sıcaklık-Nem-Rüzgar Ort.")
    tk.Label(pencere2, text=ortalama.to_string(), font=('Arial', 14)).pack()
def ortalama3():
    global df
    ortalama = df.groupby("Ülke")["Sıcaklık"].std()
    pencere2 = tk.Toplevel()
    pencere2.title("Sıcaklık Standart Sapması")
    tk.Label(pencere2, text=ortalama.to_string(), font=('Arial', 14)).pack()
def ortalama4():
    global df
    ort = df.groupby("Ülke")[["Sıcaklık", "Nem", "Rüzgar"]].mean()
    pencere2 = tk.Toplevel()
    pencere2.title("Sıcaklık-Nem-Rüzgar Ortalama")
    tk.Label(pencere2, text=ort.to_string(), font=('Arial', 14)).pack()
def artan():
    global df
    artan_s = df.sort_values("Sıcaklık", ascending=True)
    pencere2 = tk.Toplevel()
    pencere2.title("Sıcaklık Artan")
    tk.Label(pencere2, text=artan_s.to_string(), font=('Arial', 15)).pack()
def azalan():
    global df
    azalan_s = df.sort_values("Sıcaklık", ascending=False)
    pencere2 = tk.Toplevel()
    pencere2.title("Sıcaklık Azalan")
    tk.Label(pencere2, text=azalan_s.to_string(), font=('Arial', 15)).pack()

pencere = tk.Tk()
pencere.title("Hava Durumu Menüsü")
entry_sehir = tk.Entry(pencere)
entry_sehir.pack()
tk.Button(pencere, text="Hava Durumu Getir", command=hava_durumu_getir).pack()
tk.Label(pencere, text="Tüm hava durumu verileri için tıklayınız").pack()
tk.Button(pencere, text="Tıkla", command=göster).pack()
tk.Label(pencere, text="Sıcaklığı 20'den büyük şehirler:").pack()
tk.Button(pencere, text="Tıkla", command=küçük).pack()
tk.Label(pencere, text="Min Sıcaklığı 10'dan büyük şehirler:").pack()
tk.Button(pencere, text="Tıkla", command=küçük2).pack()
tk.Label(pencere, text="Genel istatistikler:").pack()
tk.Button(pencere, text="Tıkla", command=istatistik).pack()
tk.Label(pencere, text="Sıcaklık Ortalamaları").pack()
tk.Button(pencere, text="Tıkla", command=ortalama1).pack()
tk.Label(pencere, text="Nem, Rüzgar, Sıcaklık Ortalamaları").pack()
tk.Button(pencere, text="Tıkla", command=ortalama2).pack()
tk.Label(pencere, text="Sıcaklık Standart Sapması").pack()
tk.Button(pencere, text="Tıkla", command=ortalama3).pack()
tk.Label(pencere, text="Sıcaklık Nem Rüzgar Ortalamaları").pack()
tk.Button(pencere, text="Tıkla", command=ortalama4).pack()
tk.Label(pencere, text="Artan Azalan Sıralama").pack()
tk.Button(pencere, text="Artan", command=artan).pack()
tk.Button(pencere, text="Azalan", command=azalan).pack()
pencere.mainloop()