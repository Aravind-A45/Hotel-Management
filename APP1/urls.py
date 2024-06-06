from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('ordered_foods/', views.ordered_foods, name="ordered_foods"),
    path('add_product/', views.add_product, name="add_product"),
    path('payment/', views.payment, name="payment"),
    path('about/', views.about, name="about"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)