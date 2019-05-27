import json
from flask import Response

# Error Codes
UNEXPECTED = 1
OK = 0
NOT_LOGGED_IN = -1
AUTHORIZE_FAILED = -2
PERMISSION_DENIED = -3
INFORMATION_INCOMPLETE = -4

# Send JSON as response to Client
def JSON(data) :
    return Response(
      json.dumps(data),
      mimetype = 'application/json'
    )

# Send Error info as response to Client
def error(i, **detail) :
    res = {'code': i}
    if i == OK :
        res['msg'] = 'Everything OK.'
    elif i == NOT_LOGGED_IN :
        res['msg'] = 'Not logged in.'
    elif i == AUTHORIZE_FAILED :
        res['msg'] = 'Authorize failed.'
    elif i == PERMISSION_DENIED :
        res['msg'] = 'Permission denied.'
    elif i == INFORMATION_INCOMPLETE :
        res['msg'] = 'Information incomplete.'
    else :
        res['msg'] = 'Unexpected exception.'
    if (detail) :
        res['detail'] = detail
    return JSON(res)