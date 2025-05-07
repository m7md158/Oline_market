from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Item

class ItemTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(
            name='Test Category'
        )
        self.item = Item.objects.create(
            category=self.category,
            name='Test Item',
            description='Test Description',
            price=99.99,
            created_by=self.user,
            image='items/test.jpg'
        )

    def test_items_page(self):
        response = self.client.get(reverse('item:items'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item/items.html')

    def test_item_detail_page(self):
        response = self.client.get(reverse('item:detail', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item/detail.html')

    def test_new_item_page_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('item:new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item/form.html')

    def test_new_item_page_unauthenticated(self):
        response = self.client.get(reverse('item:new'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_create_item(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('item:new'), {
            'category': self.category.id,
            'name': 'New Test Item',
            'description': 'New Test Description',
            'price': 149.99,
            'image': 'items/test.jpg'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Item.objects.filter(name='New Test Item').exists())

    def test_delete_item(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('item:delete', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(Item.objects.filter(pk=self.item.pk).exists())

    def test_edit_item(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('item:edit', kwargs={'pk': self.item.pk}), {
            'category': self.category.id,
            'name': 'Updated Test Item',
            'description': 'Updated Test Description',
            'price': 199.99,
            'image': 'items/test.jpg'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful edit
        updated_item = Item.objects.get(pk=self.item.pk)
        self.assertEqual(updated_item.name, 'Updated Test Item')
