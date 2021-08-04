import pymysql
from django.contrib.auth.models import *
from django.db.models import Max
# Create your views here.
#视图函数,返回index.html页面
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, permission_required
# 注册
# Create your views here.
from app01 import models



#进入未选课界面
@login_required(login_url='/login.html')
def NotArrange(request):
    print("NotArrange")
    gglist = models.Cou.objects.filter(flag=0)
    pa_list1 = models.Parameter.objects.all().aggregate(Max('id'))
    # 取最新输入的参数
    for item in pa_list1:
        print('pa_list1', pa_list1[item])
    pa_list = models.Parameter.objects.filter(id=pa_list1[item])
    return render(request, 'NotArrange.html', context={'gglist': gglist, 'palist': pa_list})




# 某个校区的安排结果
@login_required(login_url='/login.html')
def ArrangeRes(request):
    print("=======ArrangeRes==========")
    if request.method == 'GET':
        pa_list = models.Parameter.objects.filter(id=1)
        # if camp=='全部':
        gglist = models.Cou.objects.all()
        # else:
        #     gglist=models.Cou.objects.filter(campus_id=camp)

        return render(request,'ArrangeRes.html',context={'gglist':gglist,'palist':pa_list})
    # else:




# 临时调配
@login_required(login_url='/login.html')
# @permission_required('app01.chang_app01_temp_tem')
def TempArrange(request):
    print("========TempArrange========")
    camp1 = request.POST.get('camp1')
    techno = request.POST.get('techno')
    courseno = request.POST.get('courseno')
    tempclasstype = request.POST.get('tempclasstype')
    # name就是教室编号
    name = request.POST.get('name')
    # 教室类型
    type = request.POST.get('type')
    week = request.POST.get('week')
    classnum = request.POST.get('classnum')
    num = request.POST.get('num')
    back = request.POST.get('back')

    print('TempArrange临时调配', camp1, techno, courseno, tempclasstype, name, type, week, classnum, num,
          back)
    name1 = request.session.get('name')

    if request.method == 'GET':
        str1 = ''
        tt_list = models.ClassroomType.objects.all()
        return render(request, 'TempArrange.html', {'ttlist': tt_list})
    if request.method == 'POST':
        camp=request.POST.get('camp')
        techno=request.POST.get('techno')
        courseno=request.POST.get('courseno')
        tempclasstype=request.POST.get('tempclasstype')
        #name就是教室编号
        name=request.POST.get('name')
        #教室类型
        type=request.POST.get('type')
        week=request.POST.get('week')
        classnum = request.POST.get('classnum')
        num = request.POST.get('num')
        back = request.POST.get('back')
        print('TempArrange临时调配', camp, techno, courseno, tempclasstype, name, type, week, classnum, num,
                  back)

        if camp and techno and courseno and tempclasstype and name and type and week and classnum and num:
            if camp == '宝山':
                camp = 0
            elif camp == '嘉定':
                camp = 1
            else:
                camp = 2

            if week=='星期一':str1='Mon'
            elif week=='星期二':str1='Tue'
            elif week=='星期三':str1='Wed'
            elif week=='星期四':str1='Thu'
            elif week=='星期五':str1='Fri'
            elif week=='星期六':str1='Sat'
            elif week=='星期日':str1='Sun'
            response_dic = {'status': 111, 'msg': '获取到页面传来的信息'}
            str=str1+classnum
            back=courseno+techno
            print(str)
            if num == '一次':
                back='*'+back
            elif num == '单周':
                back=back+'/'
            elif num == '双周':
                back='/'+back
            # classId = back.split(' ')[0]
            # teachId = back.split(' ')[1]
            else:
                back=' '
            #每周有点bug
            if tempclasstype == '教室编号':
                if name:
                    if name.isdigit():
                        #教室名称
                        cname=models.Classroom.objects.filter(cid=name,campus_id=camp).values('cname')
                        if cname.count() == 0:
                            print('cname.count')
                            response_dic = {'status': 111, 'msg': '没有该教室信息！'}
                        else:
                            for p in cname:
                                cname = p['cname']
                                print(cname)
                            conn = pymysql.connect(
                                host='127.0.0.1',
                                user='root',
                                passwd='12345678',
                                db='dg11',
                                port=3306,
                                charset='utf8'
                            )
                            cursor = conn.cursor()
                            sql = "UPDATE app01_arrangement set %s='%s' where RoomID_id='%s' and campus_id=%s;" % (
                                            str, back, name,camp)
                            # sql = "UPDATE app01_arrangement set Mon1_2='1223' where RoomID_id='666' and campus_id=2;"
                            cursor.execute(sql)
                            print("更新数据成功")
                            # 提交到数据库执行
                            conn.commit()
                            sql = "UPDATE app01_Cou set F1='%s' where coID='%s' and TEACHNO='%s' and campus_id='%s';" % (
                                            cname,courseno,techno,camp)
                            cursor.execute(sql)
                            # 提交到数据库执行
                            conn.commit()
                            cursor.close()
                            conn.close()
                            response_dic = {'status': 100, 'msg': None}
                    else:
                        response_dic = {'status': 111, 'msg':'教室编号请填写数字！'}
                else:
                    response_dic = {'status': 111, 'msg': '请填写完整信息！'}
            elif tempclasstype == '教室容量':
                if name:
                    if name.isdigit():
                        remain = models.Parameter.objects.filter(id=1).values('Remainder')
                        for q in remain:
                            remain = q['Remainder']
                        remain=remain+int(name)
                        if type == '多媒体':
                            type = 1
                        elif type == '语音室':
                            type = 2
                        else:
                            type = 3
                        models.Classroom.objects.filter(capacity__gte=remain,ctype_id=type,campus_id=camp).values('coID','TOTALS','TIMETEXT','TIMESET','NAME','TEACHNO','NOTUSEROOM','ROOM').order_by('-TOTALS', 'coID', 'TEACHNO')
                        response_dic={'status': 100, 'msg': None}
                    else:
                        response_dic = {'status': 111, 'msg': '教室容量请填写数字！'}
                else:
                    response_dic = {'status': 111, 'msg': '请填写完整信息！'}
        else:
            response_dic = {'status': 111, 'msg': '请填写完整信息'}
    return JsonResponse(response_dic)