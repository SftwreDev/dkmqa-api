from django.db import models

from plant.models import Plant
from shift.models import Shift
from person.models import Person
from authentication.models import User


# Create your models here.
class Recipient_Email(models.Model):
    plant = models.ForeignKey(Plant, on_delete = models.CASCADE , related_name = 'plant_id')
    shift = models.ForeignKey(Shift, on_delete = models.CASCADE , related_name = 'shift_id')
    person = models.ForeignKey(Person, on_delete = models.CASCADE , related_name = 'person_id')
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'recipient_created_by')
    date_updated = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'recipient_updated_by')

    def __str__(self):
        return self.plant + ' | ' + self.shift + ' | ' + 'From' + self.person

    
    class Meta:
        db_table = 'recipient_email'