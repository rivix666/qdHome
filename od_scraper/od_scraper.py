""" TODO """

import requests
from bs4 import BeautifulSoup
import const
from models.home_data import HomeData


def request_response(url):
    try:
        return requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Exception:", e)


def soup_gather_homes(url):
    response = request_response(url)
    if response:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.select(".offer-item-details")


def soup_gather_home_data(item):
    data = HomeData()
    data.title = item.select_one(".offer-item-title").getText()
    data.price = item.select_one(".offer-item-price").getText()
    data.rooms = item.select_one(".offer-item-rooms").getText()
    data.area = item.select_one(".offer-item-area").getText()
    data.m_price = item.select_one(".offer-item-price-per-m").getText()
    data.desc_url = item.select_one("h3 > a")["href"]
    item.select_one("p.text-nowrap > span").decompose()
    data.district = item.select_one("p.text-nowrap").getText()
    return data



# items = soup_gather_homes(const.MAIN_URL)
# if items:
#     keke = [soup_gather_home_data(it) for it in items]
#     for i in keke:
#         print(i)
