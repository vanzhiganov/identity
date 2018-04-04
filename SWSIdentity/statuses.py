status = {
    0: {'message': 'Success'},
    1: {'message': 'Auth fail'},
    7: {'message': 'Invalid token'},
    # Zones
    1001: {'message': 'Invalid source URL'},
    1002: {'message': 'Invalid alias'},
    1003: {'message': 'Dab code Received from source server'},
    1004: {'message': 'Server not responding'},
}

def get_status(code):
    """Return complete message by status ID"""
    return {'code': code, 'message': status[code]['message']}
