# Django imports
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext as _
# Third-party app imports
from model_utils.models import TimeStampedModel
from model_utils import Choices


CLIMB_TYPE = Choices(
    (0, 'toprope', _('Top rope')),
    (1, 'lead', _('Lead')),
    (2, 'bouldering', _('Bouldering')),
)
GRADE_TYPE = Choices(
    (0, 'ewbanks', _('Ewbanks')),
    # TODO: additional grading systems
)


class Business(TimeStampedModel):
    """Businesses own Walls and Climbs.
    Define a standard grade type to use for climbing and bouldering routes.
    """
    name = models.CharField(max_length=512)
    slug = models.SlugField(max_length=128)
    current = models.BooleanField(default=True)
    #default_grade_type
    #managers - M2M for business managers, can update business details, etc.
    #employees - M2M for business staff, can update walls and climbs.
    #email (primary)
    #address
    #location
    #website
    #logo_image

    class Meta:
        verbose_name_plural = 'businesses'

    def __unicode__(self):
        return u'{}'.format(self.name)


class Wall(TimeStampedModel):
    """Walls belong to a business, and can be used to organise climbs.
    """
    name = models.CharField(max_length=256)
    current = models.BooleanField(default=True)
    business = models.ForeignKey(Business)
    climb_type = models.IntegerField(
        choices=CLIMB_TYPE, default=CLIMB_TYPE.toprope, null=True, blank=True)
    position = models.PositiveIntegerField(null=True, blank=True)  # Arbitrary ordering.

    class Meta:
        ordering = ['business', 'position']

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.business)


class Rope(TimeStampedModel):
    """Rope represents a slot on a wall.
    """
    name = models.CharField(max_length=256, verbose_name='name/number')
    current = models.BooleanField(default=True)
    wall = models.ForeignKey(Wall)

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.wall)


class Climb(TimeStampedModel):
    """Can be top-rope, lead or bouldering problem.
    Climbs can optionally belong to Ropes and/or Walls.
    """
    name = models.CharField(max_length=256)
    current = models.BooleanField(default=True)
    climb_type = models.IntegerField(choices=CLIMB_TYPE, null=True, blank=True)
    business = models.ForeignKey(Business)
    wall = models.ForeignKey(Wall, null=True, blank=True)
    rope = models.ForeignKey(Rope, null=True, blank=True)
    position = models.PositiveIntegerField(null=True, blank=True)  # Arbitrary ordering.
    grade_type = models.IntegerField(choices=GRADE_TYPE, null=True, blank=True)
    grade = models.CharField(max_length=16)
    # TODO: grading system validation
    #setter
    #qr_hash

    class Meta:
        ordering = ['business', 'position']

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.business)


class Rating(TimeStampedModel):
    """Record user 'likes' or 'dislikes' of specific climbs.
    """
    user = models.ForeignKey(get_user_model())
    climb = models.ForeignKey(Climb)
    like = models.NullBooleanField(default=None)  # +ve: liked it

    def __unicode__(self):
        if self.like:
            return u'{} liked {}'.format(self.user, self.climb)
        else:
            return u'{} disliked {}'.format(self.user, self.climb)
