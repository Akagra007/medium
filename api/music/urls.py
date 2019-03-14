from django.urls import path,include
from music.views import ListSongsView

urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all")
]


