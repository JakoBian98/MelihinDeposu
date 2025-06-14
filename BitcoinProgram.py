import tkinter as tk
from tkinter import messagebox
from binance.client import Client
import pandas as pd
from PIL import Image,ImageTk
import requests
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import time
from binance.exceptions import BinanceAPIException

client = Client(api_key="", api_secret="")

def göster():
    try:
        sembol = str(görüntüle.get())
        coin = client.get_symbol_ticker(symbol=sembol.upper())
        messagebox.showinfo("Sonuç", f"{sembol} Anlık Fiyat : {coin['price']}")
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
    except Exception as e:
        messagebox.showerror("HATA",f"{e}")
def en_yüksek():
   try:
       sembol = str(görüntüle.get())
       coin = client.get_ticker(symbol=sembol.upper())
       messagebox.showinfo("Sonuç",f"{sembol} 24 Saat En Yüksek : {coin['highPrice']}")
   except BinanceAPIException as e:
       messagebox.showerror("HATA",f"{e.message}")
   except ValueError:
       messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
   except ValueError:
       messagebox.showerror("HATA",f"{e}")
def en_düsük():
    try:
        sembol = str(görüntüle.get())
        coin = client.get_ticker(symbol=sembol.upper())
        messagebox.showinfo("Sonuç", f"24 Saate en düşük {coin['lowPrice']}")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")
def Hacim_Göster():
    try:
        sembol = str(görüntüle.get())
        coin = client.get_ticker(symbol=sembol.upper())
        messagebox.showinfo("Sonuç",f"{sembol} Anlık Hacim : {coin['volume']}")
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
    except Exception as e:
        messagebox.showerror("HATA",f"{e}")


def ortalama_fonksiyonları():
    def bes_dakikalık_ortalama():
        sembol = str(görüntüle.get())
        try:
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1MINUTE, limit=5)
            prices1 = [float(kline[4]) for kline in klines]
            avg_price = sum(prices1) / len(prices1)
            messagebox.showinfo("Sonuç", f"{sembol} 5 dakikalık ortalaması : {avg_price}")
        except:
            messagebox.showerror("Hata", "Bir hata oluştu")

    def onbeş_dakikalık_ortalama():
        sembol = str(görüntüle.get())
        try:
            klines = client.get_klines(symbol=sembol.upper(),interval="1m",limit=15)
            prices1 = [float(kline[4]) for kline in klines]
            avg_price = sum(prices1) / len(prices1)
            messagebox.showinfo("Sonuç",f"{sembol} 15 dakikalık ortalaması : {avg_price}")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def otuz_dakikalık_ortalama():
        try:
            sembol = str(görüntüle.get())
            klines = client.get_klines(symbol=sembol.upper(), interval="1m", limit=30)
            prices1 = [float(kline[4]) for kline in klines]
            avg_price = sum(prices1) / len(prices1)
            messagebox.showinfo("Sonuç", f"{sembol} 30 dakikalık ortalaması : {avg_price}")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def kırk_beş_dakikalık_ortalama():
        try:
            sembol = str(görüntüle.get())
            klines = client.get_klines(symbol=sembol.upper(),interval="1m",limit=45)
            prices1 = [float(kline[4]) for kline in klines]
            avg_price = sum(prices1) / len(prices1)
            messagebox.showinfo("Sonuç", f"{sembol} 45 dakikalık ortalaması : {avg_price}")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def ortalama_1_hour():
        try:
            sembol = str(görüntüle.get())
            klines = client.get_klines(symbol=sembol.upper(), interval="5m", limit=12)
            prices1 = [float(kline[4]) for kline in klines]
            avg_price = sum(prices1) / len(prices1)
            messagebox.showinfo("Sonuç", f"{sembol} 1 saatlik ortalaması : {avg_price}")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu : {e}")

    def ortalama_6_saat():
        try:
            sembol = str(görüntüle.get())
            klines = client.get_klines(symbol=sembol.upper(), interval="15m", limit=24)
            prices1 = [float(kline[4]) for kline in klines]
            avg_price = sum(prices1) / len(prices1)
            messagebox.showinfo("Sonuç", f"{sembol} 6 saatlik ortalaması : {avg_price}")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu : {e}")

    def ortalama_12_saat():
        try:
            sembol = str(görüntüle.get())
            klines = client.get_klines(symbol=sembol.upper(), interval="1h", limit=12)
            prices1 = [float(kline[4]) for kline in klines]
            avg_price = sum(prices1) / len(prices1)
            messagebox.showinfo("Sonuç", f"{sembol} 12 saatlik ortalaması : {avg_price}")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu : {e}")

    def ortalama_1_day():
        try:
            sembol = str(görüntüle.get())
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1HOUR, limit=24)
            prices1 = [float(kline[4]) for kline in klines]
            avg_price = sum(prices1) / len(prices1)
            messagebox.showinfo("Sonuç", f"{sembol} 1 günlük ortalaması : {avg_price}")
        except Exception as e:
            messagebox.showerror("Hata", f"{e}")

    def ortalama_1_hafta():
        try:
            sembol = str(görüntüle.get())
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_12HOUR, limit=14)
            prices1 = [float(kline[4]) for kline in klines]
            avg_price = sum(prices1) / len(prices1)
            messagebox.showinfo("Sonuç", f"{sembol} 1 haftalık ortalaması : {avg_price}")
        except Exception as e:
            messagebox.showerror("Hata", f"{e}")

    def ortalama_2_hafta():
        try:
            sembol = str(görüntüle.get())
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_12HOUR, limit=28)
            prices1 = [float(kline[4]) for kline in klines]
            avg_price = sum(prices1) / len(prices1)
            messagebox.showinfo("Sonuç", f"{sembol} 2 haftalık ortalaması : {avg_price}")
        except Exception as e:
            messagebox.showerror("Hata", f"{e}")
    def ortalama_3_hafta():
        try:
            sembol = str(görüntüle.get())
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_12HOUR, limit=42)
            prices1 = [float(kline[4]) for kline in klines]
            avg_price = sum(prices1) / len(prices1)
            messagebox.showinfo("Sonuç", f"{sembol} 3 haftalık ortalaması : {avg_price}")
        except Exception as e:
            messagebox.showerror("Hata", f"{e}")
    def bir_ay_ort():
        try:
                sembol = görüntüle.get()
                klines = client.get_klines(symbol=sembol.upper(), interval="1d", limit=30)
                prices1 = [float(kline[4]) for kline in klines]
                avg_price = sum(prices1) / len(prices1)
                messagebox.showinfo("Sonuç", f"1 Aylık ortalama {avg_price}")
        except Exception as e:
                messagebox.showerror("Hata", f"{e}")

    çerçeve = tk.Toplevel(pencere)
    çerçeve.title("Ortalama Fonksiyonları Menüsü")

    tk.Label(çerçeve,text="Ortalamasını görüntülemek istediğiniz coini aşağıya yazın").pack()
    görüntüle = tk.Entry(çerçeve)
    görüntüle.pack()

    gir_width = 25
    gir_height = 1

    tk.Button(çerçeve,text="5 dakikalık ortalama",command=bes_dakikalık_ortalama,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="15 dakikalık ortalama",command=onbeş_dakikalık_ortalama,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="30 Dakikalık ortalama",command=otuz_dakikalık_ortalama,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="45 Dakikalık ortalama",command=kırk_beş_dakikalık_ortalama,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="1 Saatlik ortalama",command=ortalama_1_hour,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="6 Saatlik ortalama",command=ortalama_6_saat,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="12 Saatlik ortalama",command=ortalama_12_saat,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="1 günlük ortalama",command=ortalama_1_day,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="1 haftalık ortalama",command=ortalama_1_hafta,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="2 Haftalık ortalama",command=ortalama_2_hafta,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="3 Haftalık ortalama",command=ortalama_3_hafta,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="1 Aylık ortalama",command=bir_ay_ort,width=gir_width,height=gir_height).pack()

    çerçeve.transient(pencere)
    çerçeve.grab_set()
    çerçeve.focus_force()

