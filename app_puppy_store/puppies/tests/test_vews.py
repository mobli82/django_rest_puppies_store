import json
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from puppies.models import PuppyModel
from puppies.serializers import PuppySerializer

class GetAllPuppiesTestView(TestCase):
    def setUp(self):
        PuppyModel.objects.create(
            name='Pinki', age=3, breed='Spanier', color='White'
        )
        PuppyModel.objects.create(
            name='Winki', age=4, breed='wolf', color='black'
        )
        PuppyModel.objects.create(
            name='Rambo', age=3, breed='Labrador', color='Braown'
        )
        PuppyModel.objects.create(
            name='Rocky', age=3, breed='Grande', color='Blue'
        )
    
    def test_get_all_puppies(self):
        resp = self.client.get(reverse('get-post-puppies'))

        puppies = PuppyModel.objects.all()

        serializer_puppies = PuppySerializer(puppies, many=True)

        self.assertEqual(resp.status_code,status.HTTP_200_OK)
        self.assertEqual(resp.data, serializer_puppies.data)

class GetSinglePuppyTest(TestCase):
    def setUp(self):
        self.casper = PuppyModel.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        self.muffin = PuppyModel.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')
        self.rambo = PuppyModel.objects.create(
            name='Rambo', age=2, breed='Labrador', color='Black')
        self.ricky = PuppyModel.objects.create(
            name='Ricky', age=6, breed='Labrador', color='Brown')
    
    def test_get_valid_single_puppy(self,):
        resp = self.client.get(reverse('get-delete-update-puppy', kwargs={'pk': self.rambo.pk}))

        puppy = PuppyModel.objects.get(pk=self.rambo.pk)

        serializer_ppuppy = PuppySerializer(puppy)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, serializer_ppuppy.data)
    
    def test_get_invalid_single_puppy(self,):
        resp = self.client.get(reverse('get-delete-update-puppy', kwargs={'pk': 300}))
        
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewPuppyTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'Muffin',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

        self.invalid_data = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }
    
    def test_create_valid_data(self):

        req = self.client.post(reverse('get-post-puppies'),
                                        data=json.dumps(self.valid_data),
                                        content_type='application/json')

        self.assertEqual(req.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_data(self):

        req = self.client.post(reverse('get-post-puppies'),
                                        data=json.dumps(self.invalid_data),
                                        content_type='application/json')
        self.assertEqual(req.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSinglePuppyTest(TestCase):
    def setUp(self):
        self.casper = PuppyModel.objects.create(
            name='Casper', age=5, breed='York', color='brown'
        )
        self.muffin = PuppyModel.objects.create(
            name='Muffin', age=2, breed='Gradane', color='black'
        )

        self.valid_data = {
            'name': 'Casper-updated',
            'age': 5,
            'breed': 'Pamerion',
            'color': 'White'
        }
        self.invalid_data = {
            'name': '',
            'age': 5,
            'breed': 'Pamerion',
            'color': 'White'
        }
    
    def test_valid_update_puppy(self):
        resp = self.client.put(reverse('get-delete-update-puppy', kwargs={'pk': self.casper.pk}),
                                        data=json.dumps(self.valid_data),
                                        content_type='application/json'
        )

        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_puppy(self):
        resp = self.client.put(reverse('get-delete-update-puppy', kwargs={'pk': self.casper.pk}),
                                        data=json.dumps(self.invalid_data),
                                        content_type='application/json'
        )

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSinglePuppyTest(TestCase):
    def setUp(self):
        self.casper = PuppyModel.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        self.muffin = PuppyModel.objects.create(
            name='Muffy', age=1, breed='Gradane', color='Brown')

    def test_delete_valid_puppy(self):
        resp = self.client.delete(reverse('get-delete-update-puppy', kwargs={'pk': self.casper.pk}))

        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_delete_invalid_puppy(self):
        resp = self.client.delete(reverse('get-delete-update-puppy', kwargs={'pk': 8888}))

        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)