from django.urls import path
from . import views


app_name = 'rcdapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('form_page/', views.form_page, name='form_page'),
    path('form_list/', views.form_list, name='form_list'),
    path('form_update/<int:id>', views.form_update, name='form_update'),
    path('delete_user/<int:id>', views.delete_user, name='delete_user'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('backup/', views.backup, name='backup'),
]