def coin_göser():
    try:
        root = tk.Toplevel(pencere)
        root.title("Görüntüleme menüsü")
        img_path = "C:/Users/Mehtap Aysan/Downloads/grafik-yl9l_cover.jpg"
        img = Image.open(img_path)
        ekran_genişliği = root.winfo_screenwidth()
        ekran_yüksekliği = root.winfo_screenheight()
        img = img.resize((ekran_genişliği, ekran_yüksekliği), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(img)

        background_label = tk.Label(root, image=bg_image)
        background_label.image = bg_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        btc = client.get_symbol_ticker(symbol="BTCUSDT")
        eth = client.get_symbol_ticker(symbol="ETHUSDT")
        xrp = client.get_symbol_ticker(symbol="XRPUSDT")
        doge = client.get_symbol_ticker(symbol="DOGEUSDT")
        solana = client.get_symbol_ticker(symbol="SOLUSDT")
        bnb = client.get_symbol_ticker(symbol="BNBUSDT")
        ada = client.get_symbol_ticker(symbol="ADAUSDT")
        avax = client.get_symbol_ticker(symbol="AVAXUSDT")
        pepe = client.get_symbol_ticker(symbol="PEPEUSDT")
        SUI = client.get_symbol_ticker(symbol="SUIUSDT")
        shıba = client.get_symbol_ticker(symbol="SHIBUSDT")
        ltc = client.get_symbol_ticker(symbol="LTCUSDT")
        chaınlınk = client.get_symbol_ticker(symbol="LINKUSDT")
        bonk = client.get_symbol_ticker(symbol="BONKUSDT")
        loki = client.get_symbol_ticker(symbol="FLOKIUSDT")
        hype = client.get_symbol_ticker(symbol="HYPERUSDT")
        aave = client.get_symbol_ticker(symbol="AAVEUSDT")
        ghst = client.get_symbol_ticker(symbol="GHSTUSDT")
        apt = client.get_symbol_ticker(symbol="APTUSDT")
        etc = client.get_symbol_ticker(symbol="ETCUSDT")
        arb = client.get_symbol_ticker(symbol="ARBUSDT")
        jup = client.get_symbol_ticker(symbol="JUPUSDT")
        tk.Label(root, text=f"APT : {apt['price']} USDT", fg="white", bg="black", font=('Arial', 20)).place(x=100, y=30)
        tk.Label(root, text=f"ETC : {etc['price']} USDT", fg="white", bg="black", font=('Arial', 20)).place(x=800, y=30)
        tk.Label(root, text=f"BTC : {btc['price']} USDT", fg="white", bg="black", font=("Arial", 20)).place(x=100,
                                                                                                            y=100)
        tk.Label(root, text=f"ETH : {eth['price']} USDT", fg="white", bg="black", font=("Arial", 20)).place(x=800,
                                                                                                            y=100)
        tk.Label(root, text=f"XRP : {xrp['price']} USDT", fg="white", bg="black", font=("Arial", 20)).place(x=100,
                                                                                                            y=170)
        tk.Label(root, text=f"DOGE : {doge['price']} USDT", fg="white", bg="black", font=("Arial", 20)).place(x=800,
                                                                                                              y=170)
        tk.Label(root, text=f"Solana {solana['price']} USDT", fg="white", bg="black", font=("Arial", 20)).place(
            x=100, y=240)
        tk.Label(root, text=f"BNB : {bnb['price']} USDT", fg="white", bg="black", font=("Arial", 20)).place(x=800,
                                                                                                            y=240)
        tk.Label(root, text=f"ADA : {ada['price']} USDT", fg="white", bg="black", font=("Arial", 20)).place(x=100,
                                                                                                            y=310)
        tk.Label(root, text=f"AVAX : {avax['price']} USDT", fg="white", bg="black", font=("Arial", 20)).place(x=800,
                                                                                                              y=310)
        tk.Label(root, text=f"PEPE : {pepe['price']} USDT", fg="white", bg="black", font=("Arial", 20)).place(x=100,
                                                                                                              y=380)
        tk.Label(root, text=f"SUI : {SUI['price']} USDT", fg="white", bg="black", font=("Arial", 20)).place(x=800,
                                                                                                            y=380)
        tk.Label(root, text=f"SHIBA : {shıba['price']}USDT", fg="white", bg="black", font=("Arial", 20)).place(x=100,
                                                                                                               y=450)
        tk.Label(root, text=f"LITECOİN : {ltc['price']} USDT", fg="white", bg="black", font=("Arial", 20)).place(
            x=800, y=450)
        tk.Label(root, text=f"CHAINLIK : {chaınlınk['price']} USDT", fg="white", bg="black",
                 font=("Arial", 20)).place(x=100, y=520)

        tk.Label(root, text=f"BONK : {bonk['price']} USDT", fg="white", bg="black", font=('Arial', 20)).place(x=800,
                                                                                                              y=520)
        tk.Label(root, text=f"FLOKI : {loki['price']} USDT", fg="white", bg="black", font=('Arial', 20)).place(x=100,
                                                                                                               y=590)
        tk.Label(root, text=f"HYPE : {hype['price']} USDT", fg="white", bg="black", font=('Arial', 20)).place(x=800,
                                                                                                              y=590)
        tk.Label(root, text=f"AAVE : {aave['price']} USDT", fg="white", bg="black", font=('Arial', 20)).place(x=100,
                                                                                                              y=660)
        tk.Label(root, text=f"GHST : {ghst['price']} USDT", fg="white", bg="black", font=('Arial', 20)).place(x=800,
                                                                                                              y=660)
        tk.Label(root, text=f"ARB : {arb['price']} USDT", fg="white", bg="black", font=('Arial', 20)).place(x=100,
                                                                                                            y=730)
        tk.Label(root, text=f"JUP: {jup['price']} USDT", fg="white", bg="black", font=('Arial', 20)).place(x=800, y=730)
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
    except Exception as e:
        messagebox.showerror("HATA",f"{e}")

def ath_göster():
    try:
        sembol = str(görüntüle.get())
        klines = client.get_historical_klines(
            symbol=sembol,
            interval=Client.KLINE_INTERVAL_1DAY,
            start_str="1 January 2017"
        )
        zirve = [float(k[2]) for k in klines]
        ath = max(zirve)
        messagebox.showinfo("Sonuç", f"{sembol} Tüm zamanlar en yüksek (ATH): {ath}")
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
    except Exception as e:
        messagebox.showerror("HATA", f"{e}")
def atl_göster():
    try:
        sembol = str(görüntüle.get())
        klines = client.get_historical_klines(symbol=sembol,interval=client.KLINE_INTERVAL_1DAY,start_str="1 January2017")
        dip = [float(kline[3]) for kline in klines]
        atl = min(dip)
        messagebox.showinfo("Sonuç",f"Tüm Zamanlar En Düşük (ATL) : : {atl}")
    except Exception as e:
        messagebox.showerror("HATA",f"{e}")

def değişim_fonksiyonları():
    çerçeve = tk.Toplevel(pencere)
    çerçeve.title("Değişim Fonksiyonları menüsü")

    def değişim_5_dakika():
        try:
            sembol = str(görüntüle.get())
            kline_5dk = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1MINUTE, limit=5)
            ilk_5dk = float(kline_5dk[0][4])
            son_5dk = float(kline_5dk[-1][4])
            değişim_5dk = ((son_5dk - ilk_5dk) / ilk_5dk) * 100
            messagebox.showinfo("Sonuç", f"{sembol} 5 dakikalık değişimi %{değişim_5dk}")
        except Exception as e:
            messagebox.showerror("Hata", f"{e}")

    def değişim_15_dakika():
        try:
            sembol = str(görüntüle.get())
            kline_15_dakika = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_15MINUTE, limit=2)
            ilk_15_dk = [float(kline_15_dakika[0][4])]
            son_15_dk = [float(kline_15_dakika[-1][-4])]
            değişim_15dk = ((son_15_dk) - ilk_15_dk) * 100
            messagebox.showinfo("Sonuç", f"15 Dakikalık değişim {değişim_15dk}")
        except Exception as e:
            messagebox.showerror("Hata", f"{e}")

    def değişim_bir_saat():
        try:
            sembol = str(görüntüle.get())
            kline1saat = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1HOUR, limit=2)
            ilk_1saat = float(kline1saat[0][1])
            son_1saat = float(kline1saat[-1][4])
            değişim_1saat = ((son_1saat - ilk_1saat) / ilk_1saat) * 100
            messagebox.showinfo("Sonuç", f"{sembol} 1 saatlik değişimi %{değişim_1saat}")
        except Exception as e:
            messagebox.showerror("Hata", f"{e}")

    def değişim_30_dakika():
        try:
            sembol = str(görüntüle.get())
            kline_30_dk = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_30MINUTE, limit=2)
            ilk_30_dk = float(kline_30_dk[0][4])
            son_30_dk = float(kline_30_dk[0][1])
            değişim_30_dk=((son_30_dk - ilk_30_dk) / ilk_30_dk) * 100
            messagebox.showinfo("Sonuç", f"{sembol} 30 Dakikalık değişimi : %{değişim_30_dk}")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def değişim_2_saat():
        try:
            sembol = str(görüntüle.get())
            kline_2_saat = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_2HOUR, limit=2)
            ilk_2_saat = float(kline_2_saat[0][4])
            son_2_saat = float(kline_2_saat[-1][4])
            değişim_2_hour = ((son_2_saat - ilk_2_saat) / ilk_2_saat) * 100
            messagebox.showinfo("Sonuç", f"{sembol} 2 Saatlik değişim : %{değişim_2_hour}")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def değişim_4_saat():
        try:
            sembol = str(görüntüle.get())
            kline_4_saat = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_4HOUR, limit=2)
            ilk_4_saat = float(kline_4_saat[0][4])
            son_4_saat = float(kline_4_saat[-1][4])
            değişim_4_hour = ((son_4_saat - ilk_4_saat) / ilk_4_saat) * 100
            messagebox.showinfo("Sonuç", f"4 Saatlik değişim : %{değişim_4_hour}")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def değişim_6_saat():
        try:
            sembol = str(görüntüle.get())
            kline_6_saat = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_6HOUR, limit=2)
            ilk_6_saat = float(kline_6_saat[0][4])
            son_6_saat = float(kline_6_saat[-1][4])
            değişim_6_hour = ((son_6_saat - ilk_6_saat) / ilk_6_saat) * 100
            messagebox.showinfo("Sonuç", f"4 Saatlik değişim : %{değişim_6_hour}")
        except Exception as e:
            messagebox.showerror("Hata",f"{e}")

    def değişim_12_hr():
        try:
            sembol = str(görüntüle.get())
            kline_12_saat = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_12HOUR, limit=2)
            ilk_12_saat = float(kline_12_saat[0][4])
            son_12_saat = float(kline_12_saat[-1][4])
            değişim_12_hour = ((son_12_saat - ilk_12_saat) / ilk_12_saat) * 100
            messagebox.showinfo("Sonuç", f"{sembol} 12 Saatlik değişim : %{değişim_12_hour}")
        except Exception as e:
            messagebox.showerror("Hata",f"{e}")

    def değişim_bir_gün():
        try:
            sembol = str(görüntüle.get())
            kline_1gün = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1DAY, limit=2)
            ilk_gün = float(kline_1gün[0][4])
            son_gün = float(kline_1gün[-1][4])
            değişim_1gün = ((son_gün - ilk_gün) / ilk_gün) * 100
            messagebox.showinfo("Sonuç", f"{sembol} 1 günlük değişimi %{değişim_1gün}")
        except Exception as e:
            messagebox.showerror("Hata", f"{e}")

    def değişim_bir_hafta():
        try:
            sembol = str(görüntüle.get())
            kline1hafta = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1WEEK, limit=2)
            ilkhafta = float(kline1hafta[0][4])
            son_hafta = float(kline1hafta[-1][4])
            değişim1_hafta = ((son_hafta - ilkhafta) / ilkhafta) * 100
            messagebox.showinfo("Sonuç", f"{sembol} 1 haftalık değişimi %{değişim1_hafta}")
        except Exception as e:
            messagebox.showerror("Hata", f"{e}")

    def değişim_2_hafta():
        try:
            sembol = str(görüntüle.get())
            kline_2_hafta = client.get_klınes(symbol=sembol.upper(),interval=client.KLINE_INTERVAL_1WEEK,limit=3)
            ilk_2_hafta = float(kline_2_hafta[0][4])
            son_2_hafta = float(kline_2_hafta[-1][4])
            değişim_2_week = ((son_2_hafta - ilk_2_hafta) / ilk_2_hafta) * 100
            messagebox.showinfo("Sonuç",f"2 Haftalık değişim : {değişim_2_week}")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def değişim_3_hafta():
        try:
            sembol = str(görüntüle.get())
            kline_3_hafta = client.get_klines(symbol=sembol.upper(),interval=client.KLINE_INTERVAL_1WEEK,limit=4)
            ilk_3_hafta = float(kline_3_hafta[0][4])
            son_3_hafta = float(kline_3_hafta[-1][4])
            değişim_3_week = ((son_3_hafta - ilk_3_hafta) / ilk_3_hafta) * 100
            messagebox.showinfo("Sonuç",f"3 Haftalık değişim : {değişim_3_week}")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def değişim_1_month():
        try:
            sembol = str(görüntüle.get())
            kline1ay = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1MONTH, limit=2)
            ilk_ay = float(kline1ay[0][4])
            son_ay = float(kline1ay[-1][4])
            değişim1_ay = ((son_ay - ilk_ay) / ilk_ay) * 100
            messagebox.showinfo("Sonuç", f"1 aylık değişim %{değişim1_ay}")
        except:
            messagebox.showerror("Hata","Bir hata oluştu")

    tk.Label(çerçeve,text=f"Görüntülemek istediğiniz coini aşağıya yazın").pack()

    def değişim_1_yıl():
        try:
            sembol = str(görüntüle.get())
            kline_1_yıl = client.get_klines(symbol=sembol, interval=client.KLINE_INTERVAL_1MONTH, limit=13)
            ilk_yıl = float(kline_1_yıl[0][4])
            son_1_yıl = float(kline_1_yıl[-1][4])
            değişim_1_year = ((son_1_yıl - ilk_yıl) / ilk_yıl) * 100
            messagebox.showinfo("Sonuç", f"1 yıllık değişim : {değişim_1_year}")
        except Exception as e:
            messagebox.showerror("Hata",f"{e}")

    görüntüle = tk.Entry(çerçeve)
    görüntüle.pack()

    gir_width = 20
    gir_height = 1

    tk.Button(çerçeve, text="5 dakikalık değişim", command=değişim_5_dakika, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve, text="15 dakikalık değişim", command=değişim_15_dakika, width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="30 Dakikalık değişim",command=değişim_30_dakika,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve, text="1 Saatlik değişim", command=değişim_bir_saat, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve,text="2 Saatlik değişim",command=değişim_2_saat,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="4 Saatlik değişim",command=değişim_4_saat,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="6 Saatlik değişim",command=değişim_6_saat,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="12 Saatlik değişim",command=değişim_12_hr,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve, text="1 günlük değişim", command=değişim_bir_gün, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve, text="1 haftalık değişim", command=değişim_bir_hafta, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve,text="2 Haftalık değişim",command=değişim_2_hafta,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve, text="1 Aylık değişim", command=değişim_1_month, width=gir_width, height=gir_height).pack()

    çerçeve.transient(pencere)
    çerçeve.grab_set()
    çerçeve.focus_force()

