"""shifty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

from attendance.views import RFIDView
from doorbell.views import doorbell
from kiosk_endpoint.views import KioskBackend, ProductOverview, RegisterUser, InsertThemCashMoney, DefaultHomePage
from kiosk_endpoint.views import kiosk_website_login, ExtraLog, Statistics
from shifty import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("accounts/",admin.site.urls),
    path('doorbell', doorbell, name='doorbell'),
    path('rfid', RFIDView.rfid_endpoint, name='rfid'),
    path('testing/',include("testing.urls")),
    path("kiosk",KioskBackend.kiosk_endpoint, name="kiosk_backend"),
    path("products/",ProductOverview.load_page, name="ProductOverview"),
    path("register/",RegisterUser.load_page, name="RegisterUser"),
    path("change_balance/",InsertThemCashMoney.load_page, name="InsertThemCashMoney"),
    path("statistics/",Statistics.load_page, name="Statistics"),
    path("",DefaultHomePage.load_page, name="HomePage"),
    path("login/", kiosk_website_login, name="LoginPage"),
    path("extra_log/", ExtraLog.load_page, name="LoginPage"),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
