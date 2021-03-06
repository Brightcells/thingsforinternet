# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('dh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('api', models.CharField(blank=True, help_text='API \u540d\u79f0', max_length=255, null=True, verbose_name='api')),
                ('func', models.TextField(blank=True, help_text='API  \u529f\u80fd\u63cf\u8ff0', null=True, verbose_name='function')),
                ('tag', models.CharField(blank=True, help_text='API \u6807\u7b7e', max_length=255, null=True, verbose_name='tag')),
                ('url', models.URLField(blank=True, help_text='API \u8be6\u7ec6\u4fe1\u606f', max_length=255, null=True, verbose_name='url')),
                ('visit', models.IntegerField(default=0, help_text='API \u8bbf\u95ee\u6570', verbose_name='visit')),
                ('evaluate', models.IntegerField(default=0, help_text='API \u8bc4\u4ef7\u6570', verbose_name='evaluate')),
                ('like', models.IntegerField(default=0, help_text='API \u70b9\u8d5e\u6570', verbose_name='like')),
                ('unlike', models.IntegerField(default=0, help_text='API \u88ab\u8e29\u6570', verbose_name='unlike')),
                ('follow', models.IntegerField(default=0, help_text='API \u5173\u6ce8\u6570', verbose_name='follow')),
                ('display', models.BooleanField(default=True, help_text='API \u662f\u5426\u663e\u793a True for display && False for not', verbose_name='display')),
                ('author', models.ForeignKey(blank=True, help_text='API \u521b\u5efa\u8005', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserInfo', verbose_name='author')),
            ],
            options={
                'db_table': 'apiinfo',
                'verbose_name': 'apiinfo',
                'verbose_name_plural': 'apiinfo',
            },
        ),
        migrations.CreateModel(
            name='ClassifyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('name', models.CharField(help_text='\u5206\u7c7b\u540d\u79f0', max_length=255, verbose_name='name')),
                ('title', models.CharField(blank=True, help_text='\u5206\u7c7b\u6807\u9898', max_length=255, null=True, verbose_name='title')),
                ('descr', models.TextField(blank=True, help_text='\u5206\u7c7b\u63cf\u8ff0', null=True, verbose_name='description')),
                ('num', models.IntegerField(default=0, help_text='\u5206\u7c7b\u7ad9\u70b9\u6570', verbose_name='num')),
                ('visit', models.IntegerField(default=0, help_text='\u5206\u7c7b\u7ad9\u70b9\u70b9\u51fb\u6570', verbose_name='visit')),
                ('position', models.IntegerField(default=0, help_text='\u5206\u7c7b\u4f4d\u7f6e', verbose_name='position')),
                ('display', models.BooleanField(default=True, help_text='\u5206\u7c7b\u662f\u5426\u663e\u793a True for display && False for not display', verbose_name='display')),
            ],
            options={
                'db_table': 'classifyinfo',
                'verbose_name': 'classifyinfo',
                'verbose_name_plural': 'classifyinfo',
            },
        ),
        migrations.CreateModel(
            name='CsySite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('display', models.BooleanField(default=True, help_text='\u7f51\u7ad9\u662f\u5426\u663e\u793a True for display && False for not', verbose_name='display')),
                ('classify', models.ForeignKey(blank=True, help_text='\u7f51\u7ad9\u5bfc\u822a\u5206\u7c7b', null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.ClassifyInfo', verbose_name='classify')),
            ],
            options={
                'db_table': 'csysite',
                'verbose_name': 'csysite',
                'verbose_name_plural': 'csysite',
            },
        ),
        migrations.CreateModel(
            name='DIY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('host', models.GenericIPAddressField(blank=True, help_text='\u6536\u85cf IP', null=True, verbose_name='host')),
                ('user', models.ForeignKey(blank=True, help_text='\u7528\u6237', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserInfo', verbose_name='user')),
            ],
            options={
                'verbose_name': 'diy',
                'verbose_name_plural': 'diy',
            },
        ),
        migrations.CreateModel(
            name='Evaluate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('host', models.GenericIPAddressField(blank=True, help_text='\u8bc4\u8bba IP', null=True, verbose_name='host')),
                ('content', models.TextField(blank=True, help_text='\u7528\u6237\u8bc4\u4ef7\u5185\u5bb9', null=True, verbose_name='content')),
                ('user', models.ForeignKey(blank=True, help_text='\u7528\u6237\uff0c blank=True\u4ee3\u8868\u964c\u751f\u4eba\u8bc4\u8bba', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserInfo', verbose_name='user')),
            ],
            options={
                'db_table': 'evaluate',
                'verbose_name': 'evaluate',
                'verbose_name_plural': 'evaluate',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('host', models.GenericIPAddressField(blank=True, help_text='\u6536\u85cf IP', null=True, verbose_name='host')),
                ('user', models.ForeignKey(blank=True, help_text='\u7528\u6237', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserInfo', verbose_name='user')),
            ],
            options={
                'db_table': 'favorite',
                'verbose_name': 'favorite',
                'verbose_name_plural': 'favorite',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('host', models.GenericIPAddressField(blank=True, help_text='\u8d5e/\u8e29IP', null=True, verbose_name='host')),
                ('flag', models.BooleanField(default=True, help_text='\u8d5e or \u8e29 True for like && False for unlike', verbose_name='flag')),
                ('user', models.ForeignKey(blank=True, help_text='\u7528\u6237\uff0c blank=True \u4ee3\u8868\u964c\u751f\u4eba\u8d5e/\u8e29', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserInfo', verbose_name='user')),
            ],
            options={
                'db_table': 'like',
                'verbose_name': 'like',
                'verbose_name_plural': 'like',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('host', models.GenericIPAddressField(blank=True, help_text=b'IP', null=True, verbose_name='host')),
                ('descr', models.TextField(blank=True, help_text='Log \u63cf\u8ff0', null=True, verbose_name='description')),
                ('user', models.ForeignKey(blank=True, help_text='\u7528\u6237', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserInfo', verbose_name='user')),
            ],
            options={
                'db_table': 'log',
                'verbose_name': 'log',
                'verbose_name_plural': 'log',
            },
        ),
        migrations.CreateModel(
            name='NavInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('name', models.CharField(help_text='\u5bfc\u822a\u540d\u79f0', max_length=255, verbose_name='name')),
                ('title', models.CharField(blank=True, help_text='\u5bfc\u822a\u6807\u9898', max_length=255, null=True, verbose_name='title')),
                ('image', models.ImageField(blank=True, help_text='\u5bfc\u822a\u56fe\u6807', null=True, upload_to=b'nav', verbose_name='image')),
                ('qiniu_image', models.CharField(default=b'', help_text='image', max_length=255, verbose_name='qiniu_image')),
                ('descr', models.TextField(blank=True, help_text='\u5bfc\u822a\u63cf\u8ff0', null=True, verbose_name='description')),
                ('position', models.IntegerField(blank=True, default=0, help_text='\u5bfc\u822a\u4f4d\u7f6e', null=True, verbose_name='position')),
                ('display', models.BooleanField(default=True, help_text='\u5bfc\u822a\u662f\u5426\u663e\u793a True for display && False for not display', verbose_name='display')),
                ('func', models.ForeignKey(blank=True, help_text=b'Function', null=True, on_delete=django.db.models.deletion.CASCADE, to='dh.FunctionInfo', verbose_name='function')),
            ],
            options={
                'db_table': 'navinfo',
                'verbose_name': 'navinfo',
                'verbose_name_plural': 'navinfo',
            },
        ),
        migrations.CreateModel(
            name='TagInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('tag', models.CharField(blank=True, help_text='\u7f51\u7ad9\u7f51\u5740', max_length=255, null=True, verbose_name='tag')),
            ],
            options={
                'db_table': 'taginfo',
                'verbose_name': 'taginfo',
                'verbose_name_plural': 'taginfo',
            },
        ),
        migrations.CreateModel(
            name='UserApiInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('status', models.BooleanField(default=True, help_text='API \u662f\u5426\u4e3a\u81ea\u5df1\u521b\u5efa True for create && False for follow', verbose_name='status')),
                ('api', models.ForeignKey(blank=True, help_text='API', null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.ApiInfo', verbose_name='api')),
                ('user', models.ForeignKey(blank=True, help_text='\u7528\u6237', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserInfo', verbose_name='user')),
            ],
            options={
                'db_table': 'userapiinfo',
                'verbose_name': 'userapiinfo',
                'verbose_name_plural': 'userapiinfo',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('host', models.GenericIPAddressField(blank=True, help_text='\u8bbf\u95ee IP', null=True, verbose_name='host')),
                ('user', models.ForeignKey(blank=True, help_text='\u7528\u6237', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserInfo', verbose_name='user')),
            ],
            options={
                'db_table': 'visit',
                'verbose_name': 'visit',
                'verbose_name_plural': 'visit',
            },
        ),
        migrations.CreateModel(
            name='WebSiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('url', models.CharField(blank=True, help_text='\u7f51\u7ad9\u7f51\u5740', max_length=255, null=True, verbose_name='url')),
                ('name', models.CharField(blank=True, help_text='\u7f51\u7ad9\u540d\u79f0', max_length=255, null=True, verbose_name='name')),
                ('logo', models.ImageField(blank=True, help_text='\u7f51\u7ad9 logo', null=True, upload_to=b'logo', verbose_name='image')),
                ('qiniu_logo', models.CharField(default=b'', help_text='logo', max_length=255, verbose_name='qiniu_logo')),
                ('slogan', models.TextField(blank=True, help_text='\u7f51\u7ad9\u4e00\u53e5\u8bdd\u4ecb\u7ecd', null=True, verbose_name='slogan')),
                ('descr', models.TextField(blank=True, help_text='\u7f51\u7ad9\u63cf\u8ff0', null=True, verbose_name='description')),
                ('tag', models.CharField(blank=True, help_text='\u7f51\u7ad9\u6807\u7b7e', max_length=255, null=True, verbose_name='tag')),
                ('srcode', models.CharField(blank=True, help_text='\u7f51\u7ad9\u6e90\u7801', max_length=255, null=True, verbose_name='srcode')),
                ('visit', models.IntegerField(default=0, help_text='\u7f51\u7ad9\u8bbf\u95ee\u6570', verbose_name='visit')),
                ('evaluate', models.IntegerField(default=0, help_text='\u7f51\u7ad9\u8bc4\u4ef7\u6570', verbose_name='evaluate')),
                ('like', models.IntegerField(default=0, help_text='\u7f51\u7ad9\u70b9\u8d5e\u6570', verbose_name='like')),
                ('unlike', models.IntegerField(default=0, help_text='\u7f51\u7ad9\u88ab\u8e29\u6570', verbose_name='unlike')),
                ('fav', models.IntegerField(default=0, help_text='\u7f51\u7ad9\u6536\u85cf\u6570', verbose_name='fav')),
                ('display', models.BooleanField(default=True, help_text='\u7f51\u7ad9\u662f\u5426\u663e\u793a True for display && False for not display', verbose_name='display')),
            ],
            options={
                'db_table': 'websiteinfo',
                'verbose_name': 'websiteinfo',
                'verbose_name_plural': 'websiteinfo',
            },
        ),
        migrations.CreateModel(
            name='WebsiteRelatedInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('name', models.CharField(blank=True, help_text='\u7f51\u7ad9\u76f8\u5173\u4fe1\u606f\u540d\u79f0', max_length=255, null=True, verbose_name='name')),
                ('url', models.CharField(blank=True, help_text='\u7f51\u7ad9\u76f8\u5173\u4fe1\u606f\u7f51\u5740', max_length=255, null=True, verbose_name='url')),
                ('descr', models.TextField(blank=True, help_text='\u7f51\u7ad9\u76f8\u5173\u4fe1\u606f\u63cf\u8ff0', null=True, verbose_name='description')),
                ('srcode', models.CharField(blank=True, help_text='\u7f51\u7ad9\u76f8\u5173\u4fe1\u606f\u6e90\u7801', max_length=255, null=True, verbose_name='srcode')),
                ('display', models.BooleanField(default=True, help_text='\u7f51\u7ad9\u76f8\u5173\u4fe1\u606f\u662f\u5426\u663e\u793a True for display && False for not display', verbose_name='display')),
                ('website', models.ForeignKey(blank=True, help_text='\u7f51\u7ad9', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_website', to='resources.WebSiteInfo', verbose_name='website')),
            ],
            options={
                'db_table': 'websiterelatedinfo',
                'verbose_name': 'websiterelatedinfo',
                'verbose_name_plural': 'websiterelatedinfo',
            },
        ),
        migrations.CreateModel(
            name='WebSiteSubmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createtime')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='modifytime')),
                ('url', models.CharField(blank=True, help_text='\u7f51\u7ad9\u7f51\u5740', max_length=255, null=True, verbose_name='url')),
                ('tag', models.CharField(blank=True, help_text='\u7f51\u7ad9\u6807\u7b7e', max_length=255, null=True, verbose_name='tag')),
                ('deal', models.BooleanField(default=False, help_text='\u7f51\u7ad9\u63d0\u4ea4\u662f\u5426\u5df2\u5904\u7406 True for deal && False for not', verbose_name='deal')),
            ],
            options={
                'db_table': 'websitesubmit',
                'verbose_name': 'websitesubmit',
                'verbose_name_plural': 'websitesubmit',
            },
        ),
        migrations.AddField(
            model_name='visit',
            name='website',
            field=models.ForeignKey(blank=True, help_text='\u7f51\u7ad9', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visit_website', to='resources.WebSiteInfo', verbose_name='website'),
        ),
        migrations.AddField(
            model_name='taginfo',
            name='website',
            field=models.ForeignKey(blank=True, help_text='\u7f51\u7ad9', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taginfo_website', to='resources.WebSiteInfo', verbose_name='website'),
        ),
        migrations.AddField(
            model_name='log',
            name='website',
            field=models.ForeignKey(blank=True, help_text='\u7f51\u7ad9', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='log_website', to='resources.WebSiteInfo', verbose_name='website'),
        ),
        migrations.AddField(
            model_name='like',
            name='website',
            field=models.ForeignKey(blank=True, help_text='\u7f51\u7ad9', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_website', to='resources.WebSiteInfo', verbose_name='website'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='website',
            field=models.ForeignKey(blank=True, help_text='\u7f51\u7ad9', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_website', to='resources.WebSiteInfo', verbose_name='website'),
        ),
        migrations.AddField(
            model_name='evaluate',
            name='website',
            field=models.ForeignKey(blank=True, help_text='\u7f51\u7ad9', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluate_website', to='resources.WebSiteInfo', verbose_name='website'),
        ),
        migrations.AddField(
            model_name='diy',
            name='website',
            field=models.ForeignKey(blank=True, help_text='\u7f51\u7ad9', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diy_website', to='resources.WebSiteInfo', verbose_name='website'),
        ),
        migrations.AddField(
            model_name='csysite',
            name='website',
            field=models.ForeignKey(blank=True, help_text='\u7f51\u7ad9', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='csysite_website', to='resources.WebSiteInfo', verbose_name='website'),
        ),
        migrations.AddField(
            model_name='classifyinfo',
            name='nav',
            field=models.ForeignKey(blank=True, help_text='\u5206\u7c7b\u6240\u5c5e\u5bfc\u822a', null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.NavInfo', verbose_name='nav'),
        ),
    ]