def vadeli():
    try:
        sembol = str(görüntüle.get())
        fiyat_bilgi = client.futures_symbol_ticker(symbol=sembol.upper())
        fiyat = fiyat_bilgi['price']
        messagebox.showinfo("Sonuç", f"{sembol} vadeli fiyatı : {fiyat} USDT")
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA",f"Lütfen Geçerli Karakterler Kullanın")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")
def adil():
    try:
        sembol = str(görüntüle.get())
        mark_price = client.futures_mark_price(symbol=sembol.upper())
        messagebox.showinfo("Sonuç", f"Adil değer (Mark Price) : {mark_price['markPrice']} USDT")
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")
def fonlama():
    try:
        sembol = str(görüntüle.get())
        fonlama_oranı = client.futures_mark_price(symbol=sembol.upper())
        messagebox.showinfo("Sonuç", f"Son Fonlama Oranı : {fonlama_oranı['lastFundingRate']}")
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")

def piyasa_ortalama():
    try:
        tickers = client.get_ticker()
        price_changes = []
        for ticker in tickers:
            symbol = ticker['symbol']
            if symbol.endswith('USDT'):
                price_changes.append(float(ticker['priceChangePercent']))
        if price_changes:
            avg_change = sum(price_changes) / len(price_changes)
            messagebox.showinfo("Sonuç", f"Tüm coinlerin 24 saatlik ortalaması : {avg_change}")
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")





