"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path, re_path

import mainapp.views as mainapp

urlpatterns = [
    re_path(r"^$", mainapp.main, name="main"),
    re_path(r"^products/", include("mainapp.urls", namespace="products")),
    re_path(r"^contact/", mainapp.contact, name="contact"),
    path("", include("social_django.urls", namespace="social")),
    re_path(r"^auth/", include("authnapp.urls", namespace="auth")),
    re_path(r"^basket/", include("basketapp.urls", namespace="basket")),
    re_path(r"^order/", include("ordersapp.urls", namespace="order")),
    re_path(r"^admin/", include("adminapp.urls", namespace="admin")),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [re_path(r"^__debug__/", include(debug_toolbar.urls))]
