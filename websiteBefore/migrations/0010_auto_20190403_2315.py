# Generated by Django 2.1.5 on 2019-04-03 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteBefore', '0009_teachermessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermessage',
            name='teacherContent',
            field=models.CharField(max_length=400, verbose_name='老师介绍'),
        ),
        migrations.AlterField(
            model_name='teachermessage',
            name='teacherImage',
            field=models.ImageField(upload_to='', verbose_name='老师图片'),
        ),
        migrations.AlterField(
            model_name='teachermessage',
            name='teacherLabel',
            field=models.CharField(max_length=20, verbose_name='老师标签'),
        ),
        migrations.AlterField(
            model_name='teachermessage',
            name='teacherName',
            field=models.CharField(max_length=20, verbose_name='老师名称'),
        ),
        migrations.AlterField(
            model_name='teachermessage',
            name='teacherTitle',
            field=models.CharField(max_length=20, verbose_name='老师荣誉'),
        ),
    ]