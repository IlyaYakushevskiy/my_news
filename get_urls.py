import requests
import dateutil.parser
from datetime import datetime, timedelta, timezone
import re
from lxml import etree

_sitemap_url = "https://www.nasaspaceflight.com/post-sitemap6.xml"
_response = requests.get(_sitemap_url)
_article_page_pattern = re.compile("https://www\.nasaspaceflight\.com/[0-9]{4}/[0-9]{2}/.*")
_namespaces = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def _is_request_successful(response_):
    return response_.status_code == 200


def _is_within_time_frame(lastmod, day_delta):
    if lastmod is None:
        return False
    comp_datetime = datetime.now(timezone.utc) - timedelta(days=day_delta)
    datetime_obj = dateutil.parser.isoparse(lastmod)
    return datetime_obj >= comp_datetime


def _is_article(url):
    return re.match(_article_page_pattern, url) is not None


def get_recent_urls(day_delta=1):
    recent_urls = []
    if _is_request_successful(_response):
        tree = etree.fromstring(_response.content)
        url_elements = tree.xpath("//ns:url", namespaces=_namespaces)
        for element in url_elements:
            lastmod = element.find('ns:lastmod', namespaces=_namespaces).text
            url = element.find('ns:loc', namespaces=_namespaces).text
            if _is_within_time_frame(lastmod, day_delta) and _is_article(url):
                recent_urls.append(url)
    else:
        raise Exception("XML request not successful")
    return recent_urls

if __name__ == "__main__":
    urls = get_recent_urls(1)
    print(urls)
