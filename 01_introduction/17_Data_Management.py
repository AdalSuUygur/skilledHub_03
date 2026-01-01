
#! DATA MANAGEMENT
# 1. HTTP Döngüsü (Pizzacı Analojisi): İstemci (Sen) ve Sunucu (Pizzacı) arasındaki o "kurallı konuşma".
# 2. JSON Yapısı (Koli Analojisi): Verilerin o "standart kutunun" içinde nasıl düzenli durduğunu hatırla.
# 3. API Mantığı (Garson Analojisi): Senin mutfağa girmene gerek kalmadan, garsonun (API) aradaki köprüyü nasıl kurduğu.

#! HTTP Protokolü:
#* Sen evdesin (**Client/İstemci**). Pizza yemek istiyorsun. Pizzacı dükkanı ise uzakta (**Server/Sunucu**).
#* Senin pizzacıya telefon açıp "Bana karışık pizza gönder" demen **Request (İstek)**'tir.
#* Pizzacının sana pizzayı kutulayıp göndermesi **Response (Cevap)**'tır.
#* HTTP ise, o telefon konuşmasının **kurallarıdır**.
#* "Önce merhaba de, sonra adresini ver, sonra siparişi söyle" gibi kurallar bütünüdür.
#* Eğer bu kurallar (Protokol) olmasaydı; sen Türkçe konuşurken pizzacı Çince konuşuyor olabilirdi ve pizza asla gelmezdi. 
#* Bütün web siteleri (Google, YouTube, Instagram) bu kurallar sayesinde, senin bilgisayarın hangi marka olursa olsun aynı şekilde açılır.
#? Yani HTTP Protokolü: Farklı dildeki istemlerin server tarafında anlaşılabilmesi için konulmuş kurallar bütünüdür.

#! JSON (Java Script Object Notation)
#* Diyelim ki evini taşıyorsun (Veri transferi).
#* Eşyalarını (Verilerini) kamyona rastgele atamazsın. Kırılır, kaybolur.
#* Hepsini standart kolilere (JSON) koyarsın. Üzerine ne olduğunu yazarsın.
#* Yeni eve gittiğinde kolileri açar, eşyaları tekrar yerleştirirsin.
#? Yani JSON: Verilerin internette seyahat ederken bozulmaması için konulduğu o standart, metin tabanlı kolidir.

#! API (Application Programming Interface)
#* API, iki farklı yazılımın birbiriyle konuşmasını sağlayan "Ortak Bağlantı Noktası"dır.
#* Restorandaki Garson gibidir: Sen (Client) mutfağa (Server) giremezsin. Siparişini (Request) garsona verirsin, o da sana yemeği (Response) getirir.
#* Elektrik Prizi gibidir: Duvarın arkasındaki (Backend) karmaşık kabloları bilmene gerek yoktur. Fişi prize takarsın ve çalışır.
#* Güvenliktir: Mutfağın sırlarını ve malzemelerini (Veritabanı) dışarıdan gelenlere karşı koruyan kapıdaki görevlidir.
#? Yani API: İki farklı yazılımın, birbirlerinin kodlarını veya çalışma şekillerini görmeden, sadece veri alışverişi yaparak anlaşmasını sağlayan köprüdür.

# Not: İlk kullanım amacı farklı programlama dillerinde yazılmış farklı ortamlarda çalışabilen uygulamaların birbirleriyle konuşması için idi.
# Ancak artık hayatımız mikro servisler girdi ve bununla birlikte her farklı bir özellik için farklı bir API kullanılıyor. 
# Mesela e-ticaret sitesindeki search için bir API, ödeme için bir API, kategoriler için API, mobil uygulama için APIler kullanılıyor.


#* Bütün paketler pypi.org sitesinde. Buradan requests adlı paket indirilecek.
#* Bir modül nasıl yüklenir?
# 1. pypi.org sitesine gidilerek ilgili modül aratılır.
# 2. modülün sitesinde isminin altında "copy to clipboard" seçeneği seçilir.
# 3. VS Code'da terminal açılır.
# 4. venv aktif olunup olunmadığı kontrol edilir. Aktifse; yapıştır ve paketi yükle.
# 5. venv aktif değilse terminale: .\venv\Scripts\activate yazmak gerekli. Aktif olduktan sonra yapıştır ve modülü yükle.
#* Not: Bu neden önemli? Çünkü modüller venv içerisine yüklenir.

#todo 
from requests import get #request modülünden get fonksiyonunu kullanacağımız için bunu aldık.
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException #her farklı modülün kendi exception sınıfları vardır
from pprint import pprint #güzel gözülmesi için

#Şu anda kendimizce bir API yazdık sanırım?
try: #Her API'nin bir endpointi vardır. Biz bu endpoint'e request atarız.
    end_point = "https://newsapi.org/v2/everything?q=tesla&from=2025-11-18&sortBy=publishedAt&apiKey=47f3419f49864ca889f632677d485de1"
    # NewsAPI'den aldığımız beleş API key'ini yapıştırıyoruz.

    response = get(end_point, timeout= 6000) # endpointten talepte bulunduk, 6 sn içinde yanıt gelmezse timeout olur dedik.

    data = response.json() #gelen yanıtı json'a dönüştürüyoruz.
    pprint(data) #yazdırdık ve veriye ulaştık!

except HTTPError as err: #alınan her hataya farklı cevaplar vermek için
    print(f"HTTP error: {err}")
except ConnectionError as err: #her bir hatayı ayrı ayrı yazabiliriz
    print(f"Connection error: {err}")
except (Timeout, RequestException) as err: #ya da hepsini böyle parantez içinde tek bir çıktıda yazabiliriz
    print(err)


#ilk makalenin yazarını ve titleını ekrana yazdıran program. bu kod bloğuna ihtiyacım var ama


# # # 18 12 25 - ders notları
# # #ödev çözümü

# # # özlemin çözümü

# # # author_name = input("Auther name:")
# # # articles = []
# # # for article in data["articles"]:
# # #     author = article.get("author")
    
# # #     if author and author_name.lower() in author.lower():
# # #         articles.append(article)
# # # if articles:
# # #     print(f"\nArticles by {author_name}:\n")
# # #     for art in articles:
# # #         print(art["title"])

