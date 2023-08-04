from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='helpyou'

urlpatterns = [
    path('', views.index),  # 첫 화면(메인페이지)
    #path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='helpyou/login.html'), name='login'), # 로그인
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # 로그아웃
    # path('category/{self.categorybig}/{self.categorysmall}', views.category_page),  # 카테고리/과일/사과
    path('category/<str:categorybig>/<str:categorysmall>/<int:pk>/', views.ProductDetail.as_view()), # 카테고리/사과/과일/pk번호
    path('cart/<int:pk>/', views.Cart.as_view()),                   # 장바구니
    path('payment/<int:pk>/', views.Payment.as_view()),         # 결제
    # path('mypage/', views.MyPage.as_view()),           # 마이페이지

#     path('search/<str:q>/', views.PostSearch.as_view()),               #게시물 검색
#     path('<int:pk>/new_comment/', views.new_comment),                  #새로운 댓글 작성
#     path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),   #댓글 수정
#     path('delete_comment/<int:pk>/', views.delete_comment),            #댓글 삭제
#
#     path('', views.PostList.as_view()),  # blog/views.py 에서 클래스를 이용할 때는 이렇게 코드 바꾸기
#     path('<int:pk>/', views.PostDetail.as_view()), #상세페이지
#     path('category/<str:slug>/', views.category_page),  # 뒤에 괄호 있으면 class, 없으면 함수 가져온다
#     path('created_post/', views.PostCreate.as_view()), # PostCreate 클래스를 참조해라.
#     path('update_post/<int:pk>/', views.PostUpdate.as_view()), #PostUpdate 클래스를 참조해라
]