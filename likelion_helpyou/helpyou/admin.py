from django.contrib import admin
from .models import CategoryBig,CategorySmall, Product, Payment

#여기서 Post 다 볼 수 있음

# Register your models here.
#admin.site.register(SignUp)
#admin.site.register(CustomUser)
admin.site.register(Product)
#admin.site.register(Cart)
admin.site.register(Payment)

class CategoryBigAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # 자동으로 채워주는 필드

class CategorySmallAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # 자동으로 채워주는 필드

# class ProductSmallAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug_big': ('categorybig',), 'slug_small':('categorysmall')}  # 자동으로 채워주는 필드

# class ProductBigAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug_small': ('categorysmall',)}  # 자동으로 채워주는 필드

#admin 사이트에 category와 categoryAdmin 등록하기
admin.site.register(CategoryBig, CategoryBigAdmin)
admin.site.register(CategorySmall, CategorySmallAdmin)