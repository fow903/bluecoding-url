import hashlib
import os
from bs4 import BeautifulSoup
import requests
from rest_framework import status
from rest_framework.response import Response

def shorten_url_convert(original_url):
    hash_object = hashlib.md5(original_url.encode())
    hash_hex = hash_object.hexdigest()[:6]
    shortened_url = f'{os.environ.get("SHORTEN_URL")}/s/{hash_hex}'
    return shortened_url

def valid_reponse(data, status=status.HTTP_200_OK):
    return Response(data, status=status)

def invalid_response(data, status=status.HTTP_400_BAD_REQUEST):
    return Response(data, status=status)


def crawl_title(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find('title').string
        return title
    except Exception as e:
        print(e)
        return 'No title found'