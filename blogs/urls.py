from django.urls import path
from blogs.views import BlogsView, BlogDetailView

urlpatterns = [
    path('', BlogsView.as_view(), name='blogs'),
    path('blog/<int:id>/', BlogDetailView.as_view(), name='blog-detail')
]
