from django.urls import path
from . import views
urlpatterns = [
      path('',views.index,name='index'),
      path('personform_page/', views.personform_page, name='personform_page'),
      path('logout/',views.logout,name='logout'),
]