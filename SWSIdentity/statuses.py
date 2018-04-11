status = {
    0: {'message': 'Success'},
    1: {'message': 'Auth fail'},
    2: {'message': 'Email already registered'},
    7: {'message': 'Invalid token'},
}


def get_status(code):
    """Return complete message by status ID"""
    return {'code': code, 'message': status[code]['message']}
