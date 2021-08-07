import ssl
import pymysql
from django.contrib.auth.models import *
from django.db.models import Max
# Create your views here.
#视图函数,返回index.html页面
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from pandas.tests.io.excel.test_xlrd import xlrd
from django.contrib.auth.decorators import login_required, permission_required
# 注册
# Create your views here.
from app01 import models


# 上传文件
@login_required(login_url='/login.html')
def UploadCourse(request):
    print('UploadCourse')
    if request.method == 'GET':
        return render(request, 'ClassView1.html')
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
            query = 'insert into app01_cou (coID,NAME,CREDIT,TEACHNO,TEACHNAME,TEACHID,TIMETEXT,TIMESET,F1,NOTUSEROOM,TOTALS,ENROLLS,flag,MARK,DELROLE,COLLEGEID,SPECIALITYID,TIMESET1,ROOM1,F2,ROOM_id,campus_id) values (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s,%s)'
            # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
            for r in range(1, sheet.nrows):
                coID=sheet.cell(r, 0).value
                NAME=sheet.cell(r, 1).value
                CREDIT=sheet.cell(r, 2).value
                TEACHNO=sheet.cell(r, 3).value
                aa=models.Cou.objects.filter(coID=coID,TEACHNO=TEACHNO)
                if aa:
                    response_dic = {'status': 101, 'msg': coID+' '+TEACHNO}
                    return JsonResponse(response_dic)
                else:
                    TEACHNAME=sheet.cell(r, 4).value
                    TEACHID=sheet.cell(r, 5).value
                    TIMETEXT=sheet.cell(r, 6).value
                    TIMESET=sheet.cell(r, 7).value
                    F1=sheet.cell(r, 8).value
                    NOTUSEROOM=sheet.cell(r, 9).value
                    TOTALS=sheet.cell(r, 10).value
                    ENROLLS=sheet.cell(r, 11).value
                    flag=sheet.cell(r, 12).value
                    MARK=sheet.cell(r, 13).value
                    DELROLE=sheet.cell(r, 14).value
                    COLLEGEID=sheet.cell(r, 15).value
                    SPECIALITYID=sheet.cell(r, 16).value
                    TIMESET1=sheet.cell(r, 17).value
                    ROOM1=sheet.cell(r, 18).value
                    F2=sheet.cell(r, 19).value
                    ROOM_id=sheet.cell(r, 20).value
                    campus_id=sheet.cell(r, 21).value
                    print(coID,NAME,CREDIT,TEACHNO,TEACHNAME,TEACHID,TIMETEXT,TIMESET,F1,NOTUSEROOM,TOTALS,ENROLLS,flag,MARK,DELROLE,COLLEGEID,SPECIALITYID,TIMESET1,ROOM1,F2,ROOM_id,campus_id)
                    values = (coID,NAME,CREDIT,TEACHNO,TEACHNAME,TEACHID,TIMETEXT,TIMESET,F1,NOTUSEROOM,TOTALS,ENROLLS,flag,MARK,DELROLE,COLLEGEID,SPECIALITYID,TIMESET1,ROOM1,F2,ROOM_id,campus_id)
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

# 课程操作
@login_required(login_url='/login.html')
def ClassView1(request):
    print("=======ClassView1======")
    # camp=request.session.get('camp')
    gg_list = models.Cou.objects.all()
    ll_list = models.ClassroomType.objects.all()
    cc_list = models.Campus.objects.all()

    pa_list1 = models.Parameter.objects.all().aggregate(Max('id'))
    # 取最新输入的参数
    for item in pa_list1:
        print('pa_list1',pa_list1[item])
        pa_list = models.Parameter.objects.filter(id=pa_list1[item])
    return render(request, 'ClassView1.html', {'gglist': gg_list, 'palist': pa_list,'lllist': ll_list,'cclist': cc_list,})

