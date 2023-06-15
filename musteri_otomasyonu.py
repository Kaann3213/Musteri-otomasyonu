import openpyxl
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="musteri"
)

# Bağlantı başarıyla sağlandıysa aşağıdaki mesajı yazdırabilirsiniz
if mydb.is_connected():
    print("Veritabanı bağlantısı başarılı.")


# Veritabanı bağlantısı
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="musteri"
)

def kullanici_secimini_goster():
    print("1. Veri ekleme işlemi")
    print("2. Veri silme işlemi")
    print("3. Veri güncelleme işlemi")
    print("4. Veri listeleme işlemi")
    print("5. Grafik işlemleri seçenekleri")
    print("6. Dosya işlemleri seçenekleri")
    print("0. Çıkış")

def veri_ekleme_islemi():
    id = input("Müşteri ID'si: ")
    ad = input("Müşteri Adı: ")
    soyad = input("Müşteri Soyadı: ")
    eposta = input("Müşteri E-Posta: ")
    telefon = input("Müşteri Telefonu: ")

    cursor = mydb.cursor()

    # Veriyi ekleme
    sql = "INSERT INTO musteri (id, ad, soyad, eposta, telefon) VALUES (%s, %s, %s, %s, %s)"
    values = (id, ad, soyad, eposta, telefon)
    cursor.execute(sql, values)

    mydb.commit()

    print("Müşteri başarıyla eklendi.")

def veri_silme_islemi():
    id = input("Silinecek Müşteri ID'si: ")

    cursor = mydb.cursor()
    

    # Veriyi silme
    sql = "DELETE FROM musteri WHERE id = %s"
    value = (id,)
    cursor.execute(sql, value)

    mydb.commit()

    print("Müşteri başarıyla silindi.")

def veri_guncelleme_islemi():
    id = input("Güncellenecek Müşteri ID'si: ")
    yeni_ad = input("Yeni Müşteri Adı: ")
    yeni_soyad = input("Yeni Müşteri Soyadı: ")
    yeni_eposta = input("Yeni Müşteri E-Posta: ")
    yeni_telefon = input("Yeni Müşteri Telefonu: ")

    cursor = mydb.cursor()

    # Veriyi güncelleme
    sql = "UPDATE musteri SET ad = %s, soyad = %s, eposta = %s, telefon = %s WHERE id = %s"
    values = (yeni_ad, yeni_soyad, yeni_eposta, yeni_telefon, id)
    cursor.execute(sql, values)

    mydb.commit()

    print("Müşteri başarıyla güncellendi.")

def veri_listeleme_islemi():
    cursor = mydb.cursor()

    # Tüm müşterileri çekme
    sql = "SELECT * FROM musteri"
    cursor.execute(sql)

    musteri = cursor.fetchall()

    # Müşterileri liste halinde gösterme
    for musteri in musteri:
        print("ID: {}, Ad: {}, Soyad: {}, E-Posta: {}, Telefon: {}".format(musteri[0], musteri[1], musteri[2], musteri[3], musteri[4]))

def grafik_islemleri_seceneklerini_goster():
    print("1. Pasta grafiği oluşturma işlemi")
    print("2. Histogram oluşturma işlemi")
    print("3. Saçılma grafiği oluşturma işlemi")
    print("4. Çubuk grafiği oluşturma işlemi")
    print("5. Çizgi grafiği oluşturma işlemi")
    print("0. Geri Dön")

def pasta_grafigi_olusturma_islemi():
    # Veritabanı bağlantısı
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="musteri"
    )

    cursor = mydb.cursor()

    # Verileri getirme
    sql = "SELECT ad, COUNT(*) as sayi FROM musteri GROUP BY ad"
    cursor.execute(sql)

    veriler = cursor.fetchall()

    # Verileri ayrıştırma
    adlar = []
    sayilar = []
    for veri in veriler:
        adlar.append(veri[0])
        sayilar.append(veri[1])

    # Pasta grafiği oluşturma
    plt.pie(sayilar, labels=adlar, autopct='%1.1f%%')
    plt.title("Müşterilerin Adlara Göre Dağılımı")

    # Grafiği gösterme
    plt.show()

