from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home-page'),
    path('admin/', admin.site.urls),
    path('wallet/', include("wallet.urls")),
    path('account/', include('account.urls')),
    path('api/', include('api.urls')),
    path('budget/', include('budget.urls')),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
