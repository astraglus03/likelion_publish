# context를 넣어서 보내는 건 views.py!
from django.shortcuts import render, redirect
from .models import CategoryBig,CategorySmall, Product,  Payment
#from .forms import SignupForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
#from .forms import CommentForm
from django.shortcuts import get_object_or_404  # db에서 하나만 가져오는 명령어
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect

# index 페이지 (첫 화면)
def index(request):
    return render(
        request,
        'helpyou/index.html',
    )

# # 회원가입
# def signup(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid(): # 회원가입 필드값이 모두 입력되었는지, 비번1,2가 같은지, 등을 검사
#             form.save()
#             # username = form.cleaned_data.get('username')
#             # raw_password = form.cleaned_data.get('password1')
#             # #username = form.cleaned_data.get('username')
#             # user = authenticate(username=username, password=raw_password) #사용자 인증
#             # login(request, user) #로그인
#             return redirect("/login/")
#     else:
#         form = SignupForm()
#         return render(request, 'helpyou/signup.html', {'form':form})



# # 회원가입
# class Signup(ListView):
#     model = SignUp
#
#     template_name = 'helpyou/signup.html'
#     # 1.내가 이름을 바꿔서 지정하거나, 자동으로 연결되는 이름으로 다른 걸 바꾸던가(우린 후자)
#     #template_name = 'blog/post_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(Signup, self).get_context_data()  # lecture_list를 가져옴 # 상위에서 가져오기때문
#         context['categoriesbig'] = CategoryBig.objects.all()  # CategoryBig DB의 내용
#         context['categoriessmall'] = CategorySmall.objects.all()  # CategorySmall DB의 내용
#         #context['no_category_post_count'] = Lecture.objects.filter(
#             #category=None).count()  # category가 없을 수 있기 때문에 no_category이고, 뒤에는 없는 것 카운트
#         return context  # => 리턴은 lecture_list.html로 들어가게 된다.
#
# class Login():

# 상품 (상품 detail)
class ProductDetail(DetailView):
    model = Product
    template_name='helpyou/product_detail.html'
    # 여기는 템플릿 이름을 정의하지 않아서, 자동으로 post.html?을 자동으로 찾음
    # template_name = post_form.html  #post_detail.html로 이름 바꿔서 주석처리하면 자동으로 이름 바뀜

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()  # product_list를 가져옴 # 상위에서 가져오기 때문
        context['categoriesbig'] = CategoryBig.objects.all()  # CategoryBig DB의 내용
        context['categoriessmall'] = CategorySmall.objects.all()  # CategoryBig DB의 내용
        #context['no_category_post_count'] = Post.objects.filter(category=None).count()  # category가 없을 수 있기 때문에 no_category
        # 필터: 검색 조건, count 몇 개가 들어있는지 세는 것
        #context['comment_form'] = CommentForm
        return context  # => 리턴은 lecture_detail.html로 들어가게 된다. (lecture.categoriesbig,mid,small,#no_category_post_count) 값이 넘어가게 됨.



# 카테고리
def category_page(request, slug):  # 과일 등 // 미분류 -> no_category로 가게 됨

    categorybig = CategoryBig.objects.get(slug=slug)
    categorysmall = CategorySmall.objects.get(slug=slug)
    product_list = Product.objects.filter(category=categorybig) #product_list = product.objects.all()이었다면 모든 리스트가 다 나옴

    return render(
        request,
        'helpyou/product_detail.html', # category.html?
        {#context 넣는 위치! 알기 '변수명 : 들어갈 내용'
        #필터링한 것만 뜨게 하기
            'lecture_list': product_list,
            'categoriesbig': CategoryBig.objects.all(),
            'categoriessmall': CategorySmall.objects.all(),
            #'no_category_post_count': Lecture.objects.filter(category=None).count(),
            'categorybig': categorybig,
            'categorysmall': categorysmall,
        }
    )

# 토큰이 검증이 안 될 때 함수 실행 #관리자가 아닌 사용자한테 굳이 메시지를 띄울 필요는 없음.
# 에러 메시지 안 띄우고 바로 이전 페이지로 가게 하기
def crsf_failure(request, reason=""):
    return redirect('/')

# 장바구니
class Cart(DetailView):
    model = Product
    template_name='helpyou/cart.html'
    # 여기는 템플릿 이름을 정의하지 않아서, 자동으로 post.html?을 자동으로 찾음
    # template_name = post_form.html  #post_detail.html로 이름 바꿔서 주석처리하면 자동으로 이름 바뀜
    product = CategorySmall.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Cart, self).get_context_data()  # lecture_list를 가져옴 # 상위에서 가져오기 때문
        context['categoriesbig'] = CategoryBig.objects.all()  # CategoryBig DB의 내용
        context['categoriessmall'] = CategorySmall.objects.all()  # CategoryBig DB의 내용


        #context['no_category_post_count'] = Post.objects.filter(category=None).count()  # category가 없을 수 있기 때문에 no_category
        # 필터: 검색 조건, count 몇 개가 들어있는지 세는 것
        #context['comment_form'] = CommentForm
        return context  # => 리턴은 lecture_detail.html로 들어가게 된다. (lecture.categoriesbig,mid,small,#no_category_post_count) 값이 넘어가게 됨.

# 주문(결제)
class Payment(DetailView):
    model = Product
    template_name='helpyou/payment.html'
    # 여기는 템플릿 이름을 정의하지 않아서, 자동으로 post.html?을 자동으로 찾음
    # template_name = post_form.html  #post_detail.html로 이름 바꿔서 주석처리하면 자동으로 이름 바뀜
    product = CategorySmall.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Payment, self).get_context_data()  # lecture_list를 가져옴 # 상위에서 가져오기 때문
        context['categoriesbig'] = CategoryBig.objects.all()  # CategoryBig DB의 내용
        context['categoriessmall'] = CategorySmall.objects.all()  # CategoryBig DB의 내용


        #context['no_category_post_count'] = Post.objects.filter(category=None).count()  # category가 없을 수 있기 때문에 no_category
        # 필터: 검색 조건, count 몇 개가 들어있는지 세는 것
        #context['comment_form'] = CommentForm
        return context  # => 리턴은 lecture_detail.html로 들어가게 된다. (lecture.categoriesbig,mid,small,#no_category_post_count) 값이 넘어가게 됨.
