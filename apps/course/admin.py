from django.contrib import admin

from apps.common.models import Author
from .models import Category, SocialMedia, Course, CourseComment, Section, Lecture, LectureViewed, LectureComment, \
    Certificate, CourseUser

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(SocialMedia)
admin.site.register(Course)
admin.site.register(CourseUser)
admin.site.register(CourseComment)
admin.site.register(Section)
admin.site.register(Lecture)
admin.site.register(LectureViewed)
admin.site.register(LectureComment)
admin.site.register(Certificate)
