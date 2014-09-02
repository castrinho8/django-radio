import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from radio.apps.programmes.models import Programme, Role
from radio.apps.users.models import UserProfile


class UserProfileMethodTests(TestCase):

    def test_save(self):
        user_profile = UserProfile(user=User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword'), bio='my bio')
        user_profile.save()
        self.assertEqual(user_profile, UserProfile.objects.get(id=user_profile.id))

    def test_get_announcers_and_profile(self):
        user = User(username='user1', password='a')
        user.save()
        user_profile = UserProfile(user=user, bio='my bio')
        user_profile.save()
        programme = Programme.objects.create(name="Test programme", synopsis="This is a description", current_season=1, _runtime=60, start_date=datetime.date(2014, 1, 31))
        role = Role.objects.create(person=user, programme=programme)
        self.assertEqual(programme, Programme.objects.get(id=programme.id))
        self.assertEqual(user_profile, UserProfile.objects.get(id=user_profile.id))
        self.assertEqual(user, user_profile.user)
        self.assertEqual(user, programme.announcers.all()[0])
