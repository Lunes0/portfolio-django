import factory
from django.contrib.auth.models import User
from core.models import Post

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("safe_email")

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=4)
    slug = factory.Faker("slug")
    author = factory.SubFactory(UserFactory)
    content = factory.Faker("paragraph", nb_sentences=5)
    status = 1