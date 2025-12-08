def response(success=True, message="", data=None, error=None, status_code=200):
    return {
        "success": success,
        "message": message,
        "data": data,
        "error": error,
        "status_code": status_code
    }