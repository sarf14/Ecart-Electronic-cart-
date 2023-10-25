from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    # path("signup/", views.register_request, name="signup")
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
]
