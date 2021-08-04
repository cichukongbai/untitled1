# Generated by Django 3.0.4 on 2021-07-20 04:20

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('CampusId', models.IntegerField(primary_key=True, serialize=False)),
                ('CampName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ClassroomType',
            fields=[
                ('TypeId', models.IntegerField(primary_key=True, serialize=False)),
                ('TypeName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('views_app01_manager_tem', '管理用户'), ('views_app01_classroom_tem', '浏览教室'), ('change_app01_classroom_tem', '修改教室'), ('view_app01_class_tem', '浏览课程'), ('change_app01_class_tem', '修改课程'), ('change_app01_arrange_tem', '自动分配'), ('change_app01_temp_tem', '临时调配'), ('view_app01_result_tem', '查看报表'), ('change_app01_parameter_tem', '修改参数')),
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('UserTypeID', models.AutoField(primary_key=True, serialize=False)),
                ('UserTypeName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School', models.CharField(max_length=256, null=True)),
                ('SYear', models.CharField(max_length=256, null=True)),
                ('Semester', models.CharField(max_length=256, null=True)),
                ('Remainder', models.IntegerField(null=True)),
                ('Campus', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Campus')),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=256)),
                ('capacity', models.IntegerField()),
                ('cnum', models.IntegerField(null=True)),
                ('cuse', models.CharField(max_length=256)),
                ('campus', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Campus')),
                ('ctype', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.ClassroomType')),
            ],
        ),
        migrations.CreateModel(
            name='Arrangement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enroll', models.IntegerField(default=0)),
                ('Mon1_2', models.CharField(max_length=256, null=True)),
                ('Mon3_4', models.CharField(max_length=256, null=True)),
                ('Mon5_6', models.CharField(max_length=256, null=True)),
                ('Mon7_8', models.CharField(max_length=256, null=True)),
                ('Mon9_10', models.CharField(max_length=256, null=True)),
                ('Mon11_13', models.CharField(max_length=256, null=True)),
                ('Tue1_2', models.CharField(max_length=256, null=True)),
                ('Tue3_4', models.CharField(max_length=256, null=True)),
                ('Tue5_6', models.CharField(max_length=256, null=True)),
                ('Tue7_8', models.CharField(max_length=256, null=True)),
                ('Tue9_10', models.CharField(max_length=256, null=True)),
                ('Tue11_13', models.CharField(max_length=256, null=True)),
                ('Wed1_2', models.CharField(max_length=256, null=True)),
                ('Wed3_4', models.CharField(max_length=256, null=True)),
                ('Wed5_6', models.CharField(max_length=256, null=True)),
                ('Wed7_8', models.CharField(max_length=256, null=True)),
                ('Wed9_10', models.CharField(max_length=256, null=True)),
                ('Wed11_13', models.CharField(max_length=256, null=True)),
                ('Thu1_2', models.CharField(max_length=256, null=True)),
                ('Thu3_4', models.CharField(max_length=256, null=True)),
                ('Thu5_6', models.CharField(max_length=256, null=True)),
                ('Thu7_8', models.CharField(max_length=256, null=True)),
                ('Thu9_10', models.CharField(max_length=256, null=True)),
                ('Thu11_13', models.CharField(max_length=256, null=True)),
                ('Fri1_2', models.CharField(max_length=256, null=True)),
                ('Fri3_4', models.CharField(max_length=256, null=True)),
                ('Fri5_6', models.CharField(max_length=256, null=True)),
                ('Fri7_8', models.CharField(max_length=256, null=True)),
                ('Fri9_10', models.CharField(max_length=256, null=True)),
                ('Fri11_13', models.CharField(max_length=256, null=True)),
                ('Sat1_2', models.CharField(max_length=256, null=True)),
                ('Sat3_4', models.CharField(max_length=256, null=True)),
                ('Sat5_6', models.CharField(max_length=256, null=True)),
                ('Sat7_8', models.CharField(max_length=256, null=True)),
                ('Sat9_10', models.CharField(max_length=256, null=True)),
                ('Sat11_13', models.CharField(max_length=256, null=True)),
                ('Sun1_2', models.CharField(max_length=256, null=True)),
                ('Sun3_4', models.CharField(max_length=256, null=True)),
                ('Sun5_6', models.CharField(max_length=256, null=True)),
                ('Sun7_8', models.CharField(max_length=256, null=True)),
                ('Sun9_10', models.CharField(max_length=256, null=True)),
                ('Sun11_13', models.CharField(max_length=256, null=True)),
                ('RoomID', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Classroom')),
                ('campus', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Campus')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('telephone', models.BigIntegerField(null=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('UserType', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.UserType')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coID', models.CharField(max_length=255)),
                ('NAME', models.CharField(max_length=256)),
                ('CREDIT', models.IntegerField()),
                ('TEACHNO', models.CharField(max_length=256)),
                ('TEACHNAME', models.CharField(max_length=256)),
                ('TEACHID', models.CharField(max_length=256, null=True)),
                ('TIMETEXT', models.CharField(max_length=256)),
                ('TIMESET', models.CharField(max_length=256)),
                ('F1', models.CharField(max_length=256, null=True)),
                ('NOTUSEROOM', models.CharField(max_length=256)),
                ('TOTALS', models.IntegerField()),
                ('ENROLLS', models.IntegerField()),
                ('flag', models.CharField(default='0', max_length=256)),
                ('MARK', models.IntegerField()),
                ('DELROLE', models.CharField(max_length=256, null=True)),
                ('COLLEGEID', models.IntegerField()),
                ('SPECIALITYID', models.CharField(max_length=256)),
                ('TIMESET1', models.CharField(max_length=256, null=True)),
                ('ROOM1', models.CharField(max_length=256, null=True)),
                ('F2', models.CharField(max_length=256, null=True)),
                ('ROOM', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.ClassroomType')),
                ('campus', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Campus')),
            ],
            options={
                'unique_together': {('TEACHNO', 'coID')},
            },
        ),
    ]