def genel_veriler():
    try:
        sembol = str(görüntüle.get())
        data = client.get_ticker(symbol=sembol.upper())

        istatistikler = {
            "Hacim": data['volume'],
            "Anlık": data['lastPrice'],
             "24 Saat En Yüksek": data['highPrice'],
            "24 Saat En Düşük": data['lowPrice'],
            "24 Saat Değişim %": data['priceChangePercent'],
        }


        çerçeve = tk.Toplevel(pencere)
        çerçeve.title("Genel İstatistikler")

        for başlık, değer in istatistikler.items():
            tk.Label(çerçeve, text=f"{başlık}: {değer}", font=('Arial', 14)).pack(anchor="w", padx=10, pady=2)
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
    except Exception as e:
        messagebox.showerror("Hata", f"{e}")

def depth_bids():
     try:
        sembol = str(görüntüle.get())
        derinlik = client.get_order_book(symbol=sembol.upper())

        alıslar = derinlik['bids']
        satıslar = derinlik['asks']

        en_yüksek = float(alıslar[0][0])
        en_yüksek_qty = float(alıslar[0][1])

        en_düsük_satıs = float(satıslar[0][0])
        en_düsük_satıs_qyt = float(satıslar[0][1])

        spread = en_düsük_satıs - en_yüksek

        alıslarx = [(float(f), float(m)) for f, m in alıslar]
        satıslarx = [(float(f), float(m)) for f, m in satıslar]

        vwap_alıs = sum(f * m for f, m in alıslarx) / sum(m for _, m in alıslarx)
        vwap_satıs = sum(f * m for f, m in satıslarx) / sum(m for _, m in satıslarx)

        alıslar_m = [(float(fiyat), float(miktar)) for fiyat, miktar in derinlik['bids']]
        satıslar_m = [(float(fiyat), float(miktar)) for fiyat, miktar in derinlik['asks']]

        alıs_hacmi = sum(fiyat * miktar for fiyat,miktar in alıslar_m)
        satıs_hacmi = sum(fiyat * miktar for fiyat,miktar in satıslar_m)

        sayfa = tk.Toplevel(pencere)
        sayfa.title("Derinlik Bilgisi")
        tk.Label(sayfa, text=f"En yüksek alış fiyatı : {en_yüksek} miktar : {en_yüksek_qty}",font=('Arial', 20)).pack()
        tk.Label(sayfa, text=f"En düşük satış fiyatı : {en_düsük_satıs} miktar : {en_düsük_satıs_qyt}",font=('Arial', 20)).pack()
        tk.Label(sayfa, text=f"Spread : {spread}", font=('Arial', 20)).pack()
        tk.Label(sayfa, text=f"Ortalama Alış (VWAP) : {vwap_alıs}", font=('Arial', 20)).pack()
        tk.Label(sayfa, text=f"Ortalama Satış (VWAP) : {vwap_satıs}", font=('Arial', 20)).pack()
        tk.Label(sayfa,text=f"Alış hacmi : {alıs_hacmi}",font=('Arial',20)).pack()
        tk.Label(sayfa,text=f"Satış hacmi : {satıs_hacmi}",font=('Arial',20)).pack()
     except BinanceAPIException as e:
         messagebox.showerror("HATA",f"{e.message}")
     except ValueError:
         messagebox.showerror("HATA",f"Lütfen Geçerli Karakterler Kullanınız")
     except Exception as e:
         messagebox.showerror("Hata",f"{e}")

def min_max_adım():
    try:
        sembol = str(görüntüle.get())
        bilgi = client.get_symbol_info(symbol=sembol.upper())
        min_qty = max_qty = step_size = ""
        for f in bilgi['filters']:
            if f['filterType'] == 'LOT_SIZE':
                min_qty = f['minQty']
                max_qty = f['maxQty']
                step_size = f['stepSize']
            elif f['filterType'] == 'MİN_NATİONAL':
                min_nat = f['minNational']
                break

        çerçeve = tk.Toplevel(pencere)
        çerçeve.title("Menü")
        tk.Label(çerçeve, text=f"Minimum hacim : {min_qty}", font=('Arial', 20)).pack()
        tk.Label(çerçeve, text=f"Maksimum hacim : {max_qty}", font=('Arial', 20)).pack()
        tk.Label(çerçeve, text=f"Adım Boyutu : {step_size}", font=('Arial', 20)).pack()
        tk.Label(çerçeve,text=f"Minimum işlem tutarı : {min_nat}",font=('Arial',20)).pack()

    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanınız")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")

def en_yüksek_sırala():
    try:
        çerçeve = tk.Toplevel(pencere)
        çerçeve.title("En çok artanlar")

        ekran_genişlik = çerçeve.winfo_screenwidth()
        ekran_yükseklik = çerçeve.winfo_screenheight()

        çerçeve.geometry(f"{ekran_genişlik}x{ekran_yükseklik}")
        çerçeve.resizable(False, False)

        resim_yolu = r"C:\Users\Mehtap Aysan\Downloads\grafik-17-1132x670.jpg"
        resim = Image.open(resim_yolu).resize((ekran_genişlik, ekran_yükseklik))
        çerçeve.arka_plan = ImageTk.PhotoImage(resim)
        resim_etiketi = tk.Label(çerçeve, image=çerçeve.arka_plan)
        resim_etiketi.place(x=0, y=0, relwidth=1, relheight=1)

        veriler = client.get_ticker()
        usdt_coinler = [v for v in veriler if v['symbol'].endswith('USDT')]
        sıralı = sorted(usdt_coinler, key=lambda x: float(x['priceChangePercent']), reverse=True)

        for i, coin in enumerate(sıralı[:19]):
            yazı = f"{i + 1}. {coin['symbol']} %{coin['priceChangePercent']} artış."
            tk.Label(
                çerçeve,
                text=yazı,
                font=('Arial', 18, 'bold'),
                fg="white",
                bg="black"
            ).place(x=30, y=30 + i * 40)
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
    except Exception as e:
        messagebox.showerror("HATA",f"{e}")



def en_çok_düşenler():
    try:
        çerçeve = tk.Toplevel(pencere)
        çerçeve.title("En çok düşenler")

        ekran_genişlik = çerçeve.winfo_screenwidth()
        ekran_yükseklik = çerçeve.winfo_screenheight()

        resim_yolu = r"C:\Users\Mehtap Aysan\Downloads\dusus.jpg"

        resim = Image.open(resim_yolu).resize((ekran_genişlik, ekran_yükseklik))
        çerçeve.arka_plan = ImageTk.PhotoImage(resim)
        resim_etiketi = tk.Label(çerçeve, image=çerçeve.arka_plan)
        resim_etiketi.place(x=0, y=0, relwidth=1, relheight=1)

        veriler = client.get_ticker()
        usdt_coinler = [v for v in veriler if v['symbol'].endswith('USDT')]
        sıralı = sorted(usdt_coinler, key=lambda x: float(x['priceChangePercent']), reverse=False)

        for i, coin in enumerate(sıralı[:19]):
            yazı = f"{i + 1}. {coin['symbol']} %{coin['priceChangePercent']} azalış."
            tk.Label(
                çerçeve,
                text=yazı,
                font=('Arial', 18, 'bold'),
                fg="white",
                bg="black"
            ).place(x=30, y=30 + i * 40)
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
    except Exception as e:
        messagebox.showerror("HATA",f"{e}")

def al_sat_sinyal_2():
    try:
        sembol = görüntüle.get()
        klines = client.get_klines(symbol=sembol, interval=client.KLINE_INTERVAL_1HOUR, limit=100)

        df = pd.DataFrame(klines, columns=[
            'open_time', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
        ])

        df["close"] = df["close"].astype(float)

        df["EMA-5"] = df["close"].ewm(span=5, adjust=False).mean()
        df["EMA-10"] = df["close"].ewm(span=10, adjust=False).mean()

        if df["EMA-5"].iloc[-1] > df["EMA-10"].iloc[-1]:
            messagebox.showinfo("DİKKAT", "ALIM SİNYALİ")
        elif df["EMA-5"].iloc[-1] < df["EMA-10"].iloc[-1]:
            messagebox.showwarning("DİKKAT", "SATIM SİNYALİ")
        else:
            messagebox.showwarning("DİKKAT", "BEKLE")
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
    except Exception as e:
        messagebox.showerror("HATA",f"{e}")

