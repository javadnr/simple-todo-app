from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view(),name="list"),
    path('<int:pk>/detail/',views.PostDetailView.as_view(),name='post_detail'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(),name="post_update"),
    path('<int:pk>/delete/',views.PostDeleteView.as_view(),name="post_delete"),
]
