from django.conf.urls import include

urlpatterns = []

urlpatterns += [
    url(r'^catalog/', include('catalog.urls')),
]