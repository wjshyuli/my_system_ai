import requests
from lxml import etree

def getnews_of_rubber():
    result='rubber'
    url = 'https://tyre.cria.org.cn/'
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    html = etree.HTML(response.text)


    a = html.xpath('//div[contains(@class,"flex-item gw-index-notices-tabs-content-item-content-main")]//text()')

    result = [i.strip() for i in a if i.strip()]




    return result

def getnews_of_gov():
    result='gov'
    return result


if __name__ == '__main__':
    print(getnews_of_rubber())


