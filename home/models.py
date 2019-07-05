from django.db import models

# Create your models here.

class Student(models.Model):
    student_name=models.CharField('Student Name',max_length=30,unique=True)
    dept=(
        ('CSE','Computer Science'),
        ('MH','Mech'),
        ('CV','Civil')
    )
    #photo=models.ImageField(upload_to='media/',null=True)
    department=models.CharField('Department',choices=dept,blank=True,null=True,max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True,editable=False,blank=False)

class Book(models.Model):
    book=models.CharField('Book',max_length=30,null=True)
    def __str__(self):
        return self.book

class Section(models.Model):
    section=models.CharField('Section',max_length=30,null=False)
    advisor=models.OneToOneField('Teacher',on_delete=models.SET_NULL,null=True)
    students=models.ManyToManyField('Student',null=False)
    def __str__(self):
        return self.section

class Teacher(models.Model):
    teacher=models.CharField('Teacher Name',max_length=30,null=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.teacher 

class Library(models.Model):
    library_name=models.CharField('Library',null=True,max_length=100)
    books=models.ManyToManyField('Book',null=False)
    def __str__(self):
        return self.library_name

