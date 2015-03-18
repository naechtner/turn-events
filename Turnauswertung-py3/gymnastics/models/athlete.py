from django.db import models
from django.db.models import Sum


class Athlete(models.Model):
  
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    sex = models.CharField(max_length=1, null=False, choices=(('m', 'male'), ('f', 'female')), default='f')
    year_of_birth = models.IntegerField(default=2000)

    club = models.ForeignKey('Club', null=True, blank=True)
    squad = models.ForeignKey('Squad', null=True, blank=True)
    stream = models.ForeignKey('Stream', null=False)
    team = models.ForeignKey('Team', null=True, blank=True)


    class Meta:
        db_table = 'gymnastics_athletes'

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def performance_total(self):
        return self.performance_set.order_by("value")[0:self.stream.all_around_individual_counting_events].aggregate(Sum('value')).get('value__sum', 0.00)

    def performance_final_total(self):
        return self.performance_set.order_by("value_final").aggregate(Sum('value_final')).get('value__sum', 0.00)

    def performances(self):
        performance_dict = {}
        for performance in self.performance_set.all():
            performance_dict[performance.discipline] = performance.value
            performance_dict['{0}_{1}'.format(performance.discipline, 'final')] = performance.value_final
        return performance_dict