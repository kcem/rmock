"""
    Collection of tools which may be used as a param_parser http protocol params
"""

import urlparse


def rest_params_parser(method, parsed_url, body):
    """
    Parse parameters of a REST HTTP call.

    This procedure treats the HTTP resource's path as a function name.
    The HTTP method becomes that function's first argument. If we're
    dealing with a POST or PUT request, there is a second argument: raw
    request body. The function's keyword arguments are generated by
    parsing the request's query string.
    """
    #TODO: add support for body params
    if method in ('post', 'put'):
        args = (method, body)
    else:
        args = (method, )

    kwargs = {
        name: values if len(values) >= 2 else values[0]
        for (name, values) in urlparse.parse_qs(parsed_url.query).iteritems()
    }

    return parsed_url.path, args, kwargs
