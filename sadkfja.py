from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}

# movies_no = []
# url = 'https://movie.naver.com/movie/bi/mi/reviewread.naver?nid=4799281&code=208077&order=#tab'
# res = requests.get(url, headers=headers)
# html = res.content.decode('utf-8', 'replace')
# res.raise_for_status()
# soup = BeautifulSoup(html, 'html.parser')
# p_title = soup.find("h3", {"class": "h_movie"})
# p = p_title.find("a").get_text()
# p_review = soup.find("div", {"class": "user_tx_area"}).get_text()
# print(p_review)
url_list = []
movies_no=[164122]
# movies_no=[201766,164122]

for i in range(len(movies_no)) :
    reviews_no = []
    is_end = False
    for review_page in range(1, 7):
        if is_end:
            break
        url= 'https://movie.naver.com/movie/bi/mi/review.naver?code={}&page={}'.format(movies_no[i],review_page)
        res = requests.get(url, headers=headers)
        html = res.content.decode('utf-8', 'replace')
        res.raise_for_status()
        soup = BeautifulSoup(html, 'html.parser')
        con = soup.find("ul", {"class": "rvw_list_area"})
        try:
            for content in con.find_all("li"):

                review_no = re.sub(r'[^0-9]', '', (content.find("a")["onclick"]))
                if review_no in reviews_no:
                    is_end = True
                    break
                reviews_no.append(int(review_no))

        except:
            continue






    url_list.append([movies_no[i], reviews_no])

        # print(url_list)


print(url_list)

