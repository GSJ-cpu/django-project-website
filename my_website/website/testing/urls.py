from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")), # allows us to access the URLconf's from the app
    path('testing/', views.Home.as_view(), name='say_hello'),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('search/', views.index, name='index'),
    path("about/",views.about_page),
    path("account/",views.account_page),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)