def pump_dump_dedektör():
    try:
        sembol = str(görüntüle.get())
        kline_5dk = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1MINUTE, limit=5)
        ilk_5dk = float(kline_5dk[0][1])
        son_5dk = float(kline_5dk[-1][4])
        değişim_5dk = ((son_5dk - ilk_5dk) / ilk_5dk) * 100

        if abs(değişim_5dk) >= 5:
            if değişim_5dk > 0:
                messagebox.showinfo("DİKKAT", f"PUMP TESPİT EDİLDİ . Değişim : %{değişim_5dk}")
            else:
                messagebox.showinfo("DİKKAT", f"DUMP TESPİT EDİLDİ . Değişim : %{değişim_5dk}")
        else:
            messagebox.showinfo(f"BİLGİ", "DUMP VEYA PUMP TESPİT EDİLMEDİ")
    except BinanceAPIException as e:
        messagebox.showerror("HATA",f"{e.message}")
    except ValueError:
        messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanınız")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")

def grafik_fonksiyonları():
    çerçeve = tk.Toplevel(pencere)
    çerçeve.title("Grafikler Menüsü")

    gir_width = 20
    gir_height = 1

    def grafik_24_saat():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("24 Saatlik Kripto Para değişim grafiği")
            grafik_pencere.geometry("800x600")

            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_5MINUTE, limit=288)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]

            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} - Son 24 Saatlik Kapanış Fiyatları")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)

            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_1_saat():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("1 Saatlik Grafik")
            grafik_pencere.geometry("800x600")

            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1MINUTE, limit=600)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="green")
            ax.set_title(f"{sembol} - 1 Saatlik Grafik")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)

            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_5_dakika():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("5 Dakikalık Grafik")
            grafik_pencere.geometry("800x600")

            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1SECOND, limit=300)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]

            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="red")
            ax.set_title(f"{sembol} - 5 Dakikalık Grafik")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)

            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_12_saat():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("12 Saatlik Grafik")
            grafik_pencere.geometry("800x600")
            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1MINUTE, limit=720)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 12 Saatlik Değişim Grafiği")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA",f"Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_6_saat():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("6 Saatlik Grafik")
            grafik_pencere.geometry("800x600")
            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1MINUTE, limit=360)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 6 Saatlik Değişim Grafiği")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_1_dakika():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("1 Dakikalık Grafik")
            grafik_pencere.geometry("800x600")
            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1SECOND, limit=60)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 1 Dakikalık Değişim Grafiği")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_15_dakika():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("15 Dakikalık Grafik")
            grafik_pencere.geometry("800x600")
            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1SECOND, limit=900)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 15 Dakikalık Fiyat Değişim Grafiği")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lüfen Geçerli Coinler Giriniz")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_30_dk():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("30 Dakikalık Grafik")
            grafik_pencere.geometry("800x600")
            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1MINUTE, limit=30)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="red")
            ax.set_title(f"{sembol} 30 Dakikalık Fiyat Değişim Grafiği")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_45_dakika():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("45 Dakikalık Değişim Grafiği")
            grafik_pencere.geometry("1000x800")
            sembol = str(görüntüle2.get()).upper()
            klines = client.get_klines(symbol=sembol, interval=client.KLINE_INTERVAL_1MINUTE, limit=45)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 45 Dakikalık Değişim Grafiği")
            ax.set_xlabel("Fiyat")
            ax.set_ylabel("Zaman")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_1_hafta():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("1 Haftalık Grafik")
            grafik_pencere.geometry("800x600")
            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_15MINUTE, limit=672)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 1 Haftalık Değişim Grafiği")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA",f"Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_2_hafta():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("1 Haftalık Grafik")
            grafik_pencere.geometry("800x600")
            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(),interval="8h",limit=1008)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 2 Haftalık Değişim Grafiği")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanınız")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_1_ay():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("1 Aylık Grafik")
            grafik_pencere.geometry("800x600")
            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1HOUR, limit=720)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 1 Aylık Değişim Grafiği")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_3_ay():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("3 Aylık Grafik")
            grafik_pencere.geometry("800x600")
            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(),interval=client.KLINE_INTERVAL_6HOUR, limit=360)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 3 Aylık Değişim Grafiği")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanınız")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_6_ay():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("6 Aylık Grafik")
            grafik_pencere.geometry("800x600")
            sembol = görüntüle2.get()
            klines = client.get_klines(symbol=sembol.upper(), interval="5h", limit=864)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 6 Aylık Değişim Grafiği")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanınız")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_9_ay():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("9 Aylık Kripto Para Görüntüleme Menüsü")
            sembol = str(görüntüle2.get()).upper()
            grafik_pencere.geometry("1000x600")
            klines = client.get_klines(symbol=sembol, interval="12h", limit=540)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 9 Aylık Fiyat Değişim Grafiği")
            ax.set_xlabel("Fiyatlar")
            ax.set_ylabel("Zaman")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as a:
            messagebox.showerror("HATA",f"{a.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_1_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("1 Yıllık Değişim Grafiği")
            grafik_pencere.geometry("100x600")

            sembol = str(görüntüle2.get())
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_12HOUR, limit=730)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar)
            ax.set_title(f"{sembol} 1 Yıllık Değişim Grafiği")
            ax.set_ylabel("Fiyatlar")
            ax.set_xlabel("Zaman")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerrror("HATA","Lütfen Geçerli Karakterler Kullanınız")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_5_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("5 Yıllık Değişim Grafiği")
            grafik_pencere.geometry("100x600")

            sembol = str(görüntüle2.get())
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_3DAY, limit=609)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 5 Yıllık Değişim Grafiği")
            ax.set_ylabel("Fiyat")
            ax.set_xlabel("Tarih")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanınız")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_2_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("2 Yıllık Değişim Grafiği")
            grafik_pencere.geometry("100x600")
            sembol = str(görüntüle2.get())
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1DAY, limit=730)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 2 Yıllık Değişim Grafiği")
            ax.set_ylabel("Fiyat")
            ax.set_xlabel("Tarih")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanınız")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")


    def grafik_3_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("3 Yıllık Değişim Grafiği")
            grafik_pencere.geometry("1000x600")
            sembol = str(görüntüle2.get())
            klines = client.get_klines(symbol=sembol.upper(), interval="2d", limit=547)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 3 Yıllık Değişim Grafiği")
            ax.set_ylabel("Fiyat")
            ax.set_xlabel("Tarih")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA","Lütfen Geçerli bir coin ismi giriniz")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler kullanınız")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_4_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("5 Yıllık Değişim Grafiği")
            grafik_pencere.geometry("100x600")
            sembol = str(görüntüle2.get())
            klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_3DAY, limit=487)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 4 Yıllık Değişim Grafiği")
            ax.set_ylabel("Fiyat")
            ax.set_xlabel("Tarih")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA",f"Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA", f"{e}")

    def grafik_6_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol = str(görüntüle2.get())
            klines = client.get_klines(symbol=sembol, interval=client.KLINE_INTERVAL_3DAY, limit=730)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="green")
            ax.set_title(f"{sembol} 6 Yıllık Fiyat Değişim Grafiği")
            ax.set_xlabel("Fiyat")
            ax.set_ylabel("Zaman")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_7_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol = str(görüntüle2.get())
            klines = client.get_klines(symbol=sembol, interval=client.KLINE_INTERVAL_3DAY, limit=852)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 7 Yıllık Değişim Grafiği")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_8_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol = str(görüntüle2.get()).upper()
            klines = client.get_klines(symbol=sembol, interval=client.KLINE_INTERVAL_3DAY, limit=973)
            zamanlar = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines]
            fiyatlar = [float(k[4]) for k in klines]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(zamanlar, fiyatlar, color="blue")
            ax.set_title(f"{sembol} 8 Yıllık Fiyat Değişim Grafiği")
            ax.set_xlabel("Zaman")
            ax.set_ylabel("Fiyat")
            ax.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exceptiaon as e:
            messagebox.showerror("HATA",f"{e}")


    tk.Label(çerçeve, text="Grafiğini görüntülemek istediğiniz coin'i girin").pack()
    görüntüle2 = tk.Entry(çerçeve)
    görüntüle2.pack()


    tk.Button(çerçeve, text="1 Dakikalık Grafik", command=grafik_1_dakika, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve, text="5 Dakikalık Grafik", command=grafik_5_dakika, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve, text="15 Dakikalık Grafik", command=grafik_15_dakika, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve, text="30 Dakikalık Grafik", command=grafik_30_dk, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve,text="45 Dakikalık Grafik",command=grafik_45_dakika,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve, text="1 Saatlik Grafik", command=grafik_1_saat, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve, text="6 Saatlik Grafik", command=grafik_6_saat, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve, text="12 Saatlik Grafik", command=grafik_12_saat, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve, text="24 Saatlik Grafik", command=grafik_24_saat, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve, text="1 Haftalık Grafik", command=grafik_1_hafta, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve,text="2 Haftalık Grafik",command=grafik_2_hafta,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve, text="1 Aylık Grafik", command=grafik_1_ay, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve, text="3 Aylık Grafik", command=grafik_3_ay, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve, text="6 Aylık Grafik", command=grafik_6_ay, width=gir_width, height=gir_height).pack()
    tk.Button(çerçeve,text="9 Aylık Grafik",command=grafik_9_ay,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="1 Yıllık Grafik",command=grafik_1_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="2 Yıllık Grafik",command=grafik_2_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="3 Yıllık Grafik",command=grafik_3_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="4 Yıllık Grafik",command=grafik_4_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="5 Yıllık Grafik",command=grafik_5_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="6 Yıllık Grafik",command=grafik_6_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="7 Yıllık Grafik",command=grafik_7_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="8 Yıllık Grafik",command=grafik_8_yıl,width=gir_width,height=gir_height).pack()

