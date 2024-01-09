from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app.urls')),
    path('accounts/',include('accounts.urls')),
    


    # TODO: implement it for v2
    # path('auth/',include('rest_framework.urls')),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
