from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta): # UCF 상속, model만 내것으로수정하고 나머지 그대로
        model = get_user_model()
        

class CustomAuthenticationForm(AuthenticationForm):
    pass