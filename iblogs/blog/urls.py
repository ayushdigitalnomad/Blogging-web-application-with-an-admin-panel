from django.contrib import admin
from django.urls import path,include
from .views import home,post,category
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category)
]