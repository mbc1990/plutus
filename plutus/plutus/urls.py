from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'plutus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^plutus_core/', include('plutus_core.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
