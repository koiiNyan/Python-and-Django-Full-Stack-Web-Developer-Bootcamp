from django.urls import path, include
from AppTwo import views

urlpatterns = [
    path('', views.index, name="index"),
    path('help/', views.help, name='help'),
    path('users/', views.users, name='users'),
]

from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/',include(debug_toolbar.urls))
    ] + urlpatterns
    
