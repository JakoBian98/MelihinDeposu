import tkinter as tk
from tkinter import messagebox
from binance.client import Client
client = Client(api_key="", api_secret="")
def göster():

   try:
       sembol = str(görüntüle.get())
       coin = client.get_symbol_ticker(symbol=sembol.upper())
       messagebox.showinfo("Sonuç ", f"1 {sembol} : {coin['price']} USDT")
   except:
       messagebox.showerror("Hata","Bir hata oluştu")
def en_yüksek():
   try:
       sembol = str(görüntüle.get())
       coin = client.get_ticker(symbol=sembol.upper())
       messagebox.showinfo("Sonuç", f"24 Saatte en yüksek : {coin['highPrice']}")
   except Exception as e:
       messagebox.showerror("Hata",f"{e}")
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
        messagebox.showinfo("Sonuç", f"24 Saatlik hacim : {coin['volume']} USDT")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")
def bes_dakikalık_ortalama():
    sembol = str(görüntüle.get())
    try:
        klines = client.get_klines(symbol=sembol.upper(),interval="5m",limit="1")
        prices1 = [float(kline[4]) for kline in klines]
        avg_price = sum(prices1) / len(prices1)
        messagebox.showinfo("Sonuç",f"{sembol} 5 dakikalık ortalaması : {avg_price}")
    except:
        messagebox.showerror("Hata","Bir hata oluştu")
def ortalama_1_hour():
    try:
        sembol = str(görüntüle.get())
        klines = client.get_klines(symbol=sembol.upper(),interval="5m",limit="12")
        prices1 = [float(kline[4]) for kline in klines]
        avg_price = sum(prices1) / len(prices1)
        messagebox.showinfo("Sonuç",f"{sembol} 1 saatlik ortalaması : {avg_price}")
    except Exception as e:
        messagebox.showerror("Hata",f"Bir hata oluştu : {e}")
def coin_göser():
    root = tk.Toplevel(pencere)
    root.title("Görüntüleme menüsü")
    btc = client.get_symbol_ticker(symbol="BTCUSDT")
    eth = client.get_symbol_ticker(symbol="ETHUSDT")
    xrp = client.get_symbol_ticker(symbol="XRPUSDT")
    doge = client.get_symbol_ticker(symbol="DOGEUSDT")
    solana = client.get_symbol_ticker(symbol="SOLUSDT")
    bnb = client.get_symbol_ticker(symbol="BNBUSDT")
    ada = client.get_symbol_ticker(symbol="ADAUSDT")
    avax = client.get_symbol_ticker(symbol="AVAXUSDT")
    pepe = client.get_symbol_ticker(symbol="PEPEUSDT")
    tk.Label(root, text=f" BTC : {btc['price']} USDT", font=('Arial', 20), anchor="w", justify="left").pack(padx=20,
                                                                                                            pady=10,
                                                                                                            fill="x")
    tk.Label(root, text=f" ETH : {eth['price']} USDT", font=('Arial', 20), anchor="w", justify="left").pack(padx=20,
                                                                                                            pady=10,
                                                                                                            fill="x")
    tk.Label(root, text=f" XRP : {xrp['price']} USDT", font=('Arial', 20), anchor="w", justify="left").pack(padx=20,
                                                                                                            pady=10,
                                                                                                            fill="x")
    tk.Label(root, text=f" DOGE : {doge['price']} USDT", font=('Arial', 20), anchor="w", justify="left").pack(padx=20,
                                                                                                              pady=10,
                                                                                                              fill="x")
    tk.Label(root, text=f" SOLANA : {solana['price']} USDT", font=('Arial', 20), anchor="w", justify="left").pack(
        padx=20, pady=10, fill="x")
    tk.Label(root, text=f" BNB : {bnb['price']} USDT", font=('Arial', 20), anchor="w", justify="left").pack(padx=20,
                                                                                                            pady=10,
                                                                                                            fill="x")
    tk.Label(root, text=f" ADA : {ada['price']} USDT", font=('Arial', 20), anchor="w", justify="left").pack(padx=20,
                                                                                                            pady=10,
                                                                                                            fill="x")
    tk.Label(root, text=f" AVAX : {avax['price']} USDT", font=('Arial', 20), anchor="w", justify="left").pack(padx=20,
                                                                                                              pady=10,
                                                                                                              fill="x")
    tk.Label(root, text=f"PEPE : {pepe['price']} USDT", font=('Arial', 20), anchor="w", justify="left").pack(padx=20,
                                                                                                           pady=10,
                                                                                                           fill="x")
def ortalama_1_day():
    try:
        sembol = str(görüntüle.get())
        klines = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1DAY, limit=1)
        prices1 = [float(kline[4]) for kline in klines]
        avg_price = sum(prices1) / len(prices1)
        messagebox.showinfo("Sonuç", f"{sembol} 1 günlük ortalaması : {avg_price}")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")
def değişim_5_dakika():
    try:
        sembol = str(görüntüle.get())
        kline_5dk = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1MINUTE, limit=5)
        ilk_5dk = float(kline_5dk[0][1])
        son_5dk = float(kline_5dk[-1][4])
        değişim_5dk = ((son_5dk - ilk_5dk) / ilk_5dk) * 100
        messagebox.showinfo("Sonuç", f"{sembol} 1 saatlik değişimi %{değişim_5dk}")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")
