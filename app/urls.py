from django.urls import path
from .views import *

urlpatterns = [
    path('', UserListView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
