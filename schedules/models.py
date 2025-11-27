from django.db import models
from businesses.models import Business
from services.models import Service


class WorkingHours(models.Model):
    WEEKDAYS = (
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    )

    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="working_hours")
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="working_hours",
        null=True,
        blank=True,
        help_text="Optional: working hours specific to a service"
    )

    weekday = models.PositiveSmallIntegerField(choices=WEEKDAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('business', 'service', 'weekday')
        ordering = ['business', 'weekday', 'start_time']

    def __str__(self):
        return f"{self.business.name} – {self.get_weekday_display()} ({self.start_time}-{self.end_time})"