from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import register #customize with the name of the function created
from wishlist.views import login_user #customize with the name of the function created
from wishlist.views import logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]