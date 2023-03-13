from django.urls import path

from .views import CategoryList, LectureList, CategoryDetailAPIView, LectureDetailAPIView, SocialMediaList, \
    SocialMediaDetailAPIView, CourseList, CourseDetailAPIView, CourseCommentList, CourseCommentDetailAPIView, \
    SectionList, SectionDetailAPIView, LectureViewedList, LectureViewedDetailAPIView, LectureCommentList, \
    LectureCommentDetailAPIView, CertificateList, CertificateDetailAPIView, getGeneratedCertificate


class CertificateGeneratedList:
    pass


urlpatterns = [
    # Category urls
    path('category/list/', CategoryList.as_view(), name='Category-list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='Category-detail'),
    # Lecture urls
    path('lecture/list/', LectureList.as_view(), name='Lecture-list'),
    path('lecture/<int:pk>/', LectureDetailAPIView.as_view(), name='Lecture-detail'),
    # SocialMedia urls
    path('socialmedia/list/', SocialMediaList.as_view(), name='SocialMedia-list'),
    path('socialmedia/<int:pk>/', SocialMediaDetailAPIView.as_view(), name='SocialMedia-detail'),
    # Course urls
    path('course/list/', CourseList.as_view(), name='Course-list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='Course-detail'),
    path('course/<int:course_id>/<int:user_id>/', CourseDetailAPIView.as_view(), name='Course-detail'),
    # CourseComment urls
    path('coursecomment/list/', CourseCommentList.as_view(), name='CourseComment-list'),
    path('coursecomment/<int:pk>/', CourseCommentDetailAPIView.as_view(), name='CourseComment-detail'),
    # Section urls
    path('section/list/', SectionList.as_view(), name='Section-list'),
    path('section/<int:pk>/', SectionDetailAPIView.as_view(), name='Section-detail'),
    # Lecture Viewed urls
    path('lectureviewed/list/', LectureViewedList.as_view(), name='LectureViewed-list'),
    path('lectureviewed/<int:pk>/', LectureViewedDetailAPIView.as_view(), name='LectureViewed-detail'),
    # Lecture Comment urls
    path('lecturecomment/list/', LectureCommentList.as_view(), name='LectureComment-list'),
    path('lecturecomment/<int:pk>/', LectureCommentDetailAPIView.as_view(), name='LectureComment-detail'),
    # Certificate urls
    path('certificate/list/', CertificateList.as_view(), name='Certificate-list'),
    path('certificate/<int:pk>/', CertificateDetailAPIView.as_view(), name='Certificate-detail'),
    
    path('certificate/<int:course_id>/<int:user_id>/', getGeneratedCertificate, name='getGeneratedCertificate'),
]
