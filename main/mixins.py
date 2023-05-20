from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel

User = get_user_model()


class BaseModel(TimeStampedModel):
    class Meta:
        abstract = True
