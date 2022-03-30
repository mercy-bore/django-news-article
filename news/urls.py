from django.urls import re_path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views 
from . import views
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    re_path(r'^$',views.news_today,name='newsToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^article/(\d+)',views.article,name ='article'),
    re_path('accounts/', include('django_registration.backends.one_step.urls')),
    re_path('accounts/register/',
        RegistrationView.as_view(success_url='/profile/'),
        name='django_registration_register'),
    # re_path(r'^logout/$', views.logout, {"next_page": '/'}), 
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^new/article$', views.new_article, name='new-article'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

