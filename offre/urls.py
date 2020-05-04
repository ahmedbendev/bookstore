from django.urls import path
from . import views
from .views import Createoffer,Offredetail,Useroffers,Deleteoffre,Aproveoffer,Refuseoffer,Contactoffer,Doneoffer
urlpatterns = [
    path("create/<int:pk>/",views.Createoffer,name="create-offer"),
    path('<int:pk>/',views.Offredetail,name='offer-detail'),
    path('<int:pk>/delete',views.Deleteoffre,name='offer-delete'),
    path("useroffers/<str:username>/",views.Useroffers,name="useroffers"),
    path("<int:id>/approved",views.Aproveoffer,name="offer-approve"),
    path("<int:id>/refuse",views.Refuseoffer,name="offer-refuse"),
    path("<int:id>/contact",views.Contactoffer,name="offer-contact"),
    path("<int:id>/done",views.Doneoffer,name="offer-done"),
]
