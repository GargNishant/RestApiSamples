from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib.auth.models import AnonymousUser
from django.utils.functional import SimpleLazyObject

from user_manage import models


def get_user(request):
    if not hasattr(request, '_cached_user'):
        # HTTP_EMAIL will see "email" in the Headers of request
        email = request.META.get('HTTP_EMAIL', None)
        request._cached_user = get_user_from_email(email) or AnonymousUser()
        if isinstance(request._cached_user, AnonymousUser):
            print("Email Is:",email)
    return request._cached_user


def get_user_from_email(email):
    try:
        user = models.User.objects.get(email=email)
        # is_active attribute is needed for AuthMiddleware to work.
        user.is_active = True
        return user
    except Exception as e:
        raise ValueError(e)


class CustomAuthMiddleware(AuthenticationMiddleware):
    def process_request(self, request):
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'user_manage.auth_middleware.CustomAuthMiddleware'."
        )
        request.user = SimpleLazyObject(lambda: get_user(request))