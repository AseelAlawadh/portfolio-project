from django.contrib import admin

# Register your models here.
#نسوي امبورت للمودل . 
from .models import Job
#ندخل  المودل في الداتا بيز للادمن  بنروح للصفحة الادن ونسوي ريفريش وبنلاحظ وجودها 
admin.site.register(Job)