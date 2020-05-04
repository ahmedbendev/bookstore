from django.urls import path
from . import views
from .views import Addtocart,Mycarte,Myorders,Addquantity,Removequantity,Removebookorder,Checkout
urlpatterns = [
    path("addtocart/<int:pk>/",views.Addtocart,name="newbook-addtocart"),
    path("mycarte/<str:username>/",views.Mycarte,name="mycarte"),
    path("myorders/<str:username>/",views.Myorders,name="myorders"),
    path("mycarte/<int:pk>/addquantity",views.Addquantity,name="bookorderaddquantity"),
    path("mycarte/<int:pk>/removequantity",views.Removequantity,name="bookorderremovequantity"),
    path("mycarte/<int:pk>/removebookorder",views.Removebookorder,name="bookorderremove"),
    path("mycarte/<int:pk>/checkout",views.Checkout,name="checkout"),
]
