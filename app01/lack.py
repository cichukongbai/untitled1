import numpy
import pymysql
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin

from django.contrib.auth.models import Permission
from app01 import models

ch = numpy.zeros(42)
pan = numpy.zeros(42)
B = numpy.zeros((42, 3), dtype=numpy.object)
C = numpy.zeros((100, 2), dtype=numpy.object)
D = numpy.zeros((100, 2), dtype=numpy.object)
A=numpy.zeros((1,3),dtype=numpy.object)
i=0
j=0

str1 = ['RoomID', 'Mon1_2', 'Mon3_4', 'Mon5_6', 'Mon7_8','Mon9_10', 'Mon11_13', 'Tue1_2', 'Tue3_4', 'Tue5_6',
        'Tue7_8', 'Tue9_10', 'Tue11_13', 'Wed1_2', 'Wed3_4','Wed5_6', 'Wed7_8', 'Wed9_10', 'Wed11_13', 'Thu1_2',
        'Thu3_4', 'Thu5_6', 'Thu7_8', 'Thu9_10', 'Thu11_13','Fri1_2', 'Fri3_4', 'Fri5_6', 'Fri7_8', 'Fri9_10',
        'Fri11_13', 'Sat1_2', 'Sat3_4', 'Sat5_6', 'Sat7_8','Sat9_10', 'Sat11_13', 'Sun1_2', 'Sun3_4', 'Sun5_6',
        'Sun7_8', 'Sun9_10', 'Sun11_13']
# @login_required(login_url='/login.html')
def CheckSet(recordset, A):
    for i in range(1, 43):
        if ch[i] != 0:
            ch[i] = 0
    if recordset == None and A[1, 1] == '':
        result = 1
    elif recordset == None and A[1, 1] == '单':
        result = 2
    elif recordset == None and A[1, 1] == '双':
        result = 1
    elif recordset[0] == '/' and A[1, 1] == '单':
        result = 4
    elif recordset[-1] == '/' and A[1, 1] == '双':
        result = 5
    else:
        result = 0
    ch[1] = result
    ch[0] = A[0, 0]
    return render(request, 'AutoArrange.html')


# @login_required(login_url='/login.html')
def Handle(camp):
    print('======Handle camp=======')
    print(camp)
    # res=0
    if camp == '0':
        print('宝山处理完毕')
        ab = models.Cou.objects.filter(TIMETEXT__contains='上机', campus_id=camp)
        for a in ab:
            print(a.coID)
            f = list(a.TIMESET)
            print(a.TIMETEXT.split(" "))
            b = a.TIMETEXT.split(" ")[-2]
            c = int(b.split("-")[0][-1])
            week = b.split("-")[0][-2]
            d = int(b.split("-")[1][0])

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
            models.Cou.objects.filter(coID=a.coID,  campus_id=camp).update(TIMESET1=re)
        res=1
    elif camp == '1':
        print('嘉定处理完毕')
        ab = models.Cou.objects.filter(TIMETEXT__contains='上机', campus_id=camp)
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
            models.Cou.objects.filter(coID=a.coID, campus_id=camp).update(TIMESET1=re)
        res=1
    elif camp == '2':
        print('延长处理完毕')
        ab = models.Cou.objects.filter(TIMETEXT__contains='上机',campus_id=camp)
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
            models.Cou.objects.filter(coID=a.coID, campus_id=camp).update(TIMESET1=re)
        res=1
    elif camp == '3':
        print('全部处理完毕')
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
        res=1
    return res


