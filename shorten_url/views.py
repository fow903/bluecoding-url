from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view

from shorten_url.models import ShortenUrl
from .utils.util import crawl_title, invalid_response, shorten_url_convert, valid_reponse

@api_view(['POST'])
def shorten_url(request):
    if request.method == 'POST':
        try:
            original_url = request.data.get('original_url')

            if original_url is None:
                return invalid_response('original_url is required', status.HTTP_400_BAD_REQUEST)
            

            shorten_url_obj = ShortenUrl.objects.filter(original_url=original_url).first()
            if shorten_url_obj:
                return valid_reponse(
                    {
                        'shorten_url': shorten_url_obj.shorten_url,
                        'original_url': original_url
                    }, status.HTTP_200_OK)
            
            page_title = crawl_title(original_url)
            shorten_url = shorten_url_convert(original_url)
            shorten_url_obj = ShortenUrl.objects.create(
                original_url=original_url,
                shorten_url=shorten_url,
                page_title=page_title
            )
            shorten_url_obj.save()
            return valid_reponse(
                {
                    'shorten_url': shorten_url,
                    'original_url': original_url
                }, status.HTTP_201_CREATED)
        
        except Exception as e:
            return invalid_response(f'There was an error ${e}', status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return invalid_response('Method not allowed', status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['GET'])
def get_original_url(request, **kwargs):
    if request.method == 'GET':
        try:
            shortened_url = kwargs.get('shortened_url')
            shorten_url_obj = ShortenUrl.objects.get(shorten_url__contains=shortened_url)
            shorten_url_obj.visit_count += 1
            shorten_url_obj.save()
            return redirect(shorten_url_obj.original_url)
        except ShortenUrl.DoesNotExist:
            return invalid_response('Shorten url does not exist', status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return invalid_response(f'There was an error ${e}', status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return invalid_response('Method not allowed', status.HTTP_405_METHOD_NOT_ALLOWED)
        

@api_view(['GET'])
def get_top_visited_urls(request):
    if request.method == 'GET':
        try:
            top_visited_urls = ShortenUrl.objects.order_by('-visit_count')[:100]
            return valid_reponse(
                {
                    'top_visited_urls': top_visited_urls.values()
                }, status.HTTP_200_OK)
        except Exception as e:
            return invalid_response(f'There was an error ${e}', status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return invalid_response('Method not allowed', status.HTTP_405_METHOD_NOT_ALLOWED)