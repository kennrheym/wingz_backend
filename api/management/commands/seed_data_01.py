#RUN THIS:
#python manage.py seed_data_01 --users 10 --rides 20 --events 50


from django.core.management.base import BaseCommand
# from django.utils import timezone
from datetime import timezone

from faker import Faker
import random

from api.models import User, Ride, RideEvent
from api.enums import UserRole, RideStatus

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with test users, rides, and ride events'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=10)
        parser.add_argument('--rides', type=int, default=20)
        parser.add_argument('--ride_events', type=int, default=50)

    def handle(self, *args, **options):
        self.stdout.write("Deleting existing data...")
        RideEvent.objects.all().delete()
        Ride.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write("Creating users...")
        users = []
        roles = [UserRole.ADMIN, UserRole.DRIVER, UserRole.RIDER]

        for _ in range(options['users']):
            role = random.choice(roles)
            user = User.objects.create_user(
                username=fake.unique.user_name(),
                email=fake.unique.email(),
                phone_number=fake.unique.msisdn(),
                password='password123',
                role=role
            )
            users.append(user)

        # Separate users by role
        riders = [u for u in users if u.role == UserRole.RIDER]
        drivers = [u for u in users if u.role == UserRole.DRIVER]

        if not riders or not drivers:
            self.stdout.write(self.style.ERROR("Seeding requires at least one Rider and one Driver."))
            return

        self.stdout.write("Creating rides...")
        ride_statuses = [RideStatus.EN_ROUTE, RideStatus.PICKED_UP, RideStatus.DROPPED_OFF]
        rides = []

        for _ in range(options['rides']):
            ride = Ride.objects.create(
                id_rider=random.choice(riders),
                id_driver=random.choice(drivers),
                status=random.choice(ride_statuses),
                pickup_latitude=fake.latitude(),
                pickup_longitude=fake.longitude(),
                dropoff_latitude=fake.latitude(),
                dropoff_longitude=fake.longitude(),
                pickup_time=fake.date_time_this_year(before_now=True, after_now=False, tzinfo=timezone.utc)
            )
            rides.append(ride)

        self.stdout.write("Creating ride events...")
        for _ in range(options['ride_events']):
            RideEvent.objects.create(
                id_ride=random.choice(rides),
                description=fake.text(max_nb_chars=120)
            )

        self.stdout.write(self.style.SUCCESS("✅ Database seeding complete!"))
