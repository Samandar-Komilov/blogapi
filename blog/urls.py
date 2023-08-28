from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("posts.urls")),
    # Rest frameworkning default login-logout page
    path("api-auth/", include("rest_framework.urls")),
]
