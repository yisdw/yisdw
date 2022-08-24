# Generated by Django 4.1 on 2022-08-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='项目名称')),
                ('proj_owner', models.CharField(max_length=20, verbose_name='项目负责人')),
                ('dev_owner', models.CharField(max_length=20, verbose_name='开发负责人')),
                ('desc', models.CharField(max_length=100, null=True, verbose_name='项目描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='项目创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='项目更新时间')),
            ],
            options={
                'verbose_name': '项目信息表',
                'verbose_name_plural': '项目信息表',
            },
        ),
    ]
