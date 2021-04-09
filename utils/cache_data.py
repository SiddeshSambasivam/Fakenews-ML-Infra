import json
import functools
from flask import request

def cache(function):

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        
        sents = request.get_json(force=True)['sents']
        local_cache = dict()

        for sent in sents:
            if cached_data.get("sent"):
                local_cache[sent] = cached_data.get("sent")
                continue
        
        return function(*args, **kwargs, cached_data=cached_data)

    return wrapper