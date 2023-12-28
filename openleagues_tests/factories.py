import factory
from faker import Factory as FakerFactory
from api.settings.base import AUTH_USER_MODEL

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
