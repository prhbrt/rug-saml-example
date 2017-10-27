from django.conf.urls import url, include
from django.contrib import admin

import django_saml2_auth.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^saml2/auth/', include('django_saml2_auth.urls')),
    url(r'^accounts/login/$', django_saml2_auth.views.signin),
    url(r'^admin/login/$', django_saml2_auth.views.signin),
]

