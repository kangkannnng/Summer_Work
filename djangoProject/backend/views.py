import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import File
import numpy as np


# Create your views here.


def hello(request):
    return JsonResponse({"status": 0, "message": "欢迎使用本项目！"})  # 返回json数据类型


def load(request):
    if request.method == "GET":
        db = File.objects.all()  # 从数据库中获取所有数据对象
        json = serializers.serialize("json", db)  # 将模型类数据序列化为json数据
        return JsonResponse({"status": 0, "data": json})
    else:
        return JsonResponse({"status": 1, "message": "you need Get method"})


def testsimilar(request):
    temp_id = json.loads(request.body)["id"]
    print(temp_id)
    if request.method == "POST":
        if temp_id == 0:
            # 说明要比较A文件，返回B的信息
            message = {
                "id": 1,
                "name": "b.txt",
                "code": "This is b test file",
            }
            return JsonResponse({"data": message})
        if temp_id == 1:
            # 说明要比较B文件，返回C的信息
            message = {
                "id": 2,
                "name": "c.txt",
                "code": "This is c test file",
            }
            return JsonResponse({"data": message})
        if temp_id == 2:
            # 说明要比较C文件，返回A的信息
            message = {
                "id": 0,
                "name": "a.txt",
                "code": "This is a test file",
            }
            return JsonResponse({"data": message})
    else:
        return JsonResponse("error")


def index(request):
    return render(request, 'index.html')

# 获取的是前端的ID和label,返回的是一个列表
# def mostsimilar(request):
#     if request.method == "POST":
#         files = open('programme_file/JHotDraw.files', 'r')
#         clones = open('programme_file/JHotDraw.clones', 'r')
#         name = files.readlines()
#         an1 = 0
#         an2 = 0    # 分别为两个文件开头注释的行数
#         for item in name:
#             if item[0] != '#':
#                 break
#             an1 += 1
#         line1 = len(name) - an1  # 为.files文件除注释外的行数
#         namelist = []
#         for i in range(0, line1):
#             name[an1+i] = name[an1+i].split()
#             namelist.append(name[an1+i][1])   # 列表中是每个文件序号对应的文件名
#         similarlines = clones.readlines()
#         for item in similarlines:
#             if item[0] != '#':
#                 break
#             an2 += 1
#         line2 = len(similarlines) - an2  # .clones文件除注释外的行数
#         array1 = np.zeros((line1, line1))  # 二维列表记录x文件与y文件相似的行数中x文件的行数之和
#         array2 = np.zeros((line1, line1))  # 二维列表记录x文件与y文件相似的行数中y文件的行数之和
#         for i in range(0, line2):
#             similarlines[an2+i] = similarlines[an2+i].split(',')
#             array1[int(similarlines[an2+i][0])][int(similarlines[an2+i][3])] += (int(similarlines[an2+i][2]) - int(similarlines[an2+i][1]))
#             array2[int(similarlines[an2+i][0])][int(similarlines[an2+i][3])] += (int(similarlines[an2+i][5]) - int(similarlines[an2+i][4]))
#             array1[int(similarlines[an2+i][3])][int(similarlines[an2+i][0])] += (int(similarlines[an2+i][5]) - int(similarlines[an2+i][4]))
#             array2[int(similarlines[an2+i][3])][int(similarlines[an2+i][0])] += (int(similarlines[an2+i][2]) - int(similarlines[an2+i][1]))
#         # 对两个二维数组进行赋值
#         name = request.POST.get('id')
#         num = request.POST.get('label')
#         sortedlist = []
#         for i in range(0, line1):
#             if array2[name][i] != 0:
#                 sortedlist.append(array1[name][i] + 1 - 1/array2[name][i])
#             else:
#                 sortedlist.append(array1[name][i])
#         # 该列表中记录的是选取的文件与所有文件的相似度的数值表征
#         sortedlist[name] = 0  # 去除该文件本身
#         sortedlist = np.array(sortedlist)
#         arglist = np.argsort(-sortedlist)  # 该列表为sortedlist进行从大到小排序后原数字下标的顺序
#         res = []
#         for i in range(0, num):
#             res.append(arglist[i])
#         finalres = []


#         class mytype:
#             def __init__(self, res_id, res_file_name, res_url):
#                 self.id = res_id
#                 self.file_name = res_file_name
#                 self.url = res_url     # 定义一个新的类型


#         for i in res:
#             res_id = i
#             res_file_name = namelist[i].split('/')[-1]
#             res_url = '.' + namelist[i][36:]
#             temp = mytype(res_id, res_file_name, res_url)
#             finalres.append(temp)  # finalres列表里装的就是自定义对象
#         return JsonResponse({"status": 0, "data": finalres})
