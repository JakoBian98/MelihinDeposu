import tkinter as tk
from tkinter import messagebox
import os
pencere = tk.Tk()
pencere.title("Bankacılık Sistemi")
dosya_adı = "kullanıcılar.txt"
def kullanıcı_kayıt(ad, şifre, bakiye=0.0):
    with open(dosya_adı, "a") as dosya:
        dosya.write(f"{ad},{şifre},{bakiye}\n")
def kullanıcı_doğrula(ad, şifre):
    if not os.path.exists(dosya_adı):
        return False, 0.0
    with open(dosya_adı, "r") as dosya:
        satırlar = dosya.readlines()
        for satır in satırlar:
            bilgiler = satır.strip().split(",")
            if bilgiler[0] == ad and bilgiler[1] == şifre:
                return True, float(bilgiler[2])
    return False, 0.0
def bakiye_güncelle(ad, yeni_bakiye):
    if not os.path.exists(dosya_adı):
        return
    with open(dosya_adı, "r") as dosya:
        satırlar = dosya.readlines()
    with open(dosya_adı, "w") as dosya:
        for satır in satırlar:
            bilgiler = satır.strip().split(",")
            if bilgiler[0] == ad:
                dosya.write(f"{ad},{bilgiler[1]},{yeni_bakiye}\n")
            else:
                dosya.write(satır)
def para_transferi(ad, bakiye, bakiye_var):
    transfer_pencere = tk.Toplevel()
    transfer_pencere.title("Transfer Menüsü")
    tk.Label(transfer_pencere, text="Alıcı kullanıcı adı:").pack()
    entry_alıcı = tk.Entry(transfer_pencere)
    entry_alıcı.pack()
    tk.Label(transfer_pencere, text="Gönderilecek miktar:").pack()
    entry_miktar = tk.Entry(transfer_pencere)
    entry_miktar.pack()
    def transfer_et():
        nonlocal bakiye
        alıcı = entry_alıcı.get()
        try:
            miktar = float(entry_miktar.get())
            if miktar <= 0:
                messagebox.showerror("Hata", "Göndermek istediğiniz miktar sıfırdan küçük veya eşit olamaz")
                return
            if miktar > bakiye:
                messagebox.showerror("Hata", "Yetersiz bakiye")
                return
            if not os.path.exists(dosya_adı):
                messagebox.showerror("Hata", "Kullanıcı verisi bulunamadı")
                return
            alıcı_bulundu = False
            with open(dosya_adı, "r") as dosya:
                satırlar = dosya.readlines()
            for i, satır in enumerate(satırlar):
                bilgiler = satır.strip().split(",")
                if bilgiler[0] == alıcı:
                    alıcı_bakiye = float(bilgiler[2]) + miktar
                    bilgiler[2] = str(alıcı_bakiye)
                    satırlar[i] = f"{bilgiler[0]},{bilgiler[1]},{bilgiler[2]}\n"
                    alıcı_bulundu = True
                    break
            if not alıcı_bulundu:
                messagebox.showerror("Hata", "Alıcı bulunamadı")
                return
            bakiye -= miktar
            bakiye_güncelle(ad, bakiye)
            with open(dosya_adı, "w") as dosya:
                for satır in satırlar:
                    dosya.write(satır)
            bakiye_var.set(f"Bakiyeniz: {bakiye} TL")
            messagebox.showinfo("Başarılı", f"{alıcı} kişisine {miktar} TL gönderildi")
            transfer_pencere.destroy()
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir sayı giriniz")
    tk.Button(transfer_pencere, text="Transfer Et", command=transfer_et).pack(pady=5)
def ana_menü(ad, bakiye):
    yeni_pencere = tk.Toplevel(pencere)
    yeni_pencere.title("Ana Menü")
    bakiye_var = tk.StringVar()
    bakiye_var.set(f"Bakiyeniz: {bakiye} TL")
    tk.Label(yeni_pencere, text=f"Hoş geldiniz, {ad}").pack(pady=5)
    tk.Label(yeni_pencere, textvariable=bakiye_var).pack(pady=5)
    tk.Label(yeni_pencere, text="Miktar:").pack()
    entry_miktar = tk.Entry(yeni_pencere)
    entry_miktar.pack(pady=5)
    kredi_limiti = 5000
    kredi_borcu = [0.0]
    def para_çek():
        nonlocal bakiye
        try:
            miktar = float(entry_miktar.get())
            if miktar > bakiye:
                messagebox.showerror("Hata", "Yetersiz bakiye")
                return
            bakiye -= miktar
            bakiye_güncelle(ad, bakiye)
            bakiye_var.set(f"Bakiyeniz: {bakiye} TL")
            messagebox.showinfo("İşlem Başarılı", f"{miktar} TL çektiniz. Yeni bakiyeniz: {bakiye} TL")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir sayı giriniz")
    def para_yatır():
        nonlocal bakiye
        try:
            miktar = float(entry_miktar.get())
            bakiye += miktar
            bakiye_güncelle(ad, bakiye)
            bakiye_var.set(f"Bakiyeniz: {bakiye} TL")
            messagebox.showinfo("İşlem Başarılı", f"{miktar} TL yatırdınız. Yeni bakiyeniz: {bakiye} TL")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir sayı giriniz")
    def kredi_çek():
        nonlocal bakiye
        try:
            miktar = float(entry_miktar.get())
            if kredi_borcu[0] + miktar > kredi_limiti:
                messagebox.showerror("Hata", f"Kredi limitiniz yetersiz. Maksimum {kredi_limiti} TL")
                return
            bakiye += miktar
            kredi_borcu[0] += miktar
            bakiye_güncelle(ad, bakiye)
            bakiye_var.set(f"Bakiyeniz: {bakiye} TL")
            messagebox.showinfo("Kredi Alındı", f"{miktar} TL kredi çektiniz. Yeni bakiyeniz: {bakiye} TL")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir sayı giriniz")
    def kredi_öde():
        nonlocal bakiye
        try:
            miktar = float(entry_miktar.get())
            if bakiye < miktar:
                messagebox.showerror("Hata", "Yeterli bakiyeniz yok")
                return
            if miktar > kredi_borcu[0]:
                messagebox.showerror("Hata", "Kredi borcunuzdan fazla ödeme yapamazsınız")
                return
            bakiye -= miktar
            kredi_borcu[0] -= miktar
            bakiye_güncelle(ad, bakiye)
            bakiye_var.set(f"Bakiyeniz: {bakiye} TL")
            messagebox.showinfo("Ödeme Başarılı", f"{miktar} TL kredi borcu ödendi. Kalan borç: {kredi_borcu[0]} TL")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir sayı giriniz")
    tk.Button(yeni_pencere, text="Para Yatır", command=para_yatır).pack(pady=3)
    tk.Button(yeni_pencere, text="Para Çek", command=para_çek).pack(pady=3)
    tk.Button(yeni_pencere, text="Kredi Çek", command=kredi_çek).pack(pady=3)
    tk.Button(yeni_pencere, text="Kredi Öde", command=kredi_öde).pack(pady=3)
    tk.Button(yeni_pencere, text="Para Transferi", command=lambda: para_transferi(ad, bakiye, bakiye_var)).pack(pady=3)
def giriş_yap():
    ad = entry_ad.get()
    şifre = entry_şifre.get()
    doğrulandı, bakiye = kullanıcı_doğrula(ad, şifre)
    if doğrulandı:
        messagebox.showinfo("Başarılı", "Giriş yapıldı")
        ana_menü(ad, bakiye)
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı")
def kayıt_ol():
    ad = entry_ad.get()
    şifre = entry_şifre.get()
    if not ad or not şifre:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurunuz")
        return
    doğrulandı, _ = kullanıcı_doğrula(ad, şifre)
    if doğrulandı:
        messagebox.showerror("Hata", "Bu kullanıcı adı zaten alınmış")
        return
    kullanıcı_kayıt(ad, şifre)
    messagebox.showinfo("Başarılı", "Kayıt tamamlandı")
tk.Label(pencere, text="Kullanıcı Adı:").pack()
entry_ad = tk.Entry(pencere)
entry_ad.pack()
tk.Label(pencere, text="Şifre:").pack()
entry_şifre = tk.Entry(pencere, show="*")
entry_şifre.pack()
tk.Button(pencere, text="Giriş Yap", command=giriş_yap).pack(pady=5)
tk.Button(pencere, text="Kayıt Ol", command=kayıt_ol).pack(pady=5)
pencere.mainloop()