
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Drop collections directly using PyMongo
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db['octofit_tracker_user'].drop()
        db['octofit_tracker_team'].drop()
        db['octofit_tracker_activity'].drop()
        db['octofit_tracker_workout'].drop()
        db['octofit_tracker_leaderboard'].drop()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Running', duration=25, date=timezone.now().date())
        Activity.objects.create(user=users[4], activity_type='Cycling', duration=35, date=timezone.now().date())
        Activity.objects.create(user=users[5], activity_type='Swimming', duration=50, date=timezone.now().date())

        # Create Workouts
        workout1 = Workout.objects.create(name='Pushups', description='Upper body workout')
        workout2 = Workout.objects.create(name='Squats', description='Lower body workout')
        workout1.suggested_for.set([users[0], users[3]])
        workout2.suggested_for.set([users[1], users[4]])

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, score=300)
        Leaderboard.objects.create(team=dc, score=250)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
