from django.contrib import  admin
from .models import Student, Course, CourseLike,Comment

admin.site.site_header = "FN40"
admin.site.site_title = "fn40"
admin.site.logout_template = "admin/logout.html"


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = 'user'

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_year','price','image')
    list_display_links = ('title',)
    list_filter = ('published_year',)
    search_fields = ('title', 'published_year',)
    list_editable = ('published_year',)
    # fields = (
    #     ('title', 'description'),
    #     ('image',),
    #     ('published_year',),
    #
    # )
    fieldsets = [
        (
            "Asosiy",
            {
                'fields': ['title', 'description']
            }
        ),
        (
            "Media",
            {
                'fields': ['image']
            }
        ),
        (
            "Taqdim etilgan yili",
            {
                'fields': ['published_year']
            }
        )
    ]
    inlines = [
        CommentInline
    ]


admin.site.register(Course, CourseAdmin)

admin.site.register(Student)
admin.site.register(CourseLike)
