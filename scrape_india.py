from bs4 import BeautifulSoup
import requests
import os


page = 1010


categories = ["india"]


def collect_page(url, path):
    print(path)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        file = open(path, "w")
        header = soup.find("div", class_="zm-post-header")
        header_text = header.text if header else ""
        file.write(header_text)
        content = soup.find("div", class_="zm-post-content")
        content_text = content.text if content else ""
        file.write(content_text)
        file.close()
    except Exception as ex:
        pass

for category in categories:
    page = 227
    content = "content"
    url = f"https://theekkathir.in/News/GetNewsListByCategory?CategoryName={category}&SubCategoryName=&PageNo="
    while page < 1015:
        try:
            purl = url + str(page)
            print("purl", purl)
            response = requests.get(purl)
            print(response.status_code)
            soup = BeautifulSoup(response.content, "html.parser")
            h1 = soup.find_all("h1", class_="zm-post-title")
            content = h1
            # print(content)
            aurls = []
            for item in h1:
                iurl = item.find("a")['href']
                text = item.find("a").text.replace(" ", "")[:30]
                path = os.path.join(category, text)
                collect_page(iurl, path)
        except Exception as ex:
            print(str(ex))
        page += 1
        
    
