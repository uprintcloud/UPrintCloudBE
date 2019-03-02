# Generated by Django 2.1.7 on 2019-03-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='file_path',
            new_name='file',
        ),
        migrations.AlterField(
            model_name='jobs',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='已经打印'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='finished_date',
            field=models.DateField(null=True, verbose_name='打印日期'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='finished_locate',
            field=models.CharField(max_length=128, null=True, verbose_name='打印地点'),
        ),
    ]