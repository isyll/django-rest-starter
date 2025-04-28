from django.urls import path
from .views import *

urlpatterns = [
    path("login", CustomLoginView.as_view(), name="token_obtain_pair"),
    path("my-endpoint/", MyView.as_view(), name="my_smart_view"),
]
