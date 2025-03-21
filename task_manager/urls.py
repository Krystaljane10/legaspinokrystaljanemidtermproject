from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # This includes the tasks app URLs
    path('', RedirectView.as_view(url='/tasks/')),  # Redirect root URL to task list
]