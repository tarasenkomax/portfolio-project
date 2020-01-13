from django.contrib import admin
from django.urls import path, include   # Add
from django.conf import settings  # Add
from django.conf.urls.static import static  # Add
import jobs.views  # Add

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', jobs.views.home, name='home'),  # Домашняя страница
                  path('portfolio/', include('blog.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Для просмотра медиа файлов