# 课程删除
@login_required(login_url='/login.html')
def DelClass(request):
    print('DelClass')
    if request.method == 'GET':
        return render(request, 'Room.html')
    else:
        coID = request.POST.get('coID')
        print('coID',coID)
        models.Cou.objects.filter(coID=coID).delete()
        response_dic = {'status': 100, 'msg': '删除成功'}
    return JsonResponse(response_dic)

#修改课程信息（无法定位修改课程的id）
@login_required(login_url='/login.html')
# @permission_required('app01.change_app01_class_tem')
def AlterClass(request):
    print("AlterClass")
    if request.method == 'GET':

        return render(request, 'ClassView1.html')
    else:
        # 需要添加一个判断，如果教室号已经存在，则提示教室号不对。（需要重数据库中对比改号码存不存在）
        id_ind=request.POST.get('id_ind')
        id_name = request.POST.get('id_name')
        id_sco = request.POST.get('id_sco')
        id_enr = request.POST.get('id_enr')
        id_num = request.POST.get('id_num')
        id_use = request.POST.get('id_use')
        id_tea = request.POST.get('id_tea')
        id_teaname = request.POST.get('id_teaname')
        id_type = int(request.POST.get('id_type'))
        print('获取页面的信息 id_ind id_name  id_sco id_enr id_num  id_use', id_ind,id_name,id_sco,id_enr,id_num,id_use)

        if id_type and id_name and id_sco and id_enr and id_num and id_tea and id_teaname :
            if id_enr.isdigit() and id_num.isdigit():
                    if id_use == '是':
                        id_use = 1
                    else:
                        id_use = 0
                    models.Classroom.objects.filter(coID=id_ind).update(NAME=id_name, CREDIT=id_sco,
                                                                    TEACHNO=id_tea, TEACHNAME=id_teaname,ENROLLS=id_enr,
                                                                    cuse=id_use,TOTALS=id_num)
                    response_dic = {'status': 100, 'msg': '更新成功'}


            else:
                response_dic = {'status': 111, 'msg': '容量和人数应为数字！'}
        else:
            response_dic = {'status': 111, 'msg': '请填写全部内容！'}
        return JsonResponse(response_dic)
#课程添加
@login_required(login_url='/login.html')
def AddClass(request):
    print("==========添加课程AddClass===========")
    if request.method == 'GET':

        return render(request, 'ClassView1.html')
    else:
        id_addind = request.POST.get('id_addind')
        id_addname = request.POST.get('id_addname')
        id_addsco = request.POST.get('id_addsco')
        id_addenr = request.POST.get('id_addenr')
        id_addnum = request.POST.get('id_addnum')
        id_adduse = request.POST.get('id_adduse')
        id_addtype = int(request.POST.get('id_addtype'))
        id_addcamp1 = int(request.POST.get('id_addcamp1'))
        print('id_addind id_addname id_addsco id_addenr id_addnum id_adduse id_addtype,id_addcamp1',id_addind,id_addname,id_addsco,id_addenr,id_addnum,id_adduse,id_addtype,id_addcamp1)


        if id_addind and id_addname and id_addsco and id_addenr and id_addnum and id_adduse and id_addtype:
            if id_addenr.isdigit() and id_addnum.isdigit():
                # print(id_type)
                if id_adduse == '是':
                    id_adduse = 1
                else:
                    id_adduse = 0

                if int(id_addenr) < int(id_addnum):
                   response_dic = {'status': 111, 'msg': '选课人数超出课程容量！'}
                else:
                    # models.Cou.objects.create(cid=id_room, cname=id_name, capacity=id_enroll, ctype_id=id_type, cnum=id_total,
                    #                             cuse=id_use,campus_id=id_camp)
                 response_dic = {'status': 100, 'msg': '添加语句待完善'}
            else:
                response_dic = {'status': 111, 'msg': '填写不完整！'}
        else:
            response_dic = {'status': 111, 'msg': '请输入全部内容！'}
        return JsonResponse(response_dic)

