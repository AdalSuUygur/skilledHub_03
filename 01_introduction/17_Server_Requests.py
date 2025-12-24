
#ders 21 notları

from requests import get
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException #her farklı modülün kendi exception sınıfları vardır
from pprint import pprint

try:
    pass
except HTTPError as err:
    print(f"HTTP error: {err}")

#.json java script object notation - bir notasyon
#yani ortak dil 

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

