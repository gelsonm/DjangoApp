from django.contrib import admin

# Register your models here.

from home.models import Student,Teacher,Library,Book,Section
'''
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Section)
'''

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields=('student_name','id')
    list_filter=('student_name','department','timestamp')
    fields=('student_name','department')
    #pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass