"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import home, about, show_article, media, show_post, hot, contacts, lab_3, lab_4

urlpatterns = [
                  url(r'^$', home, name='home'),
                  url(r'^about/', about, name='about'),
                  url(r'^article/(?P<article_id>[0-9]+)/$', show_article, name='article'),
                  url(r'^post/(?P<post_id>[0-9]+)/$', show_post, name='post'),
                  url(r'^hot/', hot, name='hot'),
                  url(r'^contacts/', contacts, name='contacts'),
                  url(r'^lab_3/', lab_3, name='lab_3'),
                  url(r'^lab_4/', lab_4, name='lab_4'),
                  # url(r'^media/$', media, name='media'), # {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
