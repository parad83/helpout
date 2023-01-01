from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.forms import ValidationError

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()    # gets current User model
        try:
            user = UserModel.objects.get(email=email)   # looks for user with given mail
            if user.check_password(password):           # validates password
                return user
            else:
                raise ValidationError({'password': ["Incorrect password!"]})
        except UserModel.DoesNotExist:          # if user with given email doesnt exist an error is raised to field password
            raise ValidationError({'password': ["We couldn't find account with given cridentials 🙁"]})