# 课程处理
# @login_required(login_url='/login.html')
def HandleClass(request):
    if request.method == 'GET':
        return render(request, 'HandleClass.html')

    else:
        request.session['handle'] = True
        camp=request.POST.get('id_camp')

        if camp == 0:
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
        elif camp == 1:
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
        elif camp == 2:
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
def CheckTimeSet(timeset):
    print('收到')
    for d in range(0, 42):
        for x in range(0, 3):
            if B[d, x] != 0:
                B[d, x] = 0
    num = 1
    time1 = timeset.strip()
    pos1 = time1.find("1")
    pos2 = time1.find("2")
    pos3 = time1.find("3")
    if pos1 >= 0 or pos2 >= 0 or pos3 >= 0:
        for i in range(1, 8):
            beginpos = (i - 1) * 13
            time2 = time1[beginpos:beginpos + 13]
            if time2 != '0000000000000':
                if i == 1:
                    week = 'Mon'
                elif i == 2:
                    week = 'Tue'
                elif i == 3:
                    week = 'Wed'
                elif i == 4:
                    week = 'Thu'
                elif i == 5:
                    week = 'Fri'
                elif i == 6:
                    week = 'Sat'
                elif i == 7:
                    week = 'Sun'
                for j in range(1, 6):
                    beginpos = (j - 1) * 2
                    tempstr = time2[beginpos:(beginpos + 2)]
                    pos0 = tempstr.find("00")
                    if pos0 == -1:
                        pos1 = tempstr.find("1")
                        pos2 = tempstr.find("2")
                        pos3 = tempstr.find("3")
                        temp1 = str(2 * j - 1)
                        temp2 = str(2 * j)
                        if pos1 >= 0:
                            B[num, 0] = (i - 1) * 6 + j
                            B[num, 1] = "单"
                            B[num, 2] = week + temp1 + '_' + temp2
                            num = num + 1
                        elif pos2 >= 0:
                            B[num, 0] = (i - 1) * 6 + j
                            B[num, 1] = "双"
                            B[num, 2] = week + temp1 + '_' + temp2
                            num = num + 1
                        elif pos3 >= 0:
                            B[num, 0] = (i - 1) * 6 + j
                            B[num, 1] = ""
                            B[num, 2] = week + temp1 + '_' + temp2
                            num = num + 1
                tempstr = time2[10:13]
                pos0 = tempstr.find('000')
                if pos0 == -1:
                    pos1 = tempstr.find('1')
                    pos2 = tempstr.find('2')
                    pos3 = tempstr.find('3')
                    if pos1 >= 0:
                        B[num, 0] = (i - 1) * 6 + 6
                        B[num, 1] = "单"
                        B[num, 2] = week + '11' + '_' + '13'
                        num = num + 1
                    elif pos2 >= 0:
                        B[num, 0] = (i - 1) * 6 + 6
                        B[num, 1] = "双"
                        B[num, 2] = week + '11' + '_' + '13'
                        num = num + 1
                    elif pos3 >= 0:
                        B[num, 0] = (i - 1) * 6 + 6
                        B[num, 1] = ""
                        B[num, 2] = week + '11' + '_' + '13'
                        num = num + 1
    B[0, 0] = num - 1

