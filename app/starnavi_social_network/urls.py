"""
starnavi_social_network URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from .api_views import AnalyticsView

v1 = ([
          path('users/', include('users.urls')),
          path('posts/', include('posts.urls')),
          path('analytics/', AnalyticsView.as_view(), name='analytics'),
      ], 'v1')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1)),
]
