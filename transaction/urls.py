from django.urls import path
from . import views 
urlpatterns = [
    path('', views.homeFn, name='homepage'),
    path('delete/<uuid:id>/', views.delete_transaction, name='delete_tr'),
]