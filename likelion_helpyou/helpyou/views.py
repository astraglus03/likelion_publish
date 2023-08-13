# context를 넣어서 보내는 건 views.py!
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import CategoryBig,CategorySmall, Product,  Payment
import bcrypt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
#from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# 인덱스 페이지 (첫 화면)
class Index(ListView):
    model = Product
    template_name = "helpyou/index.html"

    # 카테고리
    def category_page(request, slug1, slug2):  # 과일 등 // 미분류 -> no_category로 가게 됨
        if slug1 == '과일':
            categorybig = CategoryBig.objects.get(slug=slug1)
            big_list = Product.objects.filter(categorybig=categorybig)
        elif slug1 == '쌀잡곡':
            categorybig = CategoryBig.objects.get(slug=slug1)
            big_list = Product.objects.filter(categorybig=categorybig)
        else:
            categorybig = CategoryBig.objects.get(slug=slug1)
            big_list = Product.objects.filter(categorybig=categorybig)

        if slug2 != 'no_categorysmall':
            categorysmall = CategorySmall.objects.get(slug=slug2)
            product_list = Product.objects.all()
        # product_list = Product.objects.filter(category=categorybig) #product_list = product.objects.all()이었다면 모든 리스트가 다 나옴

        return render(
            request,
            'helpyou/category.html',  # category.html?
            {  # context 넣는 위치! 알기 '변수명 : 들어갈 내용'
                # 필터링한 것만 뜨게 하기
                'big_list': big_list,
                'product_list': product_list,
                'categoriesbig': CategoryBig.objects.all(),
                'categoriessmall': CategorySmall.objects.all(),
                'categorybig': categorybig,
                'categorysmall': categorysmall,

            }
        )
# -------------------------- 종혜: 아이디 중복확인까지 코드 추가 ----------------------------------
def signup(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            error_message1 = '이미 사용중인 아이디입니다 아이디를 확인하고 로그인 해주세요.'
            return render(request, 'helpyou/signup.html',{'error_message1': error_message1})
        #현아 추가 : 아이디 중복되었으면 오류나지 않고 다시 회원가입 페이지로 돌아갈 수 있도록 함
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            return redirect('/login') #현아 수정 : 회원가입하고 메인페이지로 이동하면 로그인,회원가입 버튼 뜨는것이 아니라 바로 로그아웃, 반갑습니다 가 뜸
        #회원가입 성공하면 바로 로그인 페이지로 이동할 수 있게 수정함

        return render(request, 'helpyou/signup.html')
    return render(request, 'helpyou/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            error_message = '아이디나 비밀번호가 다릅니다.'
            return render(request, 'helpyou/login.html', {'error_message': error_message})
    else:
        return render(request, 'helpyou/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def check_duplicate_id(request):
    user_id = request.GET.get('id')
    exists = User.objects.filter(username=user_id).exists()
    return JsonResponse({'exists': exists})

# --------------------------------------- 여기까지 -----------------------------------

# 상품 (상품 detail)
class ProductDetail(DetailView):
    model = Product
    template_name='helpyou/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()  # product_list를 가져옴 # 상위에서 가져오기 때문
        context['categoriesbig'] = CategoryBig.objects.all()  # CategoryBig DB의 내용
        context['categoriessmall'] = CategorySmall.objects.all()  # CategoryBig DB의 내용
        return context




class Category(ListView):
    model=Product
    template_name = "helpyou/category.html"

    # 카테고리
    def category_page(request, slug1, slug2):  # 과일 등 // 미분류 -> no_category로 가게 됨
        if slug1 == '과일':
            categorybig = CategoryBig.objects.get(slug=slug1)
            big_list = Product.objects.filter(categorybig=categorybig)
        elif slug1 == '쌀잡곡':
            categorybig = CategoryBig.objects.get(slug=slug1)
            big_list = Product.objects.filter(categorybig=categorybig)
        else:
            categorybig = CategoryBig.objects.get(slug=slug1)
            big_list = Product.objects.filter(categorybig=categorybig)

        if slug2 == '사과':
            categorysmall = CategorySmall.objects.get(slug=slug2)
            product_list = Product.objects.all()
        # product_list = Product.objects.filter(category=categorybig) #product_list = product.objects.all()이었다면 모든 리스트가 다 나옴

        return render(
            request,
            'helpyou/category.html',  # category.html?
            {  # context 넣는 위치! 알기 '변수명 : 들어갈 내용'
                # 필터링한 것만 뜨게 하기
                'big_list': big_list,
                'product_list': product_list,
                'categoriesbig': CategoryBig.objects.all(),
                'categoriessmall': CategorySmall.objects.all(),
                'categorybig': categorybig,
                'categorysmall': categorysmall,

            }
        )
    def get_context_data(self, **kwargs):
        context = super(Category, self).get_context_data()  # post_list를 가져옴 # 상위에서 가져오기때문
        context['categoriesbig'] = CategoryBig.objects.all()  # CategoryBig DB의 내용
        context['categoriessmall'] = CategorySmall.objects.all()  # CategoryBig DB의 내용

        return context  # => 리턴은 post_list.html로 들어가게된다.

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

        return context

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

        return context

# 마이페이지
class MyPage(DetailView):
    model = Product
    template_name='helpyou/mypage.html'
    product = CategorySmall.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MyPage, self).get_context_data()  # lecture_list를 가져옴 # 상위에서 가져오기 때문
        context['categoriesbig'] = CategoryBig.objects.all()  # CategoryBig DB의 내용
        context['categoriessmall'] = CategorySmall.objects.all()  # CategoryBig DB의 내용
        return context


