from django.urls import path
from .views import *
 
urlpatterns = [
    path('current_user/', Current_user.as_view()),
    # path('users/', UserList.as_view()),

]