# File: api/modules/authentication.py

from starlette.requests import Request

def get_current_user(request: Request):
    # Replace this with your actual session authentication logic
    # You may need to access the session data or cookies to check authentication
    # For example, you can check if a user ID is present in the session data
    user = request.session.get("user")
    if user is None:
        return None  # User is not authenticated
    return user  # Return the authenticated user