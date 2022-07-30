from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('name/', include('Product.urls')),
    path('', include('members.urls')),
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# to change the headers of backend panel
admin.site.site_header = "Online Library"
admin.site.site_title = "Online Library"
admin.site.index_title = "UNITED ACADEMY"









