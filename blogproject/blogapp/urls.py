from django.urls import path
from . import views
# from . import views 와 똑같음

urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create', views.create, name="create"),
    path('newblog/', views.blogpost, name="newblog"),
]