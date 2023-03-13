from tkinter import Image

from PIL.ImageDraw import ImageDraw
from PIL.ImageFont import ImageFont
from django.db.models import Count, Q
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, ListAPIView

from apps.common.choices import PAYMENT_STATUS_CHOICES
from .models import *
from .permissions import IsAdminOrCreateOnly
from .serializers import CategorySerializer, SocialMediaSerializer, CourseSerializer, CourseCommentSerializer, \
    SectionSerializer, LectureSerializer, LectureCommentSerializer, CertificateSerializer


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


    def isUserPurchased(self, request):
        return CourseUser.objects.all().filter(payment_status=PAYMENT_STATUS_CHOICES[0][0]).filter(
            course_id=request.data['course_id'], payer_user_id=request.data['user_id'])

    def getFourEnrolledUsers(self, request):
        return CourseUser.objects.all().filter(payment_status=PAYMENT_STATUS_CHOICES[0][0]).filter(
            course_id=request.data['course_id'])[:4]


class CourseCommentList(ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = CourseComment.objects.all()
    serializer_class = CourseCommentSerializer


class CourseCommentDetailAPIView(RetrieveAPIView):
    queryset = CourseComment.objects.all()
    serializer_class = CourseCommentSerializer

    def getRating(self):
        return CourseComment.objects.all().aggregate(models.Avg('ranking'))['ranking__avg']


class SectionList(ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class SectionDetailAPIView(RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def getSectionStatus(self, section_id, course_id, user_id):
        lecture_number = Lecture.objects.filter(section_id=section_id).count()

        if Lecture.objects.filter(section_id=section_id, is_paid=True).exists():
            if Course.objects.filter(id=course_id, users__id=user_id).exists():
                result = Lecture.objects.filter(section_id=section_id).annotate(
                    lecture_views=Count('LectureViewed', filter=Q(LectureViewed__user_id=user_id))
                ).aggregate(lecture_views_total=Count('id'))['lecture_views_total']
                if result == 0:
                    return 'Ko\'rilmagan'
                elif result < lecture_number:
                    return 'jarayonda'
                else:
                    return 'ko\'rilgan'
            else:
                return 'Sotib olinmagan'
        else:
            result = Lecture.objects.filter(section_id=section_id).annotate(
                lecture_views=Count('LectureViewed', filter=Q(LectureViewed__user_id=user_id))
            ).aggregate(lecture_views_total=Count('id'))['lecture_views_total']
            if result == 0:
                return 'Ko\'rilmagan'
            elif result < lecture_number:
                return 'jarayonda'
            else:
                return 'ko\'rilgan'


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
    serializer_class = LectureViewed


class LectureViewedDetailAPIView(RetrieveAPIView):
    queryset = LectureViewed.objects.all()
    serializer_class = LectureViewed

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

    def generate_certificate(self):
        '''Function to save certificates as a .png file'''

        FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
        FONT_COLOR = "#FFFFFF"

        template = Image.open(r'template.png')
        WIDTH, HEIGHT = template.size

        image_source = Image.open(r'template.png')
        draw = ImageDraw.Draw(image_source)

        # Finding the width and height of the text.
        name_width, name_height = draw.textsize(self.user_id.first_name, font=FONT_FILE)

        # Placing it in the center, then making some adjustments.
        draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30),
                  f"{self.user_id.first_name} {self.user_id.last_name}", fill=FONT_COLOR,
                  font=FONT_FILE)

        # Saving the certificates in a different directory.
        image_source.save("../static/certificates/" + self.user_id.id + ".png")

        self.certificate_photo = "../static/certificates/" + self.user_id.id + ".png"
        Certificate.save(self, user_id=self.user_id, course_id=self.course_id, certificate_photo=self.certificate_photo)

        class Meta:
            verbose_name = "Certificate"
            verbose_name_plural = "Certificates"

    # sertificatni papkalarini to'grilab qo'yamiz

    # viewga ko'chiramiz alohida API bo'ladi


# class getGeneratedCertificate(ListAPIView):
#     queryset = Certificate.objects.all()
#     serializer_class = CertificateSerializer
#
#     def getCertificate(self, course_id, user_id):
#         certificate = Certificate(user_id, course_id)
#         certificate.generate_certificate()
#         certificate.save()
#         return certificate

# class getGeneratedCertificate(RetrieveAPIView):
#     def get_generated_certificate(request, course_id, user_id):
#         certificate = get_object_or_404(Certificate, course_id=course_id, user_id=user_id)
#         if certificate is None:
#             return Response({'detail': 'Sertifikat yo\'q'})
#         else:
#             serializer = CertificateSerializer(certificate)
#             return Response(serializer.data)

# class getGeneratedCertificate(APIView):
#     def get(self, request, pk, format=None):
#         print(request)
#     # snippet = self.get_object(pk)
#     # serializer = SnippetSerializer(snippet)
#     # return Response(serializer.data)
#
#     # queryset = Certificate.objects.all().filter(user_id=user_id).filter(course_id=course_id)

@api_view(['GET'])
def getGeneratedCertificate(request, course_id, user_id):
    certificate = Certificate.objects.filter(course_id=course_id, user_id=user_id).first()
    if not certificate:
        return Response({'detail': 'Sertifikat yo\'q'})
    else:
        serializer = CertificateSerializer(certificate)
        return Response(serializer.data)