@login_required(login_url='/login.html')
def AlterClass3(request):
    # remain = request.POST.get('remain')
    # request.session['remain'] = remain
    # File = request.FILES.get("myfile", None)
    # File1 = request.FILES.get("myfile1", None)
    # if school and colle and year and seame and remain:
    #     if remain.isdigit():
    #         if File:
    #             print(school)
    #             till = File.name.split('.')[-1]
    #             print(till)
    #             # 允许写入文件
    #             ssl._create_default_https_context = ssl._create_unverified_context
    #             # 打开特定的文件进行二进制的写操作;
    #             with open("%s" % File.name, 'wb+') as f:
    #                 # 分块写入文件;
    #                 for chunk in File.chunks():
    #                     f.write(chunk)
    #             # 打开数据所在的工作簿，以及选择存有数据的工作表
    #             file = xlrd.open_workbook(File.name)
    #             sheet = file.sheet_by_index(0)
    #             print(sheet.nrows)
    #             print(sheet.ncols)
    #             # sheet = book.sheet_by_name("sheet1")
    #             # 建立一个MySQL连接
    #             conn = pymysql.connect(
    #                 host='localhost',
    #                 user='root',
    #                 passwd='123456',
    #                 db='course',
    #                 port=3306,
    #                 charset='utf8'
    #             )
    #             cursor = conn.cursor()
    #             # SQL语句更新数据
    #             sql = "TRUNCATE TABLE app01_cou"
    #             # 执行SQL语句
    #             cursor.execute(sql)
    #             # 提交到数据库执行
    #             conn.commit()
    #             print("删除数据成功")
    #             sql = "TRUNCATE TABLE app01_parameter"
    #             # 执行SQL语句
    #             cursor.execute(sql)
    #             # 提交到数据库执行
    #             conn.commit()
    #             print("删除数据成功")
    #             models.Parameter.objects.create(School=school, Campus=colle, SYear=year, Semester=seame, Remainder=remain)
    #             # 创建插入SQL语句
    #             query = 'insert into app01_cou (coID,NAME,CREDIT,TEACHNO,TEACHNAME,TEACHID,TIMETEXT,TIMESET,ROOM,F1,ROOM1,NOTUSEROOM,TOTALS,ENROLLS,MARK,F2,DELROLE,CAMPUSID,COLLEGEID,SPECIALITYID,campus) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
    #             # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
    #             for r in range(1, sheet.nrows):
    #                 coID = sheet.cell(r, 0).value
    #                 # print(coID)
    #                 NAME = sheet.cell(r, 1).value
    #                 # print(NAME)
    #                 CREDIT = sheet.cell(r, 2).value
    #                 TEACHNO = sheet.cell(r, 3).value
    #                 TEACHNAME = sheet.cell(r, 4).value
    #                 TEACHID = sheet.cell(r, 5).value
    #                 TIMETEXT = sheet.cell(r, 6).value
    #                 TIMESET = sheet.cell(r, 7).value
    #                 ROOM = sheet.cell(r, 8).value
    #                 F1 = sheet.cell(r, 9).value
    #                 ROOM1 = sheet.cell(r, 10).value
    #                 NOTUSEROOM = sheet.cell(r, 11).value
    #                 TOTALS = sheet.cell(r, 12).value
    #                 ENROLLS = sheet.cell(r, 13).value
    #                 MARK = sheet.cell(r, 14).value
    #                 F2 = sheet.cell(r, 15).value
    #                 DELROLE = sheet.cell(r, 16).value
    #                 CAMPUSID = sheet.cell(r, 17).value
    #                 COLLEGEID = sheet.cell(r, 18).value
    #                 SPECIALITYID = sheet.cell(r, 19).value
    #                 campus=sheet.cell(r, 20).value
    #                 values = (
    #                     coID, NAME, CREDIT, TEACHNO, TEACHNAME, TEACHID, TIMETEXT, TIMESET, ROOM, F1, ROOM1, NOTUSEROOM, TOTALS,
    #                     ENROLLS, MARK, F2, DELROLE, CAMPUSID, COLLEGEID, SPECIALITYID,campus)
    #                 # 执行sql语句
    #                 cursor.execute(query, values)
    #                 conn.commit()
    #             # 关闭游标连接
    #             cursor.close()
    #
    #             # 关闭数据库连接
    #             conn.close()
    #             columns = str(sheet.ncols)
    #             rows = str(sheet.nrows)
    #             print("导入 " + columns + " 列 " + rows + " 行数据到MySQL数据库!")
    #             # response_dic = {'status': 100, 'msg': '设置成功！'}
    #         if File1:
    #             # print(school)
    #             till = File1.name.split('.')[-1]
    #             # print(till)
    #             # 允许写入文件
    #             ssl._create_default_https_context = ssl._create_unverified_context
    #             # 打开特定的文件进行二进制的写操作;
    #             with open("%s" % File1.name, 'wb+') as f:
    #                 # 分块写入文件;
    #                 for chunk in File1.chunks():
    #                     f.write(chunk)
    #             # 打开数据所在的工作簿，以及选择存有数据的工作表
    #             file1 = xlrd.open_workbook(File1.name)
    #             sheet = file1.sheet_by_index(0)
    #             # print(sheet.nrows)
    #             # print(sheet.ncols)
    #             # sheet = book.sheet_by_name("sheet1")
    #             # 建立一个MySQL连接
    #             conn = pymysql.connect(
    #                 host='localhost',
    #                 user='root',
    #                 passwd='123456',
    #                 db='classroom',
    #                 port=3306,
    #                 charset='utf8'
    #             )
    #             cursor = conn.cursor()
    #             # SQL语句更新数据
    #             sql = "TRUNCATE TABLE app01_classroom"
    #             # 执行SQL语句
    #             cursor.execute(sql)
    #             # 提交到数据库执行
    #             conn.commit()
    #             print("删除数据成功")
    #             # 创建插入SQL语句
    #             query = 'insert into app01_classroom (cid,cname,capacity,ctype,cnum,cuse,campus) values (%s, %s, %s, %s, %s, %s, %s)'
    #             # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
    #             for r in range(1, sheet.nrows):
    #                 cid = sheet.cell(r, 0).value
    #                 # print(coID)
    #                 cname = sheet.cell(r, 1).value
    #                 # print(NAME)
    #                 capacity = sheet.cell(r, 2).value
    #                 ctype = sheet.cell(r, 3).value
    #                 cnum = sheet.cell(r, 4).value
    #                 cuse = sheet.cell(r, 5).value
    #                 campus = sheet.cell(r, 6).value
    #                 values = (
    #                     cid,cname,capacity,ctype,cnum,cuse,campus)
    #                 # 执行sql语句
    #                 cursor.execute(query, values)
    #                 conn.commit()
    #             # 关闭游标连接
    #             cursor.close()
    #
    #             # 关闭数据库连接
    #             conn.close()
    #             columns = str(sheet.ncols)
    #             rows = str(sheet.nrows)
    #             print("导入 " + columns + " 列 " + rows + " 行数据到MySQL数据库!")
    #         response_dic = {'status': 100, 'msg': '设置成功！'}
    #     else:
    #         response_dic = {'status': 111, 'msg': '余量请填写数字！'}
    # else:
    #     response_dic = {'status': 111, 'msg': '请填写全部内容！'}
    # return JsonResponse(response_dic)
    #         else:
    #             return redirect('/login/')
    # return render(request, 'AlterParameter.html')
    # return render(request, 'AlterParameter.html')

    return render(request, 'ClassView1.html')

