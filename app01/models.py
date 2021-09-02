from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

#创建数据库
# 用户类型
class UserType(models.Model):
    UserTypeID=models.AutoField(primary_key=True)
    UserTypeName=models.CharField(max_length=255)
# 校区
class Campus(models.Model):
    CampusId=models.IntegerField(primary_key=True)
    CampName=models.CharField(null=False,max_length=255)

# 教室类型
class ClassroomType(models.Model):
    TypeId=models.IntegerField(primary_key=True)
    TypeName=models.CharField(null=False,max_length=255)

# Create your models here.
class UserInfo(AbstractUser):
    nid=models.AutoField(primary_key=True)
    telephone = models.BigIntegerField(null=True)
    create_date = models.DateField(auto_now_add=True)
    UserType=models.ForeignKey(UserType,null=True, blank=True, on_delete=models.SET_NULL,db_constraint=False)
    # 校区
    campus = models.ForeignKey(Campus, null=True, blank=True, on_delete=models.SET_NULL, db_constraint=False)

# 教室
class Classroom(models.Model):
    # 教室编号(默认唯一)
    cid=models.CharField(max_length=254,primary_key=True)
    # 教室名称
    cname=models.CharField(max_length=256)
    # 容量
    capacity=models.IntegerField()
    # 教室类型
    ctype=models.ForeignKey(ClassroomType,null=True, blank=True, on_delete=models.SET_NULL,db_constraint=False)
    # 考试人数
    cnum=models.IntegerField(null=True)
    # 是否可用
    cuse=models.CharField(max_length=256)
    # 校区
    campus=models.ForeignKey(Campus,null=True, blank=True, on_delete=models.SET_NULL,db_constraint=False)

# 课程
class Cou(models.Model):
    # 课程大类编号
    coID=models.CharField(max_length=255)
    NAME=models.CharField(max_length=256)
    # 学分
    CREDIT=models.IntegerField()
    # 课程编号
    TEACHNO=models.CharField(max_length=256)
    # 教师名称
    TEACHNAME=models.CharField(max_length=256)
    # 教师工号
    TEACHID=models.CharField(max_length=256,null=True)
    # 上课时间
    TIMETEXT=models.CharField(max_length=256)
    # 二进制表示
    TIMESET=models.CharField(max_length=256)
    # 教室类型
    ROOM=models.ForeignKey(ClassroomType,null=True, blank=True, on_delete=models.SET_NULL,db_constraint=False)
    # 教室名称
    F1=models.CharField(max_length=256,null=True)
    # 是否可用
    NOTUSEROOM=models.CharField(max_length=256)
    # 选课总人数
    TOTALS=models.IntegerField()
    # 容量
    ENROLLS=models.IntegerField()
    #校区名称
    campus = models.ForeignKey(Campus,null=True, blank=True, on_delete=models.SET_NULL,db_constraint=False)
    # 排课标志
    flag=models.CharField(max_length=256,default='0')


    MARK=models.IntegerField()
    DELROLE=models.CharField(max_length=256,null=True)
    COLLEGEID=models.IntegerField()
    SPECIALITYID=models.CharField(max_length=256)
    TIMESET1 = models.CharField(max_length=256,null=True)
    ROOM1 = models.CharField(max_length=256, null=True)
    F2=models.CharField(max_length=256,null=True)

    class Meta:
        unique_together=(("TEACHNO","coID"),)
# 参数
class Parameter(models.Model):
    # 校名
    School=models.CharField(max_length=256,null=True)
    # 校区
    Campus=models.ForeignKey(Campus,null=True, blank=True, on_delete=models.SET_NULL,db_constraint=False)
    # 年
    SYear=models.CharField(max_length=256,null=True)
    # 学期
    Semester=models.CharField(max_length=256,null=True)
    # 作为余量
    Remainder=models.IntegerField(null=True)

