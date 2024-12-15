from django.urls import path
from .views import blogView,homeView, singlelView


urlpatterns =[
    path('', homeView, name="home"),
    path('blog/', blogView, name="blog"),
    path('blog/<int:pk>/', singlelView, name="single"),

]
