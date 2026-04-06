from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Create Teams
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Create Users
        users = [
            User.objects.create_user(username='superman', email='superman@dc.com', team=dc),
            User.objects.create_user(username='batman', email='batman@dc.com', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', team=dc),
            User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', team=marvel),
            User.objects.create_user(username='captainamerica', email='captainamerica@marvel.com', team=marvel),
        ]

        # Create Activities
        activities = [
            octo_models.Activity.objects.create(user=users[0], type='flight', duration=60),
            octo_models.Activity.objects.create(user=users[1], type='martial arts', duration=45),
            octo_models.Activity.objects.create(user=users[3], type='tech', duration=30),
        ]

        # Create Workouts
        workouts = [
            octo_models.Workout.objects.create(name='Super Strength', description='Strength training for heroes'),
            octo_models.Workout.objects.create(name='Agility', description='Agility drills for quick response'),
        ]

        # Create Leaderboard
        octo_models.Leaderboard.objects.create(team=marvel, points=300)
        octo_models.Leaderboard.objects.create(team=dc, points=250)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
