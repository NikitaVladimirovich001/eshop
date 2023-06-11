from django.contrib.auth.backends import ModelBackend

from auth.models import CustomUser


class EmailAuthBackends(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser(email=username)
            if user.check_password(raw_password=password):
                return user
        except CustomUser.DoesNoExist:
            pass

        def get_user(self, user_id):
            try:
                return CustomUser.object.get(id=user_id)
            except CustomUser.DoesNotExist:
                pass