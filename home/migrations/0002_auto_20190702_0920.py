# Generated by Django 2.2.2 on 2019-07-02 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=30, null=True, verbose_name='Book')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=30, verbose_name='Teacher Name')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='library',
            name='sut',
        ),
        migrations.AddField(
            model_name='library',
            name='library_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Library'),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=30, verbose_name='Section')),
                ('advisor', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Teacher')),
                ('students', models.ManyToManyField(to='home.Student')),
            ],
        ),
        migrations.AddField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(to='home.Book'),
        ),
    ]