from django.urls import path
from backend import views

urlpatterns = [
    path("hello/", views.hello),		    # test路由,返回欢迎标语
    path("load/", views.load),		        # load路由,返回全部文件
    path("test/", views.testsimilar),		# test路由,返回排序结果
]
