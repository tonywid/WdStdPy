#!/usr/bin/python3

import os
import sys
from typing import Tuple
from urllib.parse import parse_qs

def getbody() ->  Tuple[int, str]:
    # Read Content-Length header
    length = int(os.environ.get("CONTENT_LENGTH", 0))
    print ("length: ", length)
    # Read raw body
    body = sys.stdin.read(length)
    ret_list = [length, body]
    return ret_list


# returns a dict
def parse_query_params():
    mem_request_uri = os.environ.get("REQUEST_URI")
    if mem_request_uri is not None:
        path, _, query_string = mem_request_uri.partition('?')
        params = parse_qs(query_string)
        # parse_qs returns values as lists, so simplify:
        return {k: v[0] if len(v) == 1 else v for k, v in params.items()}
        # Example: {"a": [10]} becomes {"a": 10}
        # Example: {"b": [1, 2, 3]} stays {"b": [1, 2, 3]}
        # https://dev.to/hexshift/handling-url-query-parameters-in-a-lightweight-python-web-framework-54dm

    # for Python http.server
    query_string = os.environ.get("QUERY_STRING")
    params = parse_qs(query_string)
    # parse_qs returns values as lists, so simplify:
    return {k: v[0] if len(v) == 1 else v for k, v in params.items()}
    # Example: {"a": [10]} becomes {"a": 10}
    # Example: {"b": [1, 2, 3]} stays {"b": [1, 2, 3]}
    # https://dev.to/hexshift/handling-url-query-parameters-in-a-lightweight-python-web-framework-54dm

def getrequestmethod():
    temp_method = os.environ.get("REQUEST_METHOD")
    return temp_method




