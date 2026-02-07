
def success(message: str, data=None):
    return {
        "success": True,
        "message": message,
        "data": data
    }

def error(message: str):
    return {
        "success": False,
        "message": message
    }
