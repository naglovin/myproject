import logging
from django.http import HttpResponse  # возвращает шттп ответ от сервера к клиенту

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def about(request):
    try:
        # некоторый код, который может возникнуть как исключение
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error on the About page": {e}')
        return HttpResponse(" Oops, something went wrong.")
    else:
        logger.debug('Information about the visited page')
    return HttpResponse("This is a page about the company")
