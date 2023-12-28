import factory
from faker import Factory as FakerFactory
from api.settings.base import AUTH_USER_MODEL
from openleagues.leagues_event.models import Location, LeaguesEvent

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AUTH_USER_MODEL

    first_name = factory.LazyAttribute(lambda x:faker.first_name())
    last_name = factory.LazyAttribute(lambda x:faker.last_name())
    username = factory.LazyAttribute(lambda x:faker.first_name())
    email = factory.LazyAttribute(lambda x:f"test@example.com")
    password = factory.LazyAttribute(lambda x:faker.password())
    is_active= True
    is_staff = False
    

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)
        
class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    state = "CO"
    county = "Boulder"
    zipcode = "80303"

class LeaguesEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LeaguesEvent

    title = faker.company()
    location = factory.SubFactory(LocationFactory)
    start_week = faker.date_this_decade()
    end_week = faker.date_this_decade()
    format = faker.random_element(elements=['singles', 'doubles', 'mixed'])
    team_type = faker.random_element(elements=['team', 'individual'])
    description = faker.text()
    gender = faker.random_element(elements=['M', 'F', 'All'])
    minimum_level = faker.random_element(elements=['1.0', '3.0','4.5'])
    spots = faker.random_digit()
    status = faker.random_element(elements=["open","inprogress","completed","cancelled"])