def çapraz_grafikler():
    çerçeve = tk.Toplevel(pencere)
    çerçeve.title("Çapraz Grafikler Penceresi")

    def grafik_çapraz_1_dakika():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get()).upper()
            sembol2 = str(görüntüle3.get()).upper()
            klines1 = client.get_klines(symbol=sembol1,interval=client.KLINE_INTERVAL_1SECOND,limit=60)
            klines2 = client.get_klines(symbol=sembol2,interval=client.KLINE_INTERVAL_1SECOND,limit=60)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.plot(zamanlar1,fiyatlar1,color="blue")
            ax1.set_ylabel(f"{sembol1} Fiyatı")
            ax1.tick_params(axis="y",color="green")
            ax2.plot(zamanlar2,fiyatlar2,color="green")
            ax2.set_ylabel(f"{sembol2} Fiyatı")
            ax2.tick_params(axis="y",color="blue")
            ax1.set_title(f"{sembol1}/{sembol2} 1 Dakikalık Fiyat Değişim Grafiği")
            ax1.set_xlabel("Zaman")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")



    def çapraz_5_dakika():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get()).upper()
            sembol2 = str(görüntüle3.get()).upper()
            klines1 = client.get_klines(symbol=sembol1, interval=client.KLINE_INTERVAL_1SECOND, limit=300)
            klines2 = client.get_klines(symbol=sembol2, interval=client.KLINE_INTERVAL_1SECOND, limit=300)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.plot(zamanlar1, fiyatlar1, color="blue")
            ax1.set_ylabel(f"{sembol1} Fiyatı")
            ax1.tick_params(axis="y", labelcolor="blue")
            ax2.plot(zamanlar2, fiyatlar2, color="green")
            ax1.set_ylabel(f"{sembol2} fiyatı")
            ax2.tick_params(axis="y", labelcolor="green")

            ax1.set_title(f"{sembol1}/{sembol2} 5 Dakikalık Fiyat Değişim Grafiği")
            ax1.set_xlabel("Zaman")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA", f"Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_çapraz_30_dakika():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get())
            sembol2 = str(görüntüle3.get())
            klines1 = client.get_klines(symbol=sembol1, interval=client.KLINE_INTERVAL_1MINUTE, limit=30)
            klines2 = client.get_klines(symbol=sembol2, interval=client.KLINE_INTERVAL_1MINUTE, limit=30)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.plot(zamanlar1, fiyatlar1, color="blue")
            ax1.set_ylabel(f"{sembol1} Fiyatı")
            ax1.tick_params(axis="y", labelcolor="blue")
            ax2.plot(zamanlar2, fiyatlar2, color="green")
            ax2.set_ylabel(f"{sembol2} Fiyatı")
            ax2.tick_params(axis="y", labelcolor="green")
            ax1.set_title(f"{sembol1}/{sembol2} 30 Dakikalık Fiyat Değişim Grafikleri")
            ax1.set_xlabel("Zaman")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")


    def çapraz_grafik_1_saat():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get()).upper()
            sembol2 = str(görüntüle3.get()).upper()
            klines1 = client.get_klines(symbol=sembol1, interval=client.KLINE_INTERVAL_1MINUTE, limit=60)
            klines2 = client.get_klines(symbol=sembol2, interval=client.KLINE_INTERVAL_1MINUTE, limit=60)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.plot(fiyatlar1, zamanlar1, color="blue", label=sembol1)
            ax2.plot(fiyatlar2, zamanlar2, color="green", label=sembol2)

            ax1.set_ylabel(f"{sembol1} Fiyatı", color="blue")
            ax1.tick_params(axis='y', labelcolor="blue")

            ax2.set_ylabel(f"{sembol2} Fiyatı", color="green")
            ax2.tick_params(axis="y", labelcolor="green")

            ax1.set_title(f"{sembol1}/{sembol2} 1 Saatlik Fiyat Karşılaştırması")
            ax1.set_xlabel("Zaman")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfern Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_çapraz_12_saat():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get()).upper()
            sembol2 = str(görüntüle3.get()).upper()
            klines1 = client.get_klines(symbol=sembol1, interval=client.KLINE_INTERVAL_1MINUTE, limit=720)
            klines2 = client.get_klines(symbol=sembol2, interval=client.KLINE_INTERVAL_1MINUTE, limit=720)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.plot(fiyatlar1, zamanlar1, color="blue")
            ax1.set_ylabel(f"{sembol1} Fiyatı")
            ax1.tick_params(axis="y", labelcolor="blue")
            ax2.plot(fiyatlar2, zamanlar2, color="green")
            ax2.set_ylabel(f"{sembol1}/{sembol2} Fiyatı")
            ax2.tick_params(axis="y", labelcolor="green")
            ax1.set_title(f"{sembol1}/{sembol2} Fiyatı")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")
    def grafik_çapraz_1_gün():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get()).upper()
            sembol2 = str(görüntüle3.get()).upper()
            klines1 = client.get_klines(symbol=sembol1, interval="5m", limit=480)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            klines2 = client.get_klines(symbol=sembol2, interval="5m", limit=480)
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)

            ax1.plot(zamanlar1, fiyatlar1, color="blue", label=sembol1)
            ax1.set_ylabel(f"{sembol1} Fiyatı", color="blue")
            ax1.tick_params(axis='y', labelcolor="blue")

            ax2 = ax1.twinx()

            ax2.plot(zamanlar2, fiyatlar2, color="green", label=sembol2)
            ax2.set_ylabel(f"{sembol2} Fiyatı", color="green")
            ax2.tick_params(axis='y', labelcolor="green")

            ax1.set_title(f"{sembol1} / {sembol2} Çapraz Grafik")
            ax1.set_xlabel("Zaman")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)

            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_çapraz_1_hafta():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.title("1 Haftalık Çapraz Grafik")
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get()).upper()
            sembol2 = str(görüntüle3.get()).upper()
            klines1 = client.get_klines(symbol=sembol1, interval="1h", limit=720)
            klines2 = client.get_klines(symbol=sembol2, interval="1h", limit=720)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()

            ax1.plot(zamanlar1, fiyatlar1, color="blue")
            ax2.plot(zamanlar2, fiyatlar2, color="green")

            ax1.set_title(f"{sembol1}/{sembol2} Fiyat Değişim Grafiği")
            ax1.set_xlabel("Fiyat")
            ax1.set_ylabel("Zaman")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")

    def grafik_çapraz_1_ay():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get()).upper()
            sembol2 = str(görüntüle3.get()).upper()
            klines1 = client.get_klines(symbol=sembol1, interval="1h", limit=730)
            klines2 = client.get_klines(symbol=sembol2, interval="1h", limit=730)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()

            ax1.plot(zamanlar1, fiyatlar1, color="blue", label=sembol1)
            ax1.set_ylabel(f"{sembol1} Fiyatı")
            ax1.tick_params(axis='y', labelcolor="blue")

            ax2.plot(zamanlar2, fiyatlar2, color="green", label=sembol2)
            ax2.set_ylabel(f"{sembol2} Fiyatı")
            ax2.tick_params(axis='y', labelcolor="green")

            ax1.set_title(f"{sembol1}/{sembol2} Fiyat Değişim Grafiği")
            ax1.set_xlabel("Zaman")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")

    def grafik_çapraz_6_ay():
            try:
                grafik_pencere = tk.Toplevel(çerçeve)
                grafik_pencere.geometry("1000x600")

                sembol1 = str(görüntüle2.get()).upper()
                sembol2 = str(görüntüle3.get()).upper()

                klines1 = client.get_klines(symbol=sembol1, interval="6h", limit=720)
                klines2 = client.get_klines(symbol=sembol2, interval="6h", limit=720)

                zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
                fiyatlar1 = [float(k[4]) for k in klines1]

                zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
                fiyatlar2 = [float(k[4]) for k in klines2]

                fig = Figure(figsize=(10, 5), dpi=100)
                ax1 = fig.add_subplot(111)
                ax2 = ax1.twinx()

                ax1.plot(zamanlar1, fiyatlar1, color="blue", label=sembol1)
                ax1.set_ylabel(f"{sembol1} Fiyatı", color="blue")
                ax1.tick_params(axis='y', labelcolor="blue")

                ax2.plot(zamanlar2, fiyatlar2, color="green", label=sembol2)
                ax2.set_ylabel(f"{sembol2} Fiyatı", color="green")
                ax2.tick_params(axis="y", labelcolor="green")

                ax1.set_title(f"{sembol1}/{sembol2} 6 Aylık Fiyat Karşılaştırması")
                ax1.set_xlabel("Zaman")
                ax1.grid(True)
                ax2.legend(loc="upper right")

                fig.autofmt_xdate(rotation=45)

                canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

            except BinanceAPIException as e:
                messagebox.showerror("HATA", f"{e.message}")

    def grafik_çapraz_1_yıl():
       try:
           grafik_pencere = tk.Toplevel(çerçeve)
           grafik_pencere.geometry("1000x600")
           sembol1 = str(görüntüle2.get()).upper()
           sembol2 = str(görüntüle3.get()).upper()
           klines1 = client.get_klines(symbol=sembol1, interval=client.KLINE_INTERVAL_12HOUR, limit=730)
           klines2 = client.get_klines(symbol=sembol2, interval=client.KLINE_INTERVAL_12HOUR, limit=730)
           zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
           fiyatlar1 = [float(k[4]) for k in klines1]
           zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
           fiyatlar2 = [float(k[4]) for k in klines2]
           fig = Figure(figsize=(10, 5), dpi=100)
           ax1 = fig.add_subplot(111)
           ax2 = ax1.twinx()

           ax1.plot(zamanlar1, fiyatlar1, color="blue", label=sembol1)
           ax1.set_ylabel(f"{sembol1} Fiyatı")
           ax1.tick_params(axis="y", labelcolor="blue")

           ax2.plot(zamanlar2, fiyatlar2, color="green", label=sembol2)
           ax2.set_ylabel(f"{sembol2} Fiyatı")
           ax2.tick_params(axis="y", labelcolor="green")

           ax1.set_title(f"{sembol1}/{sembol2} 1 Yıllık Fiyat Değişim Grafiği")
           ax1.set_xlabel("Zaman")
           ax1.grid(True)
           fig.autofmt_xdate(rotation=45)
           canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
           canvas.draw()
           canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
       except BinanceAPIException as e:
           messagebox.showerror("HATA",f"{e.message}")
       except ValueError:
           messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
       except Exception as e:
           messagebox.showerror("HATA",f"{e}")

    def çapraz_grafik_2_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get()).upper()
            sembol2 = str(görüntüle3.get()).upper()
            klines1 = client.get_klines(symbol=sembol1, interval=client.KLINE_INTERVAL_1DAY, limit=730)
            klines2 = client.get_klines(symbol=sembol2, interval=client.KLINE_INTERVAL_1DAY, limit=730)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()

            ax1.plot(zamanlar1, fiyatlar1, color="blue", label=sembol1)
            ax1.set_ylabel(f"{sembol1} Fiyatı")
            ax1.tick_params(axis="y", labelcolor="blue")

            ax2.plot(zamanlar2, fiyatlar2, color="green", label=sembol2)
            ax2.set_ylabel(f"{sembol2} Fiyatı")
            ax2.tick_params(axis="y", labelcolor="green")

            ax1.set_title(f"{sembol1}/{sembol2} 2 Yıllık Fiyat Değişim Grafikleri")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA",f"Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def çapraz_grafik_3_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get()).upper()
            sembol2 = str(görüntüle3.get()).upper()
            klines1 = client.get_klines(symbol=sembol1, interval=client.KLINE_INTERVAL_3DAY, limit=365)
            klines2 = client.get_klines(symbol=sembol2, interval=client.KLINE_INTERVAL_3DAY, limit=365)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()

            ax1.plot(zamanlar1, fiyatlar1, color="blue")
            ax1.set_ylabel(f"{sembol1} Fiyatı")
            ax1.tick_params(axis="y", labelcolor="blue")

            ax2.plot(zamanlar2, fiyatlar2, color="green")
            ax2.set_title(f"{sembol2} Fiyatı")
            ax2.tick_params(axis="y", labelcolor="green")

            ax1.set_title(f"{sembol1}/{sembol2} 3 Yıllık Fiyat Değişim Grafiği")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_çapraz_4_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get())
            sembol2 = str(görüntüle3.get())
            klines1 = client.get_klines(symbol=sembol1, interval=client.KLINE_INTERVAL_3DAY, limit=487)
            klines2 = client.get_klines(symbol=sembol2, interval=client.KLINE_INTERVAL_3DAY, limit=487)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.plot(zamanlar1, fiyatlar1, color="blue")
            ax1.set_ylabel(f"{sembol1} Fiyatı")
            ax1.tick_params(axis="y", labelcolor="blue")

            ax2.plot(zamanlar2, fiyatlar2, color="green")
            ax2.set_ylabel(f"{sembol2} Fiyatı")
            ax2.tick_params(axis="y", labelcolor="green")

            ax1.set_xlabel(f"{sembol1}/{sembol2} 4 Yıllık Değişim Grafikleri")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_çapraz_5_yıl():
       try:
           grafik_pencere = tk.Toplevel(çerçeve)
           grafik_pencere.title("5 Yıllık Kripto Para Penceresi")
           grafik_pencere.geometry("1000x600")
           sembol1 = str(görüntüle2.get()).upper()
           sembol2 = str(görüntüle3.get()).upper()
           klines1 = client.get_klines(symbol=sembol1, interval=client.KLINE_INTERVAL_3DAY, limit=609)
           klines2 = client.get_klines(symbol=sembol2, interval=client.KLINE_INTERVAL_3DAY, limit=609)
           zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
           fiyatlar1 = [float(k[4]) for k in klines1]
           zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
           fiyatlar2 = [float(k[4]) for k in klines2]
           fig = Figure(figsize=(10, 5), dpi=100)
           ax1 = fig.add_subplot(111)
           ax2 = ax1.twinx()

           ax1.plot(zamanlar1, fiyatlar1, color="blue")
           ax1.set_ylabel(f"{sembol1} Fiyatı")
           ax1.tick_params(axis="y", labelcolor="blue")

           ax2.plot(zamanlar2, fiyatlar2, color="green")
           ax2.set_ylabel(f"{sembol2} Fiyatı")
           ax2.tick_params(axis="y", labelcolor="green")

           ax1.set_title(f"{sembol1}/{sembol2} 5 Yıllık Değişim Grafiği")
           ax1.set_xlabel("Zaman")
           ax1.grid(True)
           fig.autofmt_xdate(rotation=45)
           canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
           canvas.draw()
           canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
       except BinanceAPIException as e:
           messagebox.showerror("HATA",f"{e.message}")
       except ValueError:
           messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
       except Exception as e:
           messagebox.showerror("HATA",f"{e}")

    def grafik_çapraz_6_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get()).upper()
            sembol2 = str(görüntüle3.get()).upper()
            klines1 = client.get_klines(symbol=sembol1, interval=client.KLINE_INTERVAL_3DAY, limit=730)
            klines2 = client.get_klines(symbol=sembol2, interval=client.KLINE_INTERVAL_3DAY, limit=730)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.plot(zamanlar1, fiyatlar1, color="blue")
            ax1.set_ylabel(f"{sembol1} Fiyatı ")
            ax1.tick_params(axis="y", labelcolor="blue")
            ax2.plot(zamanlar2, fiyatlar2, color="green")
            ax2.set_ylabel(f"{sembol2} Fiyatı")
            ax2.tick_params(axis="y", labelcolor="green")

            ax1.set_title(f"{sembol1}/{sembol2} 6 Yıllık Fiyat Değişimi Karşılaştırması")
            ax1.set_xlabel("Zaman")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_çapraz_7_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get()).upper()
            sembol2 = str(görüntüle3.get()).upper()
            klines1 = client.get_klines(symbol=sembol1, interval=client.KLINE_INTERVAL_3DAY, limit=852)
            klines2 = client.get_klines(symbol=sembol2, interval=client.KLINE_INTERVAL_3DAY, limit=852)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.plot(zamanlar1, fiyatlar1, color="blue")
            ax1.set_ylabel(f"{sembol1} Fiyatı")
            ax1.tick_params(axis="y", labelcolor="blue")

            ax2.plot(zamanlar2, fiyatlar2, color="green")
            ax2.set_ylabel(f"{sembol2} Fiyatı")
            ax2.tick_params(axis="y", labelcolor="green")

            ax1.set_title(f"{sembol1}/{sembol2} 7 Yıllık Fiyat Değişim Grafiği")
            ax1.set_xlabel(f"Zaman")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Doğru Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")

    def grafik_çapraz_8_yıl():
        try:
            grafik_pencere = tk.Toplevel(çerçeve)
            grafik_pencere.geometry("1000x600")
            sembol1 = str(görüntüle2.get()).upper()
            sembol2 = str(görüntüle3.get()).upper()
            klines1 = client.get_klines(symbol=sembol1, interval=client.KLINE_INTERVAL_3DAY, limit=974)
            klines2 = client.get_klines(symbol=sembol2, interval=client.KLINE_INTERVAL_3DAY, limit=974)
            zamanlar1 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines1]
            fiyatlar1 = [float(k[4]) for k in klines1]
            zamanlar2 = [datetime.fromtimestamp(int(k[0]) / 1000) for k in klines2]
            fiyatlar2 = [float(k[4]) for k in klines2]
            fig = Figure(figsize=(10, 5), dpi=100)
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()
            ax1.plot(zamanlar1, fiyatlar1, color="blue")
            ax1.set_ylabel(f"{sembol1} Fiyatı")
            ax1.tick_params(axis="y", labelcolor="blue")

            ax2.plot(zamanlar2, fiyatlar2, color="green")
            ax2.set_ylabel(f"{sembol2} Fiyatı")
            ax2.tick_params(axis="y", labelcolor="green")

            ax1.set_title(f"{sembol1}/{sembol2} 8 Yıllık Fiyat Değişim Grafiği")
            ax1.set_xlabel(f"Zaman")
            ax1.grid(True)
            fig.autofmt_xdate(rotation=45)
            canvas = FigureCanvasTkAgg(fig, master=grafik_pencere)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except BinanceAPIException as e:
            messagebox.showerror("HATA",f"{e.message}")
        except ValueError:
            messagebox.showerror("HATA","Lütfen Geçerli Karakterler Kullanın")
        except Exception as e:
            messagebox.showerror("HATA",f"{e}")




    tk.Label(çerçeve,text="Çapraz Grafiğini Görüntülemek istediğiniz iki coin i aşağıya ayrı ayrı girin").pack()
    görüntüle2 = tk.Entry(çerçeve)
    görüntüle2.pack()
    görüntüle3 = tk.Entry(çerçeve)
    görüntüle3.pack()

    gir_width = 10
    gir_height = 1
    tk.Button(çerçeve,text="1 Dakikalık",command=grafik_çapraz_1_dakika,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="5 Dakikalık",command=çapraz_5_dakika,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="30 Dakikalık",command=grafik_çapraz_30_dakika,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="1 Saatlik",command=çapraz_grafik_1_saat,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="12 Saatlik",command=grafik_çapraz_12_saat,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="1 Günlük",command=grafik_çapraz_1_gün,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="1 Hafta",command=grafik_çapraz_1_hafta,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="1 Aylık",command=grafik_çapraz_1_ay,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="6 Aylık",command=grafik_çapraz_6_ay,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="1 Yıllık",command=grafik_çapraz_1_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="2 Yıllık",command=çapraz_grafik_2_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="3 Yıllık",command=çapraz_grafik_3_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="4 Yıllık",command=grafik_çapraz_4_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="5 Yıllık",command=grafik_çapraz_5_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="6 Yıllık",command=grafik_çapraz_6_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="7 Yıllık",command=grafik_çapraz_7_yıl,width=gir_width,height=gir_height).pack()
    tk.Button(çerçeve,text="8 Yıllık",command=grafik_çapraz_8_yıl,width=gir_width,height=gir_height).pack()


