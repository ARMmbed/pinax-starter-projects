from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = [
    path("", TemplateView.as_view(template_name="homepage.html"), name="home"),
    path("admin/", include(admin.site.urls)),
    path("blog/", include("pinax.blog.urls", namespace="pinax_blog"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
