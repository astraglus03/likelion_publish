from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission, Group
import os
#from django.contrib.auth.models import Permission as DjangoPermission



# # 회원가입
# class SignUp (models.Model):
#     id = models.CharField(max_length=20, null=False)  # 아이디
#     pw = models.CharField(max_length=20, null=False)  # 비밀번호
#     pw_check = models.CharField(max_length=20, null=False)  # 비밀번호 확인
#     name = models.CharField(max_length=30, null=False)  # 이름
#     address = models.CharField(max_length=100, null=False)  # 주소
#     detail_address = models.CharField(max_length=30, null=False)  # 상세주소
#     phone_numb = models.IntegerField(max_length=11, null=False)  # 전화번호
#     email = models.CharField(max_length=20, null=False)  # 이메일 주소
#     year = models.IntegerField(max_length=4, null=False) # 생년월일-년도
#     month = models.IntegerField(max_length=2, null=False) # 생년월일-월
#     day = models.IntegerField(max_length=2, null=False) # 생년월일-일


# 카테고리 (대주제) ex. 예) 과일
class CategoryBig(models.Model): # unique : 겹치면 안 됨
    name = models.CharField(max_length=50, unique=True, null=False, default='')
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    # allow_unicode = True -> 한글도 가능하게

    def __str__(self):
       return self.name

    def get_absolute_url(self):
        return f'/category/{self.slug}/'

    # def get_absolute_url(self):
    #     return f'/helpyou/category/{self.big}/{self.mid}/{self.small}/{self.slug}/'

    class Meta:
        verbose_name_plural = 'CategoriesBig'  # Categorys로 복수형이 잘못 표시됨 # 테이블에 이름 강제 지정 가능함.

# 카테고리 (소주제)
class CategorySmall(models.Model): # 예) 사과
    # 일대다 관계
    categorybig = models.ForeignKey(CategoryBig, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=50, unique=True, null=False, default='')
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    # allow_unicode = True -> 한글도 가능하게

    def __str__(self):
       return self.name

    def get_absolute_url(self):
        return f'/category/{self.categorybig}/{self.slug}/'

    class Meta:
        verbose_name_plural = 'CategoriesSmall'  # Categorys로 복수형이 잘못 표시됨 # 테이블에 이름 강제 지정 가능함.

# 상품 등록
class Product(models.Model):

    # 일대다 관계 (1ToMany)
    categorybig = models.ForeignKey(CategoryBig, on_delete=models.CASCADE, default='')
    categorysmall = models.ForeignKey(CategorySmall, on_delete=models.CASCADE, default='')
    # blank=true, 선택 안 해도 됨
    # null=true, 반드시 로그인해서 들어가야 하기 때문에, 선택이 돼야 함

    name = models.CharField(max_length=30)  # 상품명
    country = models.CharField(max_length=30) # 원산지
    price = models.IntegerField() # 가격
    unit = models.CharField(max_length=10) # 단위 (개 or BAG) 예) 몇 개당 얼마
    card = models.CharField(max_length=30, null=False, default='3000') # 배송비 3000원
    delivery = models.CharField(max_length=30, null=False, default='3000') # 배송비 3000원


    # 상품 사진 4개 등록
    main_image = models.ImageField(upload_to='helpyou/files/%Y/%m/%d', blank=True) # 메인 이미지
    sub_image1 = models.ImageField(upload_to='helpyou/files/%Y/%m/%d', blank=True) # 서브 이미지 1
    sub_image2 = models.ImageField(upload_to='helpyou/files/%Y/%m/%d', blank=True)  # 서브 이미지 2
    sub_image3 = models.ImageField(upload_to='helpyou/files/%Y/%m/%d', blank=True)  # 서브 이미지 3

    #created_at = models.DateTimeField(auto_now_add=True)  # 업로드 날짜, 시간
    #updated_at = models.DateTimeField(auto_now=True)      # 업데이트/수정 날짜, 시간

    #author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # 외래키 이용해서 user 테이블에 연결

    def __str__(self):  # 포스트의 번호와 제목 보여주기 + use의 이름도
        return f'[{self.pk}][{self.categorybig} - {self.categorysmall}] {self.name}'

    def get_absolute_url(self):
        return f'/category/{self.categorybig.slug}/{self.categorysmall.slug}/{self.name}/' #return f'/helpyou/{self.pk}/'

    def cart_url(self):
        return f'/cart/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)  # 업로드된 파일의 전체 경로 가져오기

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]  # 가져온 전체 경로에서 이름을 가져오고, '.'을 기준으로 쪼갬
        # 확장자명 가져오기
        # test.py -> test 와 py로 쪼갬 -> -1: 마지막 인덱스 py를 return
        # 여러 개면 배열로 저장됨. 몇 개든 -1이면 확장자명 가져옴

# # 장바구니
# class Cart(models.Model):
#     delivery = models.CharField(max_length=30, null=False, default='3000') # 배송비 3000원
#
#     def __str__(self):
#        return self.delivery
#
#     def get_absolute_url(self):
#         return f'/cart/'

# 결제
class Payment(models.Model):
    name = models.CharField(max_length=30, null=False)  # 결제할 신용카드 등록
    month = models.CharField(max_length=20, null=False) # 할부개월

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/payment/'