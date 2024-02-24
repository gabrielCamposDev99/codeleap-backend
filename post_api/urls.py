from django.urls import path
from post_api.views import Posts, PostDetail

urlpatterns = [
    path('', Posts.as_view()),
    path('<str:pk>', PostDetail.as_view())
]