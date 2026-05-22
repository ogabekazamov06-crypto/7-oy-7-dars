from datetime import datetime
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db.models import TextField
from django.forms import Textarea

from .models import Student, Course, CourseLike, Comment

admin.site.site_header = "FN40"
admin.site.site_title = "fn40"
admin.site.logout_template = "admin/logout.html"


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ['user']

    formfield_overrides = {
        TextField: {
            "widget": Textarea(attrs={
                "rows": 2,
                "cols": 40,
            })
        },
    }


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_year', 'price', 'image')
    list_display_links = ('title',)
    list_filter = ('published_year',)
    search_fields = ('title', 'published_year',)

    readonly_fields = ['published_year','time', 'time_check']

    fieldsets = [
        (
            "Asosiy",
            {
                'fields': ['title', 'description','price']
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
                'fields': ['published_year','time', 'time_check']
            }
        )
    ]

    inlines = [
        CommentInline
    ]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:

            if isinstance(instance, Comment) and not instance.user:
                instance.user = request.user
            instance.save()
        formset.save_m2m()

    def get_image(self, course):
        if course.poster:
            return mark_safe(f'<img src="{course.poster.url}" width="50px" >')
        else:
            return '-'

    def get_video(self, course):
        if course.video:
            return mark_safe(f'<video src="{course.video.url}" width="50px" >')
        else:
            return '-'

    get_image.short_description = 'Rasm'
    get_video.short_description = 'Video'

    @admin.display(boolean=True, description='Tekin')
    def my_test_function(self, obj):
        if obj.published_year >= 2025:
            return False
        return True

    @admin.display(description="Vaqt boldi")
    def time_check(self, obj):
        return  f"{2026 - obj.published_year} yil boldi!!!"


    @admin.display(description='Necha yil bolgani')
    def time(self, obj):
        return datetime.now().year - obj.published_year


admin.site.register(Course, CourseAdmin)
admin.site.register(Student)
admin.site.register(CourseLike)
admin.site.register(Comment)