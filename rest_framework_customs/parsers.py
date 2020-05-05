from rest_framework.parsers import BaseParser
import ast

class PlainTextParser(BaseParser):

    """
    Plain text parser.
    """
    media_type = 'text/plain;charset=UTF-8'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        byte_str = stream.read()
        dict_str = byte_str.decode("UTF-8")
        data = ast.literal_eval(dict_str)

        return data