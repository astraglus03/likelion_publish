
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('helpyou.urls')),
    #path('accounts/', include('allauth.urls')),  # allauth 패키지가 알아서 처리함. /accout/signin/ 등 알아서 연결됨
                                                 # 회원가입, 로그인
]
