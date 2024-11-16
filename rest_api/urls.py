from django.urls import path
from .views import PostAPIView, PostdetailsAPIView

urlpatterns = [
    #path('posts/', Postview),
    #path('details/<int:pk>', posts_detail),
    path('postsapiview/', PostAPIView.as_view()),
    path('detailsapiview/<int:pk>', PostdetailsAPIView.as_view()),
]
