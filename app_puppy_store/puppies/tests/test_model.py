from django.test import TestCase
from puppies.models import PuppyModel

class PuppyTest(TestCase):
    """" Test module for Puppy Model"""

    def setUp(self):
        PuppyModel.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black'
        )
        PuppyModel.objects.create(
            name='Muffin', age=4, breed='Labrador', color='Brown'
        )
    
    def test_puppy_breed(self):
        puppy_casper = PuppyModel.objects.get(name='Casper')
        puppy_muffin = PuppyModel.objects.get(name='Muffin')

        self.assertEqual(
            puppy_casper.get_breed(), 'Casper belongs to Bull Dog breed.'
        )

        self.assertEqual(
            puppy_muffin.get_breed(), 'Muffin belongs to Labrador breed.'
        )