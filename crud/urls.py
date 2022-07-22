from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<slug:post_slug>', views.read, name='detail'),
    path('delete/<int:post_id>', views.delete, name='delete'),
    path('update/<int:post_id>', views.update, name='update')
    # path('', views.PostListView.as_view(), name='index'),
    # path('create/', views.PostCreateView.as_view(), name='create'),
    # path('detail/<slug:post_slug>', views.PostDetailView.as_view(), name='detail'),
    # path('delete/<int:post_id>', views.PostDeleteView.as_view(), name='delete'),
    # path('update/<int:post_id>', views.PostUpdateView.as_view(), name='update')

]