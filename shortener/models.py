import random
import string

from django.conf import settings
from django.db import models


class Url(models.Model):
    long_url = models.URLField(max_length=2000, null=False, blank=False)
    short_url = models.CharField(
        max_length=settings.SUFFIX_LENGTH,
        db_index=True,
        unique=True,
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def _generate_short_url(self) -> str:
        return "".join(
            random.choices(
                string.ascii_lowercase + string.digits, k=settings.SUFFIX_LENGTH
            )
        )

    def save(self, *args, **kwargs) -> None:
        if not self.short_url:
            # collision prevention (unique constraint will not allow to save it, but we want
            # to avoid raising database errors)
            while True:
                self.short_url = self._generate_short_url()

                if not self.__class__.objects.filter(
                    short_url=self.short_url
                ).exists():
                    break

        super().save(*args, **kwargs)
