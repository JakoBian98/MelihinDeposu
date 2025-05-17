import tkinter as tk
from tkinter import messagebox
from binance.client import Client
client = Client(api_key="", api_secret="")
btc = client.get_symbol_ticker(symbol="BTCUSDT")
eth = client.get_symbol_ticker(symbol="ETHUSDT")
xrp = client.get_symbol_ticker(symbol="XRPUSDT")
doge = client.get_symbol_ticker(symbol="DOGEUSDT")
solana = client.get_symbol_ticker(symbol="SOLUSDT")
bnb = client.get_symbol_ticker(symbol="BNBUSDT")
def göster():
   sembol = str(görüntüle.get())
   coin = client.get_symbol_ticker(symbol=sembol)
   messagebox.showinfo("Sonuç ",f"1 {sembol} : {coin['price']} USDT")
def göster2():
    sembol = str(görüntüle.get())
    coin = client.get_ticker(symbol=sembol)
    messagebox.showinfo("Sonuç",f"24 Saatte en yüksek : {coin['highPrice']}")
def göster3():
    sembol = str(görüntüle.get())
    coin = client.get_ticker(symbol=sembol)
    messagebox.showinfo("Sonuç",f"24 Saate en düşük {coin['lowPrice']}")
def göster4():
    sembol = str(görüntüle.get())
    coin = client.get_ticker(symbol=sembol)
    messagebox.showinfo("Sonuç",f"24 Saatlik hacim : {coin['volume']} USDT")
def göster5():
    sembol = str(görüntüle.get())
    try:
        klines = client.get_klines(symbol=sembol,interval="5m",limit="1")
        prices1 = [float(kline[4]) for kline in klines]
        avg_price = sum(prices1) / len(prices1)
        messagebox.showinfo("Sonuç",f"{sembol} 5 dakikalık ortalaması : {avg_price}")
    except:
        messagebox.showerror("Hata","Bir hata oluştu")
def göster6():
    try:
        sembol = str(görüntüle.get())
        klines = client.get_klines(symbol=sembol,interval="5m",limit="12")
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
def ortalama31():
    sembol = str(görüntüle.get())
    klines = client.get_klines(symbol=sembol,interval=client.KLINE_INTERVAL_1DAY,limit=1)
    prices1 = [float(kline[4]) for kline in klines]
    avg_price = sum(prices1) / len(prices1)
    messagebox.showinfo("Sonuç",f"{sembol} 1 günlük ortalaması : {avg_price}")
def değişim():
    sembol = str(görüntüle.get())
    kline_5dk = client.get_klines(symbol=sembol, interval=client.KLINE_INTERVAL_1MINUTE, limit=5)
    ilk_5dk = float(kline_5dk[0][1])
    son_5dk = float(kline_5dk[-1][4])
    değişim_5dk = ((son_5dk - ilk_5dk) / ilk_5dk) * 100
    messagebox.showinfo("Sonuç", f"{sembol} 1 saatlik değişimi %{değişim_5dk}")
def değişim2():
    sembol = str(görüntüle.get())
    kline1saat = client.get_klines(symbol=sembol, interval=client.KLINE_INTERVAL_1HOUR, limit=1)
    ilk_1saat = float(kline1saat[0][1])
    son_1saat = float(kline1saat[-1][4])
    değişim_1saat = ((son_1saat - ilk_1saat) / ilk_1saat) * 100
    messagebox.showinfo("Sonuç", f"{sembol} 1 saatlik değişimi %{değişim_1saat}")
def değişim3():
    sembol = str(görüntüle.get())
    kline_1gün = client.get_klines(symbol=sembol, interval=client.KLINE_INTERVAL_1DAY, limit=1)
    ilk_gün = float(kline_1gün[0][1])
    son_gün = float(kline_1gün[-1][4])
    değişim_1gün = ((son_gün - ilk_gün) / ilk_gün) * 100
    messagebox.showinfo("Sonuç", f"{sembol} 1 günlük değişimi %{değişim_1gün}")
def değişim4():
    sembol = str(görüntüle.get())
    kline1hafta = client.get_klines(symbol=sembol, interval=client.KLINE_INTERVAL_1WEEK, limit=1)
    ilkhafta = float(kline1hafta[0][1])
    son_hafta = float(kline1hafta[-1][4])
    değişim1_hafta = ((son_hafta - ilkhafta) / ilkhafta) * 100
    messagebox.showinfo("Sonuç",f"{sembol} 1 haftalık değişimi %{değişim1_hafta}")
def vadeli():
    sembol = str(görüntüle.get())
    fiyat_bilgi = client.futures_symbol_ticker(symbol=sembol)
    fiyat = fiyat_bilgi['price']
    messagebox.showinfo("Sonuç",f"{sembol} vadeli fiyatı : {fiyat} USDT")
def adil():
    sembol = str(görüntüle.get())
    mark_price = client.futures_mark_price(symbol=sembol)
    messagebox.showinfo("Sonuç",f"Adil değer (Mark Price) : {mark_price['markPrice']} USDT")
def fonlama():
    sembol = str(görüntüle.get())
    fonlama_oranı = client.futures_mark_price(symbol=sembol)
    messagebox.showinfo("Sonuç",f"Son Fonlama Oranı : {fonlama_oranı['lastFundingRate']}")
def piyasa_ortalama():
        tickers = client.get_ticker()
        price_changes = []
        for ticker in tickers:
            symbol = ticker['symbol']
            if symbol.endswith('USDT'):
                price_changes.append(float(ticker['priceChangePercent']))
        if price_changes:
            avg_change = sum(price_changes) / len(price_changes)
            messagebox.showinfo("Sonuç", f"Tüm coinlerin 24 saatlik ortalaması : {avg_change}")
pencere = tk.Tk()
pencere.title("Kripto para menüsü")
tk.Label(pencere, text="Görüntülemek istediğiniz kripto parayı yazın").pack()
görüntüle = tk.Entry(pencere)
görüntüle.pack()
tk.Button(pencere, text="Anlık fiyat", command=göster).pack()
tk.Button(pencere, text="En yüksek", command=göster2).pack()
tk.Button(pencere, text="En düşük", command=göster3).pack()
tk.Button(pencere, text="Hacim", command=göster4).pack()
tk.Button(pencere, text="5 dakikaklık ortalama", command=göster5).pack()
tk.Button(pencere, text="1 Saatlik ortalama", command=göster6).pack()
tk.Button(pencere, text="24 Saatlik ortalama", command=ortalama31).pack()
tk.Button(pencere, text="5 dakikalık değişim", command=değişim).pack()
tk.Button(pencere, text="1 Saatlik değişim", command=değişim2).pack()
tk.Button(pencere, text="1 günlük değişim", command=değişim3).pack()
tk.Button(pencere, text="1 haftalık değişim", command=değişim4).pack()
tk.Button(pencere, text="Tüm coinler", command=coin_göser).pack()
tk.Button(pencere,text="Vadeli işlemler fiyatı",command=vadeli).pack()
tk.Button(pencere,text="MarkPrice",command=adil).pack()
tk.Button(pencere,text="Son fonlama Oranı",command=fonlama).pack()
tk.Button(pencere,text="Tüm Piyasa ortalaması",command=piyasa_ortalama).pack()
pencere.mainloop()