def değişim_bir_saat():
    try:
        sembol = str(görüntüle.get())
        kline1saat = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1HOUR, limit=1)
        ilk_1saat = float(kline1saat[0][1])
        son_1saat = float(kline1saat[-1][4])
        değişim_1saat = ((son_1saat - ilk_1saat) / ilk_1saat) * 100
        messagebox.showinfo("Sonuç", f"{sembol} 1 saatlik değişimi %{değişim_1saat}")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")
def değişim_bir_gün():
    try:
        sembol = str(görüntüle.get())
        kline_1gün = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1DAY, limit=1)
        ilk_gün = float(kline_1gün[0][1])
        son_gün = float(kline_1gün[-1][4])
        değişim_1gün = ((son_gün - ilk_gün) / ilk_gün) * 100
        messagebox.showinfo("Sonuç", f"{sembol} 1 günlük değişimi %{değişim_1gün}")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")
def değişim_bir_hafta():
    try:
        sembol = str(görüntüle.get())
        kline1hafta = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1WEEK, limit=1)
        ilkhafta = float(kline1hafta[0][1])
        son_hafta = float(kline1hafta[-1][4])
        değişim1_hafta = ((son_hafta - ilkhafta) / ilkhafta) * 100
        messagebox.showinfo("Sonuç", f"{sembol} 1 haftalık değişimi %{değişim1_hafta}")
    except Exception as e:
        messagebox.showerror("Hata", f"{e}")

def değişim_1_month():
    try:
        sembol = str(görüntüle.get())
        kline1ay = client.get_klines(symbol=sembol.upper(), interval=client.KLINE_INTERVAL_1MONTH, limit=1)
        ilk_ay = float(kline1ay[0][1])
        son_ay = float(kline1ay[-1][4])
        değişim1_ay = ((son_ay - ilk_ay) / ilk_ay) * 100
        messagebox.showinfo("Sonuç", f"1 aylık değişim %{değişim1_ay}")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")
def vadeli():
    try:
        sembol = str(görüntüle.get())
        fiyat_bilgi = client.futures_symbol_ticker(symbol=sembol.upper())
        fiyat = fiyat_bilgi['price']
        messagebox.showinfo("Sonuç", f"{sembol} vadeli fiyatı : {fiyat} USDT")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")
def adil():
    try:
        sembol = str(görüntüle.get())
        mark_price = client.futures_mark_price(symbol=sembol.upper())
        messagebox.showinfo("Sonuç", f"Adil değer (Mark Price) : {mark_price['markPrice']} USDT")
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")
def fonlama():
    try:
        sembol = str(görüntüle.get())
        fonlama_oranı = client.futures_mark_price(symbol=sembol)
        messagebox.showinfo("Sonuç", f"Son Fonlama Oranı : {fonlama_oranı['lastFundingRate']}")
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
    except Exception as e:
        messagebox.showerror("Hata",f"{e}")

def bir_ay_ort():
    try:
        sembol = görüntüle.get()
        klines = client.get_klines(symbol=sembol,interval=client.KLINE_INTERVAL_1MONTH,limit=1)
        prices1 = [float(kline[4]) for kline in klines]
        avg_price = sum(prices1) / len(prices1)
        messagebox.showinfo("Sonuç",f"1 Aylık ortalama {avg_price}")
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

    except Exception as e:
        messagebox.showerror("Hata",f"{e}")



pencere = tk.Tk()
pencere.title("Kripto para menüsü")
tk.Label(pencere, text="Görüntülemek istediğiniz kripto parayı yazın").pack()
görüntüle = tk.Entry(pencere)
görüntüle.pack()
tk.Button(pencere, text="Anlık fiyat", command=göster).pack()
tk.Button(pencere, text="En yüksek", command=en_yüksek).pack()
tk.Button(pencere, text="En düşük", command=en_düsük).pack()
tk.Button(pencere, text="Hacim", command=Hacim_Göster).pack()
tk.Button(pencere, text="5 dakikaklık ortalama", command=bes_dakikalık_ortalama).pack()
tk.Button(pencere, text="1 Saatlik ortalama", command=ortalama_1_hour).pack()
tk.Button(pencere, text="24 Saatlik ortalama", command=ortalama_1_day).pack()
tk.Button(pencere,text="1 Aylık Ortalama",command=bir_ay_ort).pack()
tk.Button(pencere, text="5 dakikalık değişim", command=değişim_5_dakika).pack()
tk.Button(pencere, text="1 Saatlik değişim", command=değişim_bir_saat).pack()
tk.Button(pencere, text="1 günlük değişim", command=değişim_bir_gün).pack()
tk.Button(pencere, text="1 haftalık değişim", command=değişim_bir_hafta).pack()
tk.Button(pencere,text="1 Aylık değişim",command=değişim_1_month).pack()
tk.Button(pencere, text="Tüm coinler", command=coin_göser).pack()
tk.Button(pencere,text="Vadeli işlemler fiyatı",command=vadeli).pack()
tk.Button(pencere,text="MarkPrice",command=adil).pack()
tk.Button(pencere,text="Son fonlama Oranı",command=fonlama).pack()
tk.Button(pencere,text="Tüm Piyasa ortalaması",command=piyasa_ortalama).pack()
tk.Button(pencere,text="Genel Veriler",command=genel_veriler).pack()
tk.Button(pencere,text="Derinlik bilgisi",command=depth_bids).pack()
tk.Button(pencere,text="Hacim(detaylı)",command=min_max_adım).pack()
pencere.mainloop()
