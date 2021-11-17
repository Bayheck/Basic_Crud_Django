from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.user_form,name='user_insert'),
    path('list/', views.user_list,name='user_list'),
    path('<str:email>/', views.user_form, name = 'user_update'),
    path('delete/<str:email>/', views.user_delete, name='user_delete')
]
