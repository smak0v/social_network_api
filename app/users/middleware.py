from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()


class SetUserLastRequestMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            User.objects.filter(pk=request.user.pk).update(last_request=now())
        return response