#选课结果显示
@login_required(login_url='/login.html')
def AutoArrange(request):
    print("AutoArrange")
    # camp = request.session.get('camp', default='')
    name = request.session.get('name', default='')
    # print(camp, name)
    if name == None:
        return redirect('login.html')
    else:
        # u = models.UserInfo.objects.filter(username=name).values('UserType')
        # for i in u:
        #     if i['UserType'] == 1:
        pa_list = models.Parameter.objects.filter(id=1)
        # if camp == '全部':
        #     gglist = models.Cou.objects.all()
        # else:
        #     if camp == '宝山':
        #         camp = 0
        #     elif camp == '嘉定':
        #         camp = 1
        #     else:
        #         camp = 2
        # gglist = models.Cou.objects.filter(campus_id=camp)
        gglist = models.Cou.objects.filter(flag=1)
        # for gg in gglist:
        #     print(gg['F1'])
        pa_list1 = models.Parameter.objects.all().aggregate(Max('id'))
        # 取最新输入的参数
        for item in pa_list1:
            print('pa_list1', pa_list1[item])
        pa_list = models.Parameter.objects.filter(id=pa_list1[item])
        return render(request, 'AutoArrange.html', context={'gglist': gglist, 'palist': pa_list})
    # else:
    #     redirect('/login/')
    # return render(request,'ArrangeRes.html')
    return render(request, 'AutoArrange.html')

