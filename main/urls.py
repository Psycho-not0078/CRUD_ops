from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.create),
    path('functs', views.init_functs.as_view()),
    path('edit/<int:id>', views.editer.as_view()),
    path('edit', views.edit),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