pencere = tk.Tk()
pencere.title("Kripto Para menüsü")
screen_width = pencere.winfo_screenwidth()
screen_height = pencere.winfo_screenheight()

pencere.geometry(f"{screen_width}x{screen_height}+0+0")

original_image = Image.open("C:/Users/Mehtap Aysan/Downloads/grafik-1132x670.jpg")
resized_image = original_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(resized_image)

label = tk.Label(pencere, image=bg_photo)
label.place(x=0, y=0, width=screen_width, height=screen_height)

tk.Label(pencere, text="Görüntülemek istediğiniz kripto parayı yazın").pack()
görüntüle = tk.Entry(pencere)
görüntüle.pack()

gir_width = 20
gir_height=1

tk.Button(pencere, text="Anlık fiyat", command=göster,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="Çapraz Grafikler",command=çapraz_grafikler,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="Değişim Grafikleri",command=grafik_fonksiyonları,width=gir_width,height=gir_height).pack()
tk.Button(pencere, text="En yüksek", command=en_yüksek,width=gir_width,height=gir_height).pack()
tk.Button(pencere, text="En düşük", command=en_düsük,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="ATH Değeri",command=ath_göster,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="ATL Değeri",command=atl_göster,width=gir_width,height=gir_height).pack()
tk.Button(pencere, text="Hacim", command=Hacim_Göster,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="Ortalama Fonksiyonları",command=ortalama_fonksiyonları,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="Değişim Fonksiyonları",command=değişim_fonksiyonları,width=gir_width,height=gir_height).pack()
tk.Button(pencere, text="Tüm coinler", command=coin_göser,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="Vadeli işlemler fiyatı",command=vadeli,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="MarkPrice",command=adil,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="Son fonlama Oranı",command=fonlama,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="Tüm Piyasa ortalaması",command=piyasa_ortalama,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="Genel Veriler",command=genel_veriler,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="Derinlik bilgisi",command=depth_bids,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="Hacim(detaylı)",command=min_max_adım,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="En çok yükselenler",command=en_yüksek_sırala,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="En çok düşenler",command=en_çok_düşenler,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="Al-Sat Sinyal(EMA)",command=al_sat_sinyal_2,width=gir_width,height=gir_height).pack()
tk.Button(pencere,text="PUMP/DUMP DEDEKTÖRÜ",command=pump_dump_dedektör,width=gir_width,height=gir_height).pack()
pencere.mainloop()
