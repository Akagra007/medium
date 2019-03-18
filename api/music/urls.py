from django.urls import path,include
from music.views import ListSongsView, ListSongsDetail

urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('songs/<int:pk>/', ListSongsDetail.as_view(), name="songs-all-details")
]


