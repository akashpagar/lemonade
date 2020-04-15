import traceback

from common.utils import ForcedResponse
import logging

class ForceResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def process_exception(request, response):
        logger = logging.getLogger('django')

        if isinstance(response, ForcedResponse):
            log_message = "\"{0} {1}\" {2}\n{3}".format(request.method, request.get_full_path(), 200,
                                                        traceback.format_exc())
            # logger.error(log_message)
            print(log_message)
            return response.response

class ResponseFormatMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 500:
            print('in 500 ')
            return response
        if response.status_code == 400:
            pass
        return response
