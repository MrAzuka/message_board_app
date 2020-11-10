from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='Just a guy')
        Post.objects.create(text='Hey boo')

    def test_text(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'Just a guy')

    def test_text2(self):
        post1 = Post.objects.get(id=2)
        expected_object_name1 = f'{post1.text}'
        self.assertEqual(expected_object_name1, 'Hey boo')

class HomePageView(TestCase):
    def setUp(self):
        Post.objects.create(text='Oliseh is just a good guy')

    def test_url_exist_in_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_view_use_correct_template(self):
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'home.html')