def histogram_grafigi_olusturma_islemi():
    # Veritabanı bağlantısı
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="musteri"
    )

    cursor = mydb.cursor()

    # Verileri getirme
    sql = "SELECT telefon FROM musteri"
    cursor.execute(sql)

    veriler = cursor.fetchall()

    # Verileri ayrıştırma
    telefonlar = [int(veri[0]) for veri in veriler]

    # Histogram grafiği oluşturma
    plt.hist(telefonlar, bins=10, edgecolor='black')
    plt.title("Müşterilerin Telefon Numaralarının Histogramı")
    plt.xlabel("Telefon Numarası")
    plt.ylabel("Frekans")

    # Grafiği gösterme
    plt.show()

def sacilma_grafigi_olusturma_islemi():
    # Veritabanı bağlantısı
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="musteri"
    )

    cursor = mydb.cursor()

    # Verileri getirme
    sql = "SELECT id, telefon FROM musteri"
    cursor.execute(sql)

    veriler = cursor.fetchall()

    # Verileri ayrıştırma
    idler = [veri[0] for veri in veriler]
    telefonlar = [int(veri[1]) for veri in veriler]

    # Saçılma grafiği oluşturma
    plt.scatter(idler, telefonlar)
    plt.title("Müşterilerin Telefon Numaralarının Dağılımı")
    plt.xlabel("ID")
    plt.ylabel("Telefon Numarası")

    # Grafiği gösterme
    plt.show()

def cubuk_grafigi_olusturma_islemi():
    # Veritabanı bağlantısı
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="musteri"
    )

    cursor = mydb.cursor()

    # Verileri getirme
    sql = "SELECT ad, COUNT(*) as sayi FROM musteri GROUP BY ad"
    cursor.execute(sql)

    veriler = cursor.fetchall()

    # Verileri ayrıştırma
    adlar = []
    sayilar = []
    for veri in veriler:
        adlar.append(veri[0])
        sayilar.append(veri[1])

    # Çubuk grafiği çizme
    plt.bar(adlar, sayilar)
    plt.title("Müşterilerin Adlara Göre Dağılımı")
    plt.xlabel("Ad")
    plt.ylabel("Sayı")

    # Grafiği gösterme
    plt.show()

def cizgi_grafigi_olusturma_islemi():
    # Veritabanı bağlantısı
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="musteri"
    )

    cursor = mydb.cursor()

    # Verileri getirme
    sql = "SELECT id, COUNT(*) as sayi FROM musteri GROUP BY id"
    cursor.execute(sql)

    veriler = cursor.fetchall()

    # Verileri ayrıştırma
    idler = []
    sayilar = []
    for veri in veriler:
        idler.append(veri[0])
        sayilar.append(veri[1])

    # Çizgi grafiği çizme
    plt.plot(idler, sayilar)
    plt.title("Müşteri ID'lerine Göre Dağılım")
    plt.xlabel("ID")
    plt.ylabel("Sayı")

    # Grafiği gösterme
    plt.show()

def dosya_islemleri_seceneklerini_goster():
    print("1. Veri okuma işlemi")
    print("2. Verileri listeleme işlemi")
    print("3. Veritabanına kaydetme işlemi")
    print("0. Geri Dön")

def veri_okuma_islemi():
    # Excel dosyasını okuma
    dataframe = pd.read_excel("VERİLER.xlsx")
    dosya_adi = "VERİLER.xlsx"
    workbook = openpyxl.load_workbook(dosya_adi)
    sheet = workbook.active

    veriler = []

    # Verileri alma
    for row in sheet.iter_rows(values_only=True):
        veri = {
            "id": row[0],
            "ad": row[1],
            "soyad": row[2],
            "eposta": row[3],
            "telefon": row[4]
        }
        veriler.append(veri)

    # Veritabanı bağlantısı
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="musteri"
    )

    cursor = mydb.cursor()

    # Verileri veritabanına kaydetme
    for veri in veriler:
        sql = "INSERT INTO musteri (id, ad, soyad, eposta, telefon) VALUES (%s, %s, %s, %s, %s)"
        values = (veri["id"], veri["ad"], veri["soyad"], veri["eposta"], veri["telefon"])
        cursor.execute(sql, values)

    mydb.commit()

    print("Veriler başarıyla kaydedildi.")

