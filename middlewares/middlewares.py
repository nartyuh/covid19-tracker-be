class CorsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = 'https://covid19geotracker.tranquanghuy.me'
        # response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Methods'] = 'PUT, POST, GET, DELETE, OPTIONS'
        response['Access-Control-Max-Age'] = 86400

        return response