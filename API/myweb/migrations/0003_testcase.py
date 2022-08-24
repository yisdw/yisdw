# Generated by Django 4.1 on 2022-08-23 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myweb', '0002_alter_project_dev_owner_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('case_name', models.CharField(max_length=50, verbose_name='用例名称')),
                ('request_data', models.CharField(default='', max_length=1024, verbose_name='请求数据')),
                ('uri', models.CharField(default='', max_length=1024, verbose_name='接口地址')),
                ('assert_key', models.CharField(max_length=1024, null=True, verbose_name='断言内容')),
                ('maintainer', models.CharField(default='', max_length=1024, verbose_name='编写人员')),
                ('extract_var', models.CharField(max_length=1024, null=True, verbose_name='提取变量表达式')),
                ('request_method', models.CharField(max_length=1024, null=True, verbose_name='请求方式')),
                ('status', models.IntegerField(help_text='0：表示有效，1：表示无效，用于软删除', null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('belong_module', smart_selects.db_fields.GroupedForeignKey(group_field='belong_project', on_delete=django.db.models.deletion.CASCADE, to='myweb.module', verbose_name='所属模块')),
                ('belong_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myweb.project', verbose_name='所属项目')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='责任人')),
            ],
            options={
                'verbose_name': '测试用例表',
                'verbose_name_plural': '测试用例表',
            },
        ),
    ]
