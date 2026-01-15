from django.urls import path
from . import views 

app_name = "transaction"
urlpatterns = [
    path('', views.homeFn, name='homepage'),
    path('delete/<uuid:id>/', views.delete_transaction, name='delete_tr'),
]