#进入未选课界面
@login_required(login_url='/login.html')
def NotArrange(request):
    print("NotArrange")
    name = request.session.get('name', default='')
    camp = request.session.get('camp', default='')
    if name == None:
        return redirect('login.html')
    else:
        # u = models.UserInfo.objects.filter(username=name).values('UserType')
        # for i in u:
        #     if i['UserType'] == 1:

        #疑问处应该是从表cou中按照条件选出，但是不知道什么代表没有安排的课程
                # if camp == '全部':
                #     gg_list = models.Cou.objects.filter()
                #     # pa_list = models.Parameter.objects.filter(id=1)
                #     return render(request, 'NotArrange1.html', {'gglist': gg_list})
                # else:
                #     gg_list = models.Cou.objects.filter()
                #     # pa_list = models.Parameter.objects.filter(id=1)
                #     return render(request, 'NotArrange.html', {'gglist': gg_list})
       #      else:
       #          return redirect('/login/')
       #

            gglist = models.Cou.objects.filter(flag=0)
            # for gg in gglist:
            #     print(gg['F1'])
            pa_list1 = models.Parameter.objects.all().aggregate(Max('id'))
            # 取最新输入的参数
            for item in pa_list1:
                print('pa_list1', pa_list1[item])
            pa_list = models.Parameter.objects.filter(id=pa_list1[item])
            return render(request, 'NotArrange.html', context={'gglist': gglist, 'palist': pa_list})
        # else:
        #     redirect('/login/')
        # return render(request,'ArrangeRes.html')

