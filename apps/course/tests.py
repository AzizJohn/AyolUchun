
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from apps.course.models import Category

#
# class CategoryListTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.url = 'http://127.0.0.1:8000/course/category/list/'

    # def test_get_categories(self):
    #     response = self.client.get(self.url)
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 0)  # initially there are no categories
    #
    # def test_create_category(self):
    #     data = {'name': 'Test Category'}
    #     response = self.client.post(self.url, data)
    #
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.data['name'], 'Test Category')
    #
    #     # check that the category was actually created in the database
    #     self.assertEqual(Category.objects.count(), 1)
    #     category = Category.objects.first()
    #     self.assertEqual(category.name, 'Test Category')
