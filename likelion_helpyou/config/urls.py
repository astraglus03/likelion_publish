from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('helpyou.urls')),
    #path('accounts/', include('allauth.urls')),  # allauth 패키지가 알아서 처리함. /accout/signin/ 등 알아서 연결됨
                                                 # 회원가입, 로그인
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)