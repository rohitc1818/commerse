from django.urls import path
from store.views.order import Orderview
from store.views.home import Home
from store.views.signup import Signup
from store.views.login import Login ,logout
from store.views.cart import Cart
from store.views.checkout import Checkout


urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', Checkout.as_view(), name='check-out'),
    path('order/', Orderview.as_view(), name='order')

]
