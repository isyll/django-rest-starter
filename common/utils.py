from rest_framework.response import Response


def standard_response(success=True, message="", data=None, status_code=200):
    if data is None:
        data = {}

    return Response(
        {
            "success": success,
            "status": status_code,
            "message": message,
            "data": data,
        },
        status=status_code,
    )
