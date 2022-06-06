from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(_('Title'), max_length=2056)
    slug = models.SlugField(_('Slug'), unique=True, blank=True, null=True)
    parent = models.ForeignKey('self', verbose_name=_('Parent'), related_name="children", blank=True, null=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('knowledge-category-detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Question(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_('User'), related_name='user_questions',
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=_('Category'), related_name="questions",
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=_('Question'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))

    is_active = models.BooleanField(_('Is active'), default=False)
    order = models.PositiveSmallIntegerField(_('Order'), default=1)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('knowledge-questions-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['order']
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
