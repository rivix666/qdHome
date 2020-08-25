""" TODO """

import requests
from bs4 import BeautifulSoup

# TODO fix this later
# Some dependency problems that occures when this script is called from
if __name__ == "__main__":
    import const
    from models.home_data import HomeData
else:
    from . import const
    from .models.home_data import HomeData


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
    data.rooms = item.select_one(".offer-item-rooms").getText()
    data.area = item.select_one(".offer-item-area").getText()
    data.desc_url = item.select_one("h3 > a")["href"]
    item.select_one("p.text-nowrap > span").decompose()
    data.district = item.select_one("p.text-nowrap").getText()
    data.price = item.select_one(".offer-item-price").getText()

    # Sometimes price per m is not set directly in the offer, so we need to be prepared that it can be None
    tmp = item.select_one(".offer-item-price-per-m")
    data.m_price = tmp.getText() if tmp else -1
    return data


def soup_last_page(url):
    response = request_response(url)
    if response:
        soup = BeautifulSoup(response.text, "html.parser")
        return max([int(it.getText()) for it in soup.select("ul.pager li a") if it.getText()])


def return_page_home_data(page_url):
    items = soup_gather_homes(page_url)
    return [soup_gather_home_data(it) for it in items] # TODO very often we got here NoneType exception


def return_home_generator():
    last_page = soup_last_page(const.MAIN_URL)

    # Create Generator Expression
    return (return_page_home_data(f"{const.MAIN_URL}{const.PAGE_PARAM}{num}") for num in range(1, last_page))

