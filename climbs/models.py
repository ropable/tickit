# Django imports
from django.db import models
from django.utils.translation import ugettext as _
# Third-party app imports
from model_utils.models import TimeStampedModel
from model_utils import Choices


CLIMB_TYPE = Choices(
    (0, 'toprope', _('Top rope')),
    (1, 'lead', _('Lead')),
    (2, 'boulder', _('Boulder')),
)

class Business(TimeStampedModel):
    """Businesses own Walls and Climbs.
    Define a standard difficulty to use for climbing and bouldering routes.
    """
    name = models.CharField(max_length=1024)
    current = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'businesses'


class Wall(TimeStampedModel):
    """Walls belong to a business, and can be used to organise climbs.
    """
    name = models.CharField(max_length=256)
    current = models.BooleanField(default=True)
    business = models.ForeignKey(Business)
    climb_type =  models.IntegerField(
        choices=CLIMB_TYPE, default=CLIMB_TYPE.toprope, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)  # Arbitrary ordering.


class Climb(TimeStampedModel):
    """Can be top-rope, lead or bouldering problem.
    Climbs can optionally belong to Walls.
    """
    name = models.CharField(max_length=256)
    current = models.BooleanField(default=True)
    climb_type =  models.IntegerField(choices=CLIMB_TYPE, null=True, blank=True)
    business = models.ForeignKey(Business)
    wall = models.ForeignKey(Wall, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)  # Arbitrary ordering.
    #difficulty_type
    difficulty_rating = models.CharField(max_length=16)
