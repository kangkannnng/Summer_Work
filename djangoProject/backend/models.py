from django.db import models


# Create your models here.

# 这里创建了一个类，描述文件的各种需要信息
class File(models.Model):
    # 整型变量id
    id = models.IntegerField(primary_key=True, verbose_name="请输入文件ID")
    # 字符串变量name
    name = models.CharField(max_length=200, verbose_name="请输入文件名")
    # url类型变量field
    field = models.URLField(max_length=255, null=True, verbose_name="文件路径")
    # 字符串变量code
    code = models.CharField(max_length=2000, null=True, verbose_name="请输入代码")
    # 开始行数start_line
    start_line = models.IntegerField(default=0, verbose_name="开始行数")
    # 结束行数end_line
    end_line = models.IntegerField(default=0, verbose_name="结束行数")
