# django-blogapp
##### Basic Blog Django App

## Installation Instructions

#### Project Folder

##### urls.py
###### should look exactly like:

    from django.conf.urls import url, include
    from django.contrib import admin
    from blog import views

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^$', views.index, name='index'),
        url(r'^blog/', include('blog.urls')),
    ]

##### settings.py 
###### add 'blog' in installed apps
###### add static url

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
    ]

    STATIC_URL = '/static/'
