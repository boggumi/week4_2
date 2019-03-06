from django.contrib import admin
from django.urls import path, include #인클루드 추가
import blogapp.views
import portfolioapp.views
# media 쓰려면 추가해야함
from django.conf import settings
from django.conf.urls.static import static
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')),
    path('portfolio/', portfolioapp.views.portfolio, name="portfolio"),
    path('accounts/', include('accounts.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# media할때 path추가하는 법
# 이미 settings.py에서 MEDIA_URL = '/media/' 라고 해줬기때문에
# + 추가하는 형식으로 path를 추가함