# 课程处理
@login_required(login_url='/login.html')
def HandleClass(request):
    name1 = request.session.get('name')
    if name1 == None:
        return redirect('login.html')
    else:
        u = models.UserInfo.objects.filter(username=name1).values('UserType')
        for i in u:
            if i['UserType'] == 1 or i['UserType'] == 7:
                if request.method == 'GET':
                    return render(request, 'HandleClass.html')

                else:
                    request.session['handle'] = True
                    camp=request.POST.get('id_camp')

                    if camp == '宝山':
                        response_dic = {'status': 100, 'msg': '宝山处理完毕'}
                        ab = models.Cou.objects.filter(TIMETEXT__contains='上机',campus='宝山')
                        for a in ab:
                            print(a.coID)
                            f = list(a.TIMESET)
                            print(a.TIMETEXT.split(" "))
                            b = a.TIMETEXT.split(" ")[-2]
                            c = int(b.split("-")[0][-1])
                            week = b.split("-")[0][-2]
                            d = int(b.split("-")[1][0])
                            # print(b.split("-")[0][-1])
                            print(type(c))
                            sum = 13
                            if week == '一':
                                sum = sum * 0
                            elif week == '二':
                                sum = sum * 1
                            elif week == '三':
                                sum = sum * 2
                            elif week == '四':
                                sum = sum * 3
                            elif week == '五':
                                sum = sum * 4
                            elif week == '六':
                                sum = sum * 5
                            elif week == '日':
                                sum = sum * 6
                            for i in range(c, d + 1):
                                set = sum + i - 1
                                f[set] = '0'
                            re = ''.join(f)
                            models.Cou.objects.filter(coID=a.coID,campus='宝山').update(TIMESET1=re)
                        return JsonResponse(response_dic)
                    elif camp == '嘉定':
                        response_dic = {'status': 101, 'msg': '嘉定处理完毕'}
                        ab = models.Cou.objects.filter(TIMETEXT__contains='上机',campus='嘉定')
                        for a in ab:
                            print(a.coID)
                            f = list(a.TIMESET)
                            print(a.TIMETEXT.split(" "))
                            b = a.TIMETEXT.split(" ")[-2]
                            c = int(b.split("-")[0][-1])
                            week = b.split("-")[0][-2]
                            d = int(b.split("-")[1][0])
                            # print(b.split("-")[0][-1])
                            print(type(c))
                            sum = 13
                            if week == '一':
                                sum = sum * 0
                            elif week == '二':
                                sum = sum * 1
                            elif week == '三':
                                sum = sum * 2
                            elif week == '四':
                                sum = sum * 3
                            elif week == '五':
                                sum = sum * 4
                            elif week == '六':
                                sum = sum * 5
                            elif week == '日':
                                sum = sum * 6
                            for i in range(c, d + 1):
                                set = sum + i - 1
                                f[set] = '0'
                            re = ''.join(f)
                            models.Cou.objects.filter(coID=a.coID,campus='嘉定').update(TIMESET1=re)
                        return JsonResponse(response_dic)
                    elif camp == '延长':
                        response_dic = {'status': 102, 'msg': '延长处理完毕'}
                        ab = models.Cou.objects.filter(TIMETEXT__contains='上机',campus='延长')
                        for a in ab:
                            print(a.coID)
                            f = list(a.TIMESET)
                            print(a.TIMETEXT.split(" "))
                            b = a.TIMETEXT.split(" ")[-2]
                            c = int(b.split("-")[0][-1])
                            week = b.split("-")[0][-2]
                            d = int(b.split("-")[1][0])
                            # print(b.split("-")[0][-1])
                            print(type(c))
                            sum = 13
                            if week == '一':
                                sum = sum * 0
                            elif week == '二':
                                sum = sum * 1
                            elif week == '三':
                                sum = sum * 2
                            elif week == '四':
                                sum = sum * 3
                            elif week == '五':
                                sum = sum * 4
                            elif week == '六':
                                sum = sum * 5
                            elif week == '日':
                                sum = sum * 6
                            for i in range(c, d + 1):
                                set = sum + i - 1
                                f[set] = '0'
                            re = ''.join(f)
                            models.Cou.objects.filter(coID=a.coID,campus='延长').update(TIMESET1=re)
                        return JsonResponse(response_dic)
                    elif camp == '全部':
                        response_dic = {'status': 103, 'msg': '全部处理完毕'}
                        ab = models.Cou.objects.filter(TIMETEXT__contains='上机')
                        for a in ab:
                            print(a.coID)
                            f = list(a.TIMESET)
                            print(a.TIMETEXT.split(" "))
                            b = a.TIMETEXT.split(" ")[-2]
                            c = int(b.split("-")[0][-1])
                            week = b.split("-")[0][-2]
                            d = int(b.split("-")[1][0])
                            # print(b.split("-")[0][-1])
                            print(type(c))
                            sum = 13
                            if week == '一':
                                sum = sum * 0
                            elif week == '二':
                                sum = sum * 1
                            elif week == '三':
                                sum = sum * 2
                            elif week == '四':
                                sum = sum * 3
                            elif week == '五':
                                sum = sum * 4
                            elif week == '六':
                                sum = sum * 5
                            elif week == '日':
                                sum = sum * 6
                            for i in range(c, d + 1):
                                set = sum + i - 1
                                f[set] = '0'
                            re = ''.join(f)
                            models.Cou.objects.filter(coID=a.coID).update(TIMESET1=re)
                        return JsonResponse(response_dic)
            else:
                return redirect('login.html')