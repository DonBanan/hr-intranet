from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Niko(models.Model):
    MOOD_TYPES = (
        (0, _('Angry')),
        (1, _('Sad')),
        (2, _('Neutral')),
        (3, _('Happy')),
    )
    user = models.ForeignKey(get_user_model(), verbose_name=_('User'), related_name='niko',
                             on_delete=models.CASCADE)
    mood = models.IntegerField(_('Mood'), choices=MOOD_TYPES)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    def __str__(self):
        return '{0} - {1} ({2})'.format(self.user.get_full_name(), self.get_mood_display(), self.created_at)

    class Meta:
        verbose_name = _('Niko-Niko calendar')
        verbose_name_plural = _('Niko-Niko calendar')
