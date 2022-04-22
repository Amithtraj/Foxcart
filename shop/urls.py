from django.urls import path
from . import views

urlpatterns=[
    path('<slug:c_slug>/<slug:product_slug>',views.details,name='details'),
    path('',views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('search',views.searching,name='search'),
]