from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    # path(anyname , include('urAppname.url'))
    # path('blog/', include('blog.url')),
    
    # whene write blog1 go to the first blog and blog2 to 2nd blog ..etc
    path('<int:blog_id>/', views.detail, name='detail'),
]