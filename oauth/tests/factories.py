import factory
import factory.fuzzy
from django.utils.timezone import now, timedelta
from oauth2_provider.models import AccessToken, Application


class ApplicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Application

    user = factory.SubFactory("user.tests.factories.UserFactory", is_superuser=True)
    name = factory.fuzzy.FuzzyText(length=20)
    authorization_grant_type = Application.GRANT_PASSWORD
    client_id = factory.fuzzy.FuzzyText(length=20)
    client_secret = factory.fuzzy.FuzzyText(length=20)


class AccessTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AccessToken

    user = factory.SubFactory("user.tests.factories.UserFactory")
    application = factory.SubFactory(ApplicationFactory)
    token = factory.fuzzy.FuzzyText(length=42)
    scope = ""
    expires = now() + timedelta(days=1)
