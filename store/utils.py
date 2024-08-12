
from django.contrib.auth import get_user_model
def authenticate_custom_user(request, username, password):
    MyUser = get_user_model()
    try:
        user = MyUser.objects.get(username=username)
        if user.check_password(password):
            return user
    except MyUser.DoesNotExist:
        return None
    return None


import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
