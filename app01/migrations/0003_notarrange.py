# Generated by Django 3.0.4 on 2021-07-20 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20210720_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotArrange',
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