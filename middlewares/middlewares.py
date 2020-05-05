class CorsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = 'https://covid19geotracker.tranquanghuy.me'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Methods'] = '*'

        return response