#排课表
class Arrangement(models.Model):
    RoomID=models.ForeignKey(Classroom,null=True, blank=True, on_delete=models.SET_NULL,db_constraint=False)
    campus = models.ForeignKey(Campus,null=True, blank=True, on_delete=models.SET_NULL,db_constraint=False)
    Enroll=models.IntegerField(default=0)
    Mon1_2=models.CharField(max_length=256,null=True)
    Mon3_4=models.CharField(max_length=256,null=True)
    Mon5_6=models.CharField(max_length=256,null=True)
    Mon7_8=models.CharField(max_length=256,null=True)
    Mon9_10=models.CharField(max_length=256,null=True)
    Mon11_13=models.CharField(max_length=256,null=True)
    Tue1_2=models.CharField(max_length=256,null=True)
    Tue3_4 = models.CharField(max_length=256,null=True)
    Tue5_6 = models.CharField(max_length=256,null=True)
    Tue7_8 = models.CharField(max_length=256,null=True)
    Tue9_10 = models.CharField(max_length=256,null=True)
    Tue11_13 = models.CharField(max_length=256,null=True)
    Wed1_2 = models.CharField(max_length=256,null=True)
    Wed3_4 = models.CharField(max_length=256,null=True)
    Wed5_6 = models.CharField(max_length=256,null=True)
    Wed7_8 = models.CharField(max_length=256,null=True)
    Wed9_10 = models.CharField(max_length=256,null=True)
    Wed11_13 = models.CharField(max_length=256,null=True)
    Thu1_2 = models.CharField(max_length=256,null=True)
    Thu3_4 = models.CharField(max_length=256,null=True)
    Thu5_6 = models.CharField(max_length=256,null=True)
    Thu7_8 = models.CharField(max_length=256,null=True)
    Thu9_10 = models.CharField(max_length=256,null=True)
    Thu11_13 = models.CharField(max_length=256,null=True)
    Fri1_2 = models.CharField(max_length=256,null=True)
    Fri3_4 = models.CharField(max_length=256,null=True)
    Fri5_6 = models.CharField(max_length=256,null=True)
    Fri7_8 = models.CharField(max_length=256,null=True)
    Fri9_10 = models.CharField(max_length=256,null=True)
    Fri11_13 = models.CharField(max_length=256,null=True)
    Sat1_2 = models.CharField(max_length=256,null=True)
    Sat3_4 = models.CharField(max_length=256,null=True)
    Sat5_6 = models.CharField(max_length=256,null=True)
    Sat7_8 = models.CharField(max_length=256,null=True)
    Sat9_10 = models.CharField(max_length=256,null=True)
    Sat11_13 = models.CharField(max_length=256,null=True)
    Sun1_2 = models.CharField(max_length=256,null=True)
    Sun3_4 = models.CharField(max_length=256,null=True)
    Sun5_6 = models.CharField(max_length=256,null=True)
    Sun7_8 = models.CharField(max_length=256,null=True)
    Sun9_10 = models.CharField(max_length=256,null=True)
    Sun11_13 = models.CharField(max_length=256,null=True)

class Permission(models.Model):
    class Meta:
        permissions=(
            ('管理用户','管理用户'),
            ('浏览教室','浏览教室'),
            ('change_app01_classroom_tem','修改教室'),
            ('view_app01_class_tem','浏览课程'),
            ('change_app01_class_tem','修改课程'),
            ('change_app01_arrange_tem','自动分配'),
            ('change_app01_temp_tem','临时调配'),
            ('view_app01_result_tem','查看报表'),
            ('change_app01_parameter_tem','修改参数'),
        )

class NotArrange(models.Model):
    # 课程大类编号
    coID=models.CharField(max_length=255)
    NAME=models.CharField(max_length=256)
    # 学分
    CREDIT=models.IntegerField()
    # 课程编号
    TEACHNO=models.CharField(max_length=256)
    # 教师名称
    TEACHNAME=models.CharField(max_length=256)
    # 教师工号
    TEACHID=models.CharField(max_length=256,null=True)
    # 上课时间
    TIMETEXT=models.CharField(max_length=256)
    # 二进制表示
    TIMESET=models.CharField(max_length=256)
    # 教室类型
    ROOM=models.ForeignKey(ClassroomType,null=True, blank=True, on_delete=models.SET_NULL,db_constraint=False)
    # 教室名称
    F1=models.CharField(max_length=256,null=True)
    # 是否可用
    NOTUSEROOM=models.CharField(max_length=256)
    # 选课总人数
    TOTALS=models.IntegerField()
    # 容量
    ENROLLS=models.IntegerField()
    #校区名称
    campus = models.ForeignKey(Campus,null=True, blank=True, on_delete=models.SET_NULL,db_constraint=False)
    # 排课标志
    flag=models.CharField(max_length=256,default='0')


    MARK=models.IntegerField()
    DELROLE=models.CharField(max_length=256,null=True)
    COLLEGEID=models.IntegerField()
    SPECIALITYID=models.CharField(max_length=256)
    TIMESET1 = models.CharField(max_length=256,null=True)
    ROOM1 = models.CharField(max_length=256, null=True)
    F2=models.CharField(max_length=256,null=True)

    class Meta:
        unique_together=(("TEACHNO","coID"),)