while True:
    kullanici_secimini_goster()

    secim = input("Bir seçim yapın: ")

    if secim == "1":
        veri_ekleme_islemi()
    elif secim == "2":
        veri_silme_islemi()
    elif secim == "3":
        veri_guncelleme_islemi()
    elif secim == "4":
        veri_listeleme_islemi()
    elif secim == "5":
        while True:
            grafik_islemleri_seceneklerini_goster()

            secim = input("Bir seçim yapın: ")

            if secim == "1":
                pasta_grafigi_olusturma_islemi()
            elif secim == "2":
                histogram_grafigi_olusturma_islemi()
            elif secim == "3":
                sacilma_grafigi_olusturma_islemi()
            elif secim == "4":
                cubuk_grafigi_olusturma_islemi()
            elif secim == "5":
                cizgi_grafigi_olusturma_islemi()
            elif secim == "0":
                break
            else:
                print("Geçersiz seçim. Tekrar deneyin.")
    elif secim == "6":
        while True:
            dosya_islemleri_seceneklerini_goster()

            secim = input("Bir seçim yapın: ")

            if secim == "1":
                veri_okuma_islemi()
            elif secim == "2":
                veri_listeleme_islemi()
            elif secim == "3":
                
                
                def veritabanina_kaydet():
                    



    # Dosya okuma işlemi
    veriler = veri_okuma_islemi()

    if veriler:
        cursor = mydb.cursor()
        
        # Veritabanı bağlantısı
   
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="musteri"
    )

        # SQL sorgusu ile verileri ekleme
    sql = "INSERT INTO kitaplar (id, isim, yazar, fiyat) VALUES (%s, %s, %s, %s)"
    cursor.executemany(sql, veriler)

        # Değişiklikleri kaydetme
    mydb.commit()

    mydb.close()
    if veriler:
    cursor = mydb.cursor()

    print("Veriler başarıyla veritabanına kaydedildi.")
    else:
    print("Kaydedilecek veri bulunamadı.")

#...

    while True:
    kullanici_secimini_goster()

    secim = input("Bir seçim yapın: ")

    if secim == "1":
        veri_ekleme_islemi()
    elif secim == "2":
        veri_silme_islemi()
    elif secim == "3":
        veri_guncelleme_islemi()
    elif secim == "4":
        veri_listeleme_islemi()
    elif secim == "5":
        while True:
            grafik_islemleri_seceneklerini_goster()

            secim = input("Bir seçim yapın: ")

            if secim == "1":
                pasta_grafigi_olusturma_islemi()
            elif secim == "2":
                histogram_grafigi_olusturma_islemi()
            elif secim == "3":
                sacilma_grafigi_olusturma_islemi()
            elif secim == "4":
                cubuk_grafigi_olusturma_islemi()
            elif secim == "5":
                cizgi_grafigi_olusturma_islemi()
            elif secim == "0":
                break
            else:
                print("Geçersiz seçim. Tekrar deneyin.")
    elif secim == "6":
        while True:
            dosya_islemleri_seceneklerini_goster()

            secim = input("Bir seçim yapın: ")

            if secim == "1":
                veri_okuma_islemi()
            elif secim == "2":
                veri_listeleme_islemi()
            elif secim == "3":
                
                # Veritabanına kaydetme işlemi
                
                print("Veriler veritabanına kaydediliyor...")
                veritabanina_kaydet()
            elif secim == "0":
                break
            else:
                print("Geçersiz seçim. Tekrar deneyin.")
    elif secim == "0":
        break
    else:
        print("Geçersiz seçim. Tekrar deneyin.")

