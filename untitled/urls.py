"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views,lack,ChangeRoom,ChangeCourse,Arrangement
from django.conf.urls import url,include
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


urlpatterns = [
     # index-3.html中的all-professors.html修改成all-professors/即可
     # path('all-professors/', views.allprofessors),
     #首先进入登录界面
     path('admin/', admin.site.urls),
     path('', views.login),
     path('login.html',views.login),
     path('index.html', views.index),
     path('register.html',views.register),
     path('forget.html',views.forget),
     path('Recover.html',views.recover),
     path('PerAdmin.html',views.PerAdmin),
     path('DelAdmin.html',views.DelAdmin),
     path('AlterParameter.html', views.AlterParameter),
     path('AlterPassword.html', views.AlterPassword),

     #教室操作
     path('Room.html', ChangeRoom.Room),
     path('AlterRoom1.html', ChangeRoom.AlterRoom1),
     path('DelRoom.html', ChangeRoom.DelRoom),
     path('RoomSelect2.html', ChangeRoom.RoomSelect2),
     path('RoomSelect2Redict.html', ChangeRoom.RoomSelect2Redict),
     path('RoomSelect1.html', ChangeRoom.RoomSelect1),
     path('RoomSelect1Redict.html', ChangeRoom.RoomSelect1Redict),
     path('AddRoom.html', ChangeRoom.AddRoom),
     path('UploadRoom.html', ChangeRoom.UploadRoom),

     # 课程操作
     path('ClassView1.html', ChangeCourse.ClassView1),
     path('AlterClass.html', ChangeCourse.AlterClass),
     path('AddClass.html', ChangeCourse.AddClass),
     path('DelClass.html', ChangeCourse.DelClass),
     path('UploadCourse.html', ChangeCourse.UploadCourse),

     path('AlterClass3.html', ChangeCourse.AlterClass3),
     path('ArrangeRes.html', Arrangement.ArrangeRes),
     #仅仅是自动排课界面的显示
     # path('AutoArrange.html', views.AutoArrange),
     #自动选课业务逻辑
     path('AutoArrange.html', lack.lack),
     #自动选课结果显示
     path('AutoArrangeRes.html',lack.AutoArrangeRes),
     #未排课程
     path('NotArrange.html', Arrangement.NotArrange),
     path('TempArrange.html',Arrangement.TempArrange),
     # path('TempArrange1.html', views.TempArrange1),
     #教室总表
     #仅仅界面显示
     path('Summary.html', views.Summary),
     #用于条件查询
     # path('Summary_1.html', views.Summary_1),
     path('Summary1.html', views.Summary1),
     #教室简表
     path('Simple.html', views.Simple),
     path('Simple_1.html', views.Simple_1),
     path('Simple1.html', views.Simple1),
     path('test.html', views.test),






     path('edit-student.html',views.EditStudent),



     # url(r'^$', views.index),
    # url(r'^', include('templates.urls')),
]