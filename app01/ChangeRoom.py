import ssl
import pymysql
from django.contrib.auth.models import *
# Create your views here.
#视图函数,返回index.html页面
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, permission_required
# 注册
# Create your views here.
from pandas.tests.io.excel.test_xlrd import xlrd
from app01 import models

#教室操作
@login_required(login_url='/login.html')
def Room(request):
    print("Room")
    # 查询教室信息
    gg_list = models.Classroom.objects.all()
    ll_list = models.ClassroomType.objects.all()
    pa_list = models.Campus.objects.all()
    return render(request, 'Room.html', {'gglist': gg_list,'lllist': ll_list,'palist':pa_list})

# 按类型查询
@login_required(login_url='/login.html')
def RoomSelect1(request):
    print('====RoomSelect1======')
    id3 = request.POST.get('cat_id')
    camp = request.POST.get('id_camp')
    request.session['cat_id'] = id3
    request.session['id_camp'] = camp
    print("camp,id3", camp, id3)
    if id3==None:
        response_dic = {'status': 102, 'msg': '类型不能为空'}
        return JsonResponse(response_dic)
    else:
        response_dic = {'status': 101, 'msg': None}
        return JsonResponse(response_dic)
#按类型查询
@login_required(login_url='/login.html')
def RoomSelect1Redict(request):
    id3 = int(request.session.get('cat_id', default=''))
    camp = request.session.get('id_camp', default='')
    print('======RoomSelect1Redict=====', id3)
    print(camp)
    if camp == '全部':
        gglist = models.Classroom.objects.filter(ctype=id3)
    else:
        camp=int(camp)
        gglist = models.Classroom.objects.filter(ctype=id3, campus_id=camp)
    return render(request, 'Room.html', {'gglist': gglist})



# 按范围查询
@login_required(login_url='/login.html')
def RoomSelect2(request):
    id21 = request.POST.get('id21')
    id22 = request.POST.get('id22')
    camp=request.POST.get('id_camp')
    print("===RoomSelect2===")
    print('id21,id22,camp',id21,id22,camp)
    request.session['id21'] = id21
    request.session['id22'] = id22
    request.session['id_camp'] = camp
    id21 = request.session.get('id21', default='')
    id22 = request.session.get('id22', default='')
    camp = request.session.get('id_camp', default='')
    name = request.session.get('name')
    if name == None:
        return redirect('login.html')
    elif id21=='' or id22=='':
        response_dic = {'status': 102, 'msg': None}
        return JsonResponse(response_dic)
    else:
        response_dic = {'status': 101, 'msg': None}
        return JsonResponse(response_dic)

    # # return render(request, 'Room.html')
#按范围查询
@login_required(login_url='/login.html')
def RoomSelect2Redict(request):
    print("==RoomSelect2Redict==")
    id21 = request.session.get('id21', default='')
    id22 = request.session.get('id22', default='')
    camp = request.session.get('id_camp', default='')
    print('id21,id22,camp',id21,id22,camp)
    id1 = float(id21)
    id2 = float(id22)
    print("type", type(id2))
    if camp == '全部':
            gg_list = models.Classroom.objects.filter(capacity__gt=id21, capacity__lt=id22)
    else:
        camp=int(camp)
        gg_list = models.Classroom.objects.filter(capacity__gt=id21, capacity__lt=id22, campus_id=camp)
    return render(request, 'Room.html',{'gglist':gg_list})



# 教室添加
@login_required(login_url='/login.html')
def AddRoom(request):
    print("=====添加教室AddRoom======")
    if request.method == 'GET':
        gg_list = models.ClassroomType.objects.all()
        return render(request, 'AddRoom.html', {'gglist': gg_list})
    else:
        #需要添加一个判断，如果教室号已经存在，则提示教室号不对。（需要重数据库中对比改号码存不存在）
        id_room = request.POST.get('id_room')
        id_name = request.POST.get('id_name')
        id_enroll = request.POST.get('id_enroll')
        id_type = int(request.POST.get('id_type'))
        id_camp = int(request.POST.get('id_camp'))
        id_total = request.POST.get('id_total')
        id_use = request.POST.get('id_use')
        print("id_room，id_name，id_use，id_type,id_camp",id_room,id_name,id_use,id_type,id_camp)
        if id_room and id_name and id_enroll and id_type and id_camp and id_total and id_use:
            cid = models.Classroom.objects.filter(cid=id_room)
            if cid:
                info = '该教室编号已存在'
                response_dic = {'status': 112, 'msg': info}
            else:
                if id_enroll.isdigit() and id_total.isdigit():
                    if id_use == '是':
                        id_use = 1
                    else:
                        id_use = 0
                    if int(id_enroll) < int(id_total):
                       response_dic = {'status': 111, 'msg': '考试人数大于教室容量！'}
                    else:
                     models.Classroom.objects.create(cid=id_room, cname=id_name, capacity=id_enroll, ctype_id=id_type, cnum=id_total,
                                                    cuse=id_use,campus_id=id_camp)
                     response_dic = {'status': 100, 'msg': '添加成功'}
                else:
                    response_dic = {'status': 111, 'msg': '填写不完整！'}
        else:
            response_dic = {'status': 111, 'msg': '请输入全部内容！'}
    return JsonResponse(response_dic)

