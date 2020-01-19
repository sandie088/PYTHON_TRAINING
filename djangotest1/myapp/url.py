from django.conf.urls import include, url

from myapp import views as myapp_views

urlpatterns = [
    url(r'^hello/', myapp_views.hello, name='hello'),
    url(r'^contact/', myapp_views.contact, name='contact'),
    url(r'^article/(\d+)/', myapp_views.article, name='article')
]
