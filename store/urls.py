from django.urls import path
from . import views
from .views import (
                   LatestbookshomeListView,NewbookshomeListView,UsedbookshomeListView,
                   choose_categories_home,LangaguesengbookhomeListView,LangaguesarbbookhomeListView,
                   LangaguesfrebookhomeListView,LangaguesothbookhomeListView,categories_books,choose_region_home,
                   choose_region_home,search_book,Advancedsearch_bookresult,Advancedsearch_book,createusedbook,
                   Newbookdetail,Usedbookdetail,userusedbooks,Updateusedbook,Deleteusedbook,Wishlistuser,Wishlistremove,
                   contactusView, successView,Wishlistadd,about
)
urlpatterns = [
    path('', views.LatestbookshomeListView.as_view(),name='store-home'),
    path('newbooks/', views.NewbookshomeListView.as_view(),name='newbook-home'),
    path('newbook/<int:pk>/',views.Newbookdetail,name='newbook-detail'),
    path('usedbooks/', views.UsedbookshomeListView.as_view(),name='usedbook-home'),
    path('usedbook/<int:pk>/',views.Usedbookdetail,name='usedbook-detail'),
    path('usedbook/<int:pk>/update',views.Updateusedbook,name='usedbook-update'),
    path('usedbook/<int:pk>/delete',views.Deleteusedbook,name='usedbook-delete'),
    path('categories/', views.choose_categories_home,name='categories-home'),
    path('categories/<int:pk>/',views.categories_books,name='genredetail-home'),
    path('langagues/englishbooks', views.LangaguesengbookhomeListView.as_view(),name='langagueseng-home'),
    path('langagues/arabicbooks', views.LangaguesarbbookhomeListView.as_view(),name='langaguesarb-home'),
    path('langagues/frenchebooks', views.LangaguesfrebookhomeListView.as_view(),name='langaguesfre-home'),
    path('langagues/otherbooks', views.LangaguesothbookhomeListView.as_view(),name='langaguesoth-home'),
    path('regions/', views.choose_region_home,name='regionusedbook-home'),
    path('chooseregion/<int:pk>/',views.region_books,name='regiondetail-home'),
    path("search_book/",views.search_book,name="search_book"),
    path("advancedsearch/",views.Advancedsearch_book,name="advancedsearch"),
    path("advancedsearch_bookresult/",views.Advancedsearch_bookresult,name="advancedsearch_bookresult"),
    path("createusedbook/",views.createusedbook,name="createusedbook"),
    path("userusedbooks/<str:username>/",views.userusedbooks,name="userusedbooks"),
    path('wishlist/<str:username>/',views.Wishlistuser,name='wishlistuser'),
    path('wishlist/<int:pk>/delete',views.Wishlistremove,name='wishlistremove'),  
    path('wishlist/addwishlist',views.Wishlistadd,name='wishlistadd'),    
    path('contactus/', contactusView, name='contactus'),
    path('success/', successView, name='success'),
    path('about/',views.about,name='store-about'),
    
]
