from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import api.api_views
import api.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/projects/', api.api_views.ProjectList.as_view()),
    path('api/images/', api.api_views.ImageList.as_view()),
    path('api/tags/', api.api_views.TagList.as_view()),
    path('api/detailbodies/', api.api_views.DetailBodyList.as_view()),
    path('api/projects/new/', api.api_views.ProjectCreate.as_view()),
    path('api/images/new/', api.api_views.ImageCreate.as_view()),
    path('api/tags/new/', api.api_views.TagCreate.as_view()),
    path('api/detailbodies/new/', api.api_views.DetailBodyCreate.as_view()),
    path('api/projects/<int:id>/', api.api_views.ProjectRetrieveUpdateDestroy.as_view()),
    path('api/images/<int:id>/', api.api_views.ImageRetrieveUpdateDestroy.as_view()),
    path('api/tags/<int:id>/', api.api_views.TagRetrieveUpdateDestroy.as_view()),
    path('api/detailbodies/<int:id>/', api.api_views.DetailBodyRetrieveUpdateDestroy.as_view()),

    path('', api.views.home, name='home'),
    path('projects/', api.views.projects, name='projects'),
    path('projects/<int:project_id>', api.views.detail, name='detail'),
    path('contactme/', api.views.contact, name='contact'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