# @login_required(login_url='/login.html')
def lack(request):
    print("========lack函数==========")
    flag = 1
    if request.method == 'GET':
        print("AutoArrange")
        gg_list = models.Cou.objects.filter(flag=1)
        cc_list = models.Campus.objects.all()
        return render(request, 'AutoArrange.html', context={'gglist': gg_list, 'cclist': cc_list})
    else:
        print('1111111')
        id_a = request.POST.get('id_a')
        id_b = request.POST.get('id_b')
        remain=request.POST.get('id_remain')
        id_camp = request.POST.get('id_camp')
        type = 1
        # 取参数的第一个（最新）
        cid = models.Parameter.objects.filter(id=1).values('id')
        print('remain.isdigit()',remain.isdigit())
        if remain!='':
            if remain.isdigit():
                models.Parameter.objects.filter(id=1).update(Remainder=remain)
                # if id_b == 'not':
                #     print(id_camp)
                #     Handle(id_camp)
                # else:
                #     handle = False
                print('id_a, id_b', id_a, id_b)
                conn = pymysql.connect(
                    host='127.0.0.1',
                    user='root',
                    passwd='123456',
                    db='dg13',
                    port=3306,
                    charset='utf8'
                )
                cursor = conn.cursor()
                sql = "TRUNCATE TABLE app01_arrangement;"
                print("更新数据成功")
                cursor.execute(sql)
                # 提交到数据库执行
                conn.commit()
                conn.close()
                cursor.close()
                W = models.Classroom.objects.filter(campus_id=id_camp).values('cid', 'capacity')
                for i in W:
                    models.Arrangement.objects.create(RoomID_id=i['cid'], Enroll=i['capacity'], campus_id=id_camp)
                print('arrangeg更新完毕')

                # 松 未处理-----------------------------------------------------------------------
                if id_a == 'loose' and id_b == 'have':

                    recordcourse1 = models.Cou.objects.filter(TOTALS__gte=0, NOTUSEROOM='0', ROOM_id=type,
                                                              campus_id=id_camp, flag=0).values('coID', 'TOTALS',
                                                                                                'TIMETEXT', 'TIMESET',
                                                                                                'NAME', 'TEACHNO',
                                                                                                'NOTUSEROOM',
                                                                                                'ROOM_id').order_by(
                        '-TOTALS', 'coID', 'TEACHNO')
                    print(recordcourse1)
                    for p in recordcourse1:
                        print('___________新的课程————————————')
                        print(p['coID'])
                        CheckTimeSet(str(p['TIMESET']))
                        print(B[0,0])
                        if B[0, 0] > 0:
                            require1 = p['TOTALS'] + int(remain)
                            recordroom1 = models.Classroom.objects.filter(capacity__gte=require1, ctype=type, cuse='1',
                                                                          campus_id=id_camp).values(
                                'cid', 'cname', 'capacity', 'ctype', 'cnum', 'cuse').order_by('capacity')
                            if not (recordroom1):
                                print('没有合适教室，下一门课程')
                                continue
                            else:
                                for u in range(1, B[0, 0] + 1):
                                    for q in recordroom1:
                                        print('_________新的教室_________')
                                        pan = models.Arrangement.objects.filter(RoomID_id=q['cid'],
                                                                                campus_id=id_camp).values(str1[B[u, 0]])
                                        print(pan)
                                        op = str1[B[u, 0]]
                                        for ele in pan:
                                            oop = ele[op]
                                            if oop == None:
                                                flag = 1
                                            else:
                                                flag = 0
                                        print(flag)
                                        if flag == 1:
                                            print('=============')

                                            models.Cou.objects.filter(coID=p['coID'], TEACHNO=p['TEACHNO']).update(
                                                F1=q['cname'],
                                                flag=1)
                                            temp1 = ''
                                            temp = B[u, 2]
                                            if B[u, 1] == '':
                                                temp1 = p['coID'] + ' ' + p['TEACHNO']
                                                print(temp1)
                                            elif B[u, 1] == '单':
                                                temp1 = p['coID'] + ' ' + p['TEACHNO'] + '/'
                                            elif B[u, 1] == '双':
                                                temp1 = '/' + p['coID'] + ' ' + p['TEACHNO']
                                            conn = pymysql.connect(
                                                host='127.0.0.1',
                                                user='root',
                                                passwd='123456',
                                                db='dg13',
                                                port=3306,
                                                charset='utf8'
                                            )
                                            cursor = conn.cursor()
                                            print(q['cid'])
                                            sql = "UPDATE app01_arrangement set %s = '%s' where RoomID_id = '%s'" % (
                                            temp, temp1, pymysql.escape_string(q['cid']))
                                            print(temp, temp1)
                                            print("更新数据成功")
                                            cursor.execute(sql)
                                            conn.commit()
                                            break
                                        else:
                                            continue
                        else:
                            continue
                    response_dic = {'status': 103, 'msg': '分配完毕！'}

                # 松 处理-----------------------------------------------------------------------
                elif id_a == 'loose' and id_b == 'not':
                    print(id_camp)
                    handle=Handle(id_camp)
                    print(handle)
                    if handle != 1:
                        response_dic = {'status': 101, 'msg': '请先对课程进行预处理！'}
                    else:
                        recordcourse1 = models.Cou.objects.filter(TOTALS__gte=0, NOTUSEROOM='0', ROOM_id=type).values(
                            'coID',
                            'TOTALS',
                            'TIMETEXT',
                            'TIMESET',
                            'TIMESET1',
                            'NAME',
                            'TEACHNO',
                            'NOTUSEROOM',
                            'ROOM_id').order_by(
                            '-TOTALS', 'coID', 'TEACHNO')
                        for p in recordcourse1:
                            print(p['TIMESET1'])
                            if p['TIMESET1'] == '':
                                CheckTimeSet(p['TIMESET'])

                            else:
                                CheckTimeSet(p['TIMESET1'])
                            if B[0, 0] > 0:
                                require1 = p['TOTALS'] + int(remain)
                                recordroom1 = models.Classroom.objects.filter(capacity__gte=require1, ctype=type,
                                                                              cuse='1').values(
                                    'cid', 'cname', 'capacity', 'ctype', 'cnum', 'cuse').order_by('capacity')
                                if not (recordroom1):
                                    print(p['coID'])
                                    print(p['TEACHNO'])
                                    # aaa = models.Cou.objects.filter(coID=p['coID'], TEACHNO=p['TEACHNO']).values(
                                    #     'coID', 'NAME', 'TEACHNO', 'TEACHNAME', 'ROOM_id', 'F1', 'NOTUSEROOM',
                                    #     'TOTALS', 'ENROLLS', 'campus_id')
                                    # for i in aaa:
                                    #     models.NotArrange.objects.create(coID=i['coID'], NAME=i['NAME'],
                                    #                                      TEACHNO=i['TEACHNO'],
                                    #                                      TEACHNAME=i['TEACHNAME'], ROOM_id=i['ROOM_id'],
                                    #                                      F1=i['F1'], NOTUSEROOM=i['NOTUSEROOM'],
                                    #                                      TOTALS=i['TOTALS'], ENROLLS=i['ENROLLS'],
                                    #                                      campus_id=i['campus_id'])
                                    continue
                                else:
                                    # print(recordroom1)
                                    for u in range(1, B[0, 0] + 1):
                                        for q in recordroom1:
                                            pan = models.Arrangement.objects.filter(RoomID_id=q['cid']).values(
                                                str1[B[u, 0]])
                                            print(pan)
                                            op = str1[B[u, 0]]

                                            for ele in pan:
                                                oop = ele[op]
                                                if oop == None:
                                                    flag = 1
                                                else:
                                                    flag = 0
                                            # print(flag)
                                            if flag == 1:
                                                print('=============')

                                                models.Cou.objects.filter(coID=p['coID'], TEACHNO=p['TEACHNO']).update(
                                                    F1=q['cname'],
                                                    flag=1)

                                                # for n in range(1, B[0, 0] + 1):
                                                temp1 = ''
                                                temp = B[u, 2]
                                                if B[u, 1] == '':
                                                    temp1 = p['coID'] + ' ' + p['TEACHNO']
                                                    print(temp1)
                                                elif B[u, 1] == '单':
                                                    temp1 = p['coID'] + ' ' + p['TEACHNO'] + '/'
                                                elif B[u, 1] == '双':
                                                    temp1 = '/' + p['coID'] + ' ' + p['TEACHNO']
                                                conn = pymysql.connect(
                                                    host='localhost',
                                                    user='root',
                                                    passwd='123456',
                                                    db='dg13',
                                                    port=3306,
                                                    charset='utf8'
                                                )

                                                cursor = conn.cursor()
                                                print(q['cid'])
                                                sql = "UPDATE app01_arrangement set %s = '%s' where RoomID_id = '%s'" % (
                                                    temp, temp1, pymysql.escape_string(q['cid']))
                                                print(temp, temp1)
                                                print("更新数据成功")
                                                cursor.execute(sql)
                                                conn.commit()


                                                break
                                            else:
                                                continue
                                        # continue
                            else:
                                continue
                        response_dic = {'status': 103, 'msg': '分配完毕！'}

                # 紧 未处理-----------------------------------------------------------------------
                elif id_a == 'lack' and id_b == 'have':
                    recordcourse1 = models.Cou.objects.filter(TOTALS__gte=0, NOTUSEROOM='0', ROOM_id=type).values(
                        'coID', 'TOTALS', 'TIMETEXT', 'TIMESET', 'NAME', 'TEACHNO', 'NOTUSEROOM', 'ROOM_id').order_by(
                        '-TOTALS', 'coID', 'TEACHNO')
                    for p in recordcourse1:
                        CheckTimeSet(p['TIMESET'])
                        if B[0, 0] > 0:
                            require1 = p['TOTALS'] + int(remain)
                            recordroom1 = models.Classroom.objects.filter(capacity__gte=require1, ctype=type,
                                                                          cuse='1').values(
                                'cid', 'cname', 'capacity', 'ctype', 'cnum', 'cuse').order_by('capacity')
                            if not (recordroom1):
                                print(p['coID'])
                                print(p['TEACHNO'])
                                aaa = models.Cou.objects.filter(coID=p['coID'], TEACHNO=p['TEACHNO']).values('coID',
                                                                                                             'NAME',
                                                                                                             'TEACHNO',
                                                                                                             'TEACHNAME',
                                                                                                             'ROOM_id',
                                                                                                             'F1',
                                                                                                             'NOTUSEROOM',
                                                                                                             'TOTALS',
                                                                                                             'ENROLLS',
                                                                                                             'campus_id')
                                for i in aaa:
                                    models.NotArrange.objects.create(coID=i['coID'], NAME=i['NAME'],
                                                                     TEACHNO=i['TEACHNO'], TEACHNAME=i['TEACHNAME'],
                                                                     ROOM_id=i['ROOM_id'], F1=i['F1'],
                                                                     NOTUSEROOM=i['NOTUSEROOM'], TOTALS=i['TOTALS'],
                                                                     ENROLLS=i['ENROLLS'], campus_id=i['campus_id'])

                                continue
                            else:
                                for q in recordroom1:
                                    for u in range(1, B[0, 0] + 1):
                                        pan = models.Arrangement.objects.filter(RoomID_id=q['cid']).values(
                                            str1[B[u, 0]])
                                        print(pan)
                                        op = str1[B[u, 0]]
                                        for ele in pan:
                                            oop = ele[op]
                                            if oop == None:
                                                flag = 1
                                            else:
                                                flag = 0
                                    # print(flag)
                                    if flag == 1:
                                        print('=============')

                                        models.Cou.objects.filter(coID=p['coID'], TEACHNO=p['TEACHNO']).update(
                                            F1=q['cname'],
                                            flag=1)

                                        for n in range(1, B[0, 0] + 1):
                                            temp = B[n, 2]
                                            if B[n, 1] == '':
                                                temp1 = p['coID'] + ' ' + p['TEACHNO']
                                                print(temp1)
                                            elif B[n, 1] == '单':
                                                temp1 = p['coID'] + ' ' + p['TEACHNO'] + '/'
                                            elif B[n, 1] == '双':
                                                temp1 = '/' + p['coID'] + ' ' + p['TEACHNO']
                                            conn = pymysql.connect(
                                                host='localhost',
                                                user='root',
                                                passwd='123456',
                                                db='dg13',
                                                port=3306,
                                                charset='utf8'
                                            )
                                            cursor = conn.cursor()
                                            sql = "UPDATE app01_arrangement set %s='%s' where RoomID_id='%s';" % (
                                                temp, temp1, q['cid'])
                                            print("更新数据成功")
                                            cursor.execute(sql)
                                            # 提交到数据库执行
                                            conn.commit()

                                    else:
                                        continue
                                    break
                    # print(C)
                    response_dic = {'status': 103, 'msg': '分配完毕！'}

                # 紧 处理-----------------------------------------------------------------------
                elif id_a == 'lack' and id_b == 'not':
                    Handle(id_camp)
                    recordcourse1 = models.Cou.objects.filter(TOTALS__gte=0, NOTUSEROOM='0', ROOM_id=type).values(
                        'coID',
                        'TOTALS',
                        'TIMETEXT',
                        'TIMESET',
                        'TIMESET1',
                        'NAME',
                        'TEACHNO',
                        'NOTUSEROOM',
                        'ROOM_id').order_by(
                        '-TOTALS', 'coID', 'TEACHNO')
                    for p in recordcourse1:
                        if p['TIMESET1'] == None:
                            CheckTimeSet(p['TIMESET'])
                            print('包含上机')
                        else:
                            CheckTimeSet(p['TIMESET'])
                            print('不包含上机')
                        print(B[0,0])
                        if B[0, 0] > 0:
                            require1 = p['TOTALS'] + int(remain)
                            recordroom1 = models.Classroom.objects.filter(capacity__gte=require1, ctype=type,
                                                                          cuse='1').values(
                                'cid', 'cname', 'capacity', 'ctype', 'cnum', 'cuse').order_by('capacity')
                            if not (recordroom1):
                                print(p['coID'])
                                print(p['TEACHNO'])
                                aaa = models.Cou.objects.filter(coID=p['coID'], TEACHNO=p['TEACHNO']).values(
                                    'coID', 'NAME', 'TEACHNO', 'TEACHNAME', 'ROOM_id', 'F1', 'NOTUSEROOM',
                                    'TOTALS', 'ENROLLS', 'campus_id')
                                for i in aaa:
                                    models.NotArrange.objects.create(coID=i['coID'], NAME=i['NAME'],
                                                                     TEACHNO=i['TEACHNO'],
                                                                     TEACHNAME=i['TEACHNAME'], ROOM_id=i['ROOM_id'],
                                                                     F1=i['F1'], NOTUSEROOM=i['NOTUSEROOM'],
                                                                     TOTALS=i['TOTALS'], ENROLLS=i['ENROLLS'],
                                                                     campus_id=i['campus_id'])
                                continue
                            else:
                                for q in recordroom1:
                                    for u in range(1, B[0, 0] + 1):
                                        pan = models.Arrangement.objects.filter(RoomID_id=q['cid']).values(
                                            str1[B[u, 0]])
                                        print(pan)
                                        op = str1[B[u, 0]]
                                        for ele in pan:
                                            oop = ele[op]
                                            if oop == None:
                                                flag = 1
                                            else:
                                                flag = 0
                                    # print(flag)
                                    if flag == 1:
                                        print('=============')

                                        models.Cou.objects.filter(coID=p['coID'], TEACHNO=p['TEACHNO']).update(
                                            F1=q['cname'],
                                            flag=1)

                                        for n in range(1, B[0, 0] + 1):
                                            temp = B[n, 2]
                                            if B[n, 1] == '':
                                                temp1 = p['coID'] + ' ' + p['TEACHNO']
                                                print(temp1)
                                            elif B[n, 1] == '单':
                                                temp1 = p['coID'] + ' ' + p['TEACHNO'] + '/'
                                            elif B[n, 1] == '双':
                                                temp1 = '/' + p['coID'] + ' ' + p['TEACHNO']
                                            conn = pymysql.connect(
                                                host='localhost',
                                                user='root',
                                                passwd='123456',
                                                db='dg13',
                                                port=3306,
                                                charset='utf8'
                                            )
                                            cursor = conn.cursor()
                                            sql = "UPDATE app01_arrangement set %s='%s' where RoomID_id='%s';" % (
                                                temp, temp1, q['cid'])
                                            print("更新数据成功")
                                            cursor.execute(sql)
                                            # 提交到数据库执行
                                            conn.commit()

                                    else:
                                        continue
                                    break

                        response_dic = {'status': 103, 'msg': '分配完毕！'}
                else:
                    response_dic = {'status': 104, 'msg': '操作有误'}

            else:
                response_dic = {'status': 105, 'msg': '请在系统功能里先设置参数！'}
                return JsonResponse(response_dic)
        else:
            response_dic = {'status': 105, 'msg': '请输入预留位置数量！'}
            return JsonResponse(response_dic)




        return JsonResponse(response_dic)



# 安排结果
@login_required(login_url='/login.html')
def AutoArrangeRes(request):
    print("=====AutoArrangeRes=====")
    # camp=request.session.get('id_camp',default='')
    # name = request.session.get('name', default='')
    # print('camp,name',camp,name)
    pa_list = models.Parameter.objects.filter(id=1)
    gglist=models.Cou.objects.filter()
    return render(request,'AutoArrange.html',context={'gglist':gglist,'palist':pa_list})
