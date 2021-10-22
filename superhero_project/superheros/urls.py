from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'superheros'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('edit/<int:hero_id>/', views.edit, name='edit'),
    path('delete/<int:hero_id>', views.delete, name='delete')
]

urlpatterns += staticfiles_urlpatterns()