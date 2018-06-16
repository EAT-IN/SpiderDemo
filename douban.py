import requests
import json
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36",
    "Referer": "https://m.douban.com/movie/western"
}
while True:
    num = 18
    # chinese = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_movie_chinese_hot/items?start=0&count={}&loc_id=108288&_=1529156427243".format(num)
    western = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_movie_occident_hot/items?start=0&count={}&loc_id=108288&_=1529158954801".format(num)

    r = requests.get(western, headers=headers)
    html_context = r.content.decode()
    # pprint(json.loads(html_context)["subject_collection_items"])
    movie_list = json.loads(html_context)["subject_collection_items"]
    for movie in movie_list:
        name = (movie["title"])+"  评分:"+str(movie["rating"]["value"])+"\n"
        # time.sleep(1)
        with open("movie2.txt", "a", encoding="utf-8") as f:
            f.write(name)
    if num <200:
        num +=18
    else:
        break