from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response

from .certificate_generator import certificate_generate
from .models import *
from .permissions import IsAdminOrCreateOnly
from .serializers import CategorySerializer, SocialMediaSerializer, CourseSerializer, CourseCommentSerializer, \
    SectionSerializer, LectureSerializer, LectureCommentSerializer, CertificateSerializer, LectureViewedSerializer


class CategoryList(ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SocialMediaList(ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class SocialMediaDetailAPIView(RetrieveAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class CourseList(ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseCommentList(ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = CourseComment.objects.all()
    serializer_class = CourseCommentSerializer


class CourseCommentDetailAPIView(RetrieveAPIView):
    queryset = CourseComment.objects.all()
    serializer_class = CourseCommentSerializer


class SectionList(ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class SectionDetailAPIView(RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class LectureList(ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class LectureDetailAPIView(RetrieveAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class LectureViewedList(ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = LectureViewed.objects.all()
    serializer_class = LectureViewedSerializer


class LectureViewedDetailAPIView(RetrieveAPIView):
    queryset = LectureViewed.objects.all()
    serializer_class = LectureViewedSerializer

    def setLectureViewed(self):
        lecture = Lecture.objects.get(id=Lecture.id)
        user = User.objects.get(id=User.id)
        lecture_viewed = LectureViewed.objects.create(lecture_id=lecture, user_id=user)


class LectureCommentList(ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = LectureComment.objects.all()
    serializer_class = LectureCommentSerializer


class LectureCommentDetailAPIView(RetrieveAPIView):
    queryset = LectureComment.objects.all()
    serializer_class = LectureCommentSerializer


class CertificateList(ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertificateDetailAPIView(RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


# @api_view(['POST'])
# def postGenerate_certificate(request):
#     course = Course.objects.get(id=request.data['course'])
#     user = User.objects.get(id=request.data['user'])
#
#     file = certificate_generate('user', course)
#     certificate = Certificate.objects.create(course=course, user=user.first_name, certificate_photo=file)
#
#     serizalizer = CertificateSerializer(certificate).data
#     return Response(serizalizer)

class CreateCertificate(CreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def create(self, request, *args, **kwargs):
        course = Course.objects.get(id=request.data['course'])
        user = User.objects.get(id=request.data['user'])
        print(course, user.first_name, user.last_name)
        file = certificate_generate(user, course)
        certificate = Certificate.objects.create(course=course, user=user, certificate_photo=file)
        #
        serializer = CertificateSerializer(certificate).data
        return Response(serializer)
