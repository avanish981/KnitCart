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
    path("product/",views.product,name="product"),
    #path("product/",views.product,name="product"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.log_in),
    path("log_out/",views.log_out,name="log_out"),
    path("account/",views.account,name="account")
]