# 修改教室
@login_required(login_url='/login.html')
def AlterRoom1(request):
    print("AlterRoom1")
    if request.method == 'GET':
        gg_list = models.ClassroomType.objects.all()
        return render(request, 'AddRoom.html', {'gglist': gg_list})
    else:

        # 需要添加一个判断，如果教室号已经存在，则提示教室号不对。（需要重数据库中对比改号码存不存在）
        id_room = request.POST.get('id_room')
        id_name = request.POST.get('id_name')
        id_enroll = request.POST.get('id_enroll')
        id_type = int(request.POST.get('id_type'))
        id_total = request.POST.get('id_total')
        id_use = request.POST.get('id_use')
        print('获取页面的信息 id_room id_name  id_enroll id_total id_use id_type', id_room,id_name,id_enroll,id_total, id_use,id_type)
        if id_room and id_name and id_enroll and id_type and id_total and id_use:
            if id_enroll.isdigit() and id_total.isdigit():
                if int(id_enroll) >= int(id_total):
                    if id_use == '是':
                        id_use = 1
                    else:
                        id_use = 0
                    models.Classroom.objects.filter(cid=id_room).update(cname=id_name, capacity=id_enroll,
                                                                    ctype_id=id_type, cnum=id_total,
                                                                    cuse=id_use)
                    response_dic = {'status': 100, 'msg': None}

                else:
                    response_dic = {'status': 111, 'msg': '考试人数大于教室容量！'}
            else:
                response_dic = {'status': 111, 'msg': '教室容量和考试人数应为数字！'}
        else:
            response_dic = {'status': 111, 'msg': '请填写全部内容！'}
    return JsonResponse(response_dic)


# 教室删除
@login_required(login_url='/login.html')
def DelRoom(request):
    print('DelRoom')
    if request.method == 'GET':
        return render(request, 'Room.html')
    else:
        id_room = request.POST.get('id_room')
        print('id_room',id_room)
        if id_room:
            if id_room.isdigit():
                result = models.Classroom.objects.filter(cid=id_room)
                if result.exists():
                    response_dic = {'status': 100, 'msg': None}
                    models.Classroom.objects.filter(cid=id_room).delete()
                else:
                    response_dic = {'status': 111, 'msg': '不存在！'}
            else:
                response_dic = {'status': 111, 'msg': '输入类型不正确！'}
        else:
            response_dic = {'status': 111, 'msg': '输入不能为空！'}
        return JsonResponse(response_dic)

# 上传文件
@login_required(login_url='/login.html')
def UploadRoom(request):
    print('UploadRoom')
    if request.method == 'GET':
        return render(request, 'Room.html')
    else:
        print('_____________')
        File = request.FILES.get("myfile", None)
        if File:
            till = File.name.split('.')[-1]
            print(till)
            # 允许写入文件
            ssl._create_default_https_context = ssl._create_unverified_context
            # 打开特定的文件进行二进制的写操作;
            print(File.name)
            with open("%s" % File.name, 'wb+') as f:
                # 分块写入文件;
                for chunk in File.chunks():
                    f.write(chunk)
            # 打开数据所在的工作簿，以及选择存有数据的工作表
            file = xlrd.open_workbook(File.name)
            sheet = file.sheet_by_index(0)
            print(sheet.nrows)
            print(sheet.ncols)
            # sheet = book.sheet_by_name("sheet1")
            # 建立一个MySQL连接
            conn = pymysql.connect(
                host='localhost',
                user='root',
                passwd='123456',
                db='dg13',
                port=3306,
                charset='utf8'
            )
            cursor = conn.cursor()
            # 创建插入SQL语句
            query = 'insert into app01_classroom (cid,cname,capacity,ctype_id,cnum,cuse,campus_id) values (%s, %s, %s, %s, %s, %s, %s)'
            # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
            for r in range(1, sheet.nrows):
                cid = sheet.cell(r, 0).value
                # print(coID)
                name = sheet.cell(r, 1).value
                capacity = sheet.cell(r, 2).value
                ctype_id = sheet.cell(r, 3).value
                cnum = sheet.cell(r, 4).value
                cuse = sheet.cell(r, 5).value
                campus_id = sheet.cell(r, 6).value
                print(cid, name, capacity, ctype_id, cnum, cuse, campus_id)
                values = (cid, name, capacity, ctype_id, cnum, cuse, campus_id)
                # 执行sql语句
                cursor.execute(query, values)
                conn.commit()
            # 关闭游标连接
            cursor.close()

            # 关闭数据库连接
            conn.close()
            columns = str(sheet.ncols)
            rows = str(sheet.nrows)
            print("导入 " + columns + " 列 " + rows + " 行数据到MySQL数据库!")
            response_dic = {'status': 100, 'msg': '设置成功！'}
        else:
            response_dic = {'status': 101, 'msg': '设置失败！'}
        return JsonResponse(response_dic)


