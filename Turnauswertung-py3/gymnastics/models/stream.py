from django.db import models

from gymnastics.models.discipline import Discipline

class Stream(models.Model):
  
    difficulty = models.CharField(max_length=10, null=False)
    sex = models.CharField(max_length=1, null=False, choices=(('m', 'male'), ('f', 'female')), default='f')
    minimum_year_of_birth = models.IntegerField(default=2000, null=False)
    all_around_individual = models.BooleanField(default=True)
    all_around_individual_counting_events = models.IntegerField(null=True, blank=True, default=4)
    all_around_team = models.BooleanField(default=True)
    all_around_team_counting_athletes = models.IntegerField(null=True, blank=True, default=4)
    discipline_finals = models.BooleanField(default=False)
    discipline_finals_max_participants = models.IntegerField(null=True, blank=True)

    discipline_set = models.ManyToManyField('Discipline')


    class Meta:
        db_table = 'gymnastics_streams'
        
    def __str__(self):
        return "{0} {1}".format(self.difficulty, self.get_sex_display())

    def ranks(self):
        athlete_dict = {}
        for athlete in self.athlete_set.all():
            performance_total = athlete.performance_total()
            if performance_total == None:
                performance_total = -1
            if not athlete_dict.get(performance_total):
                athlete_dict[performance_total] = []

            athlete_dict[performance_total].append(athlete)

        rank = 0
        ranks_dict = {}  
        for total_value, athlete_list in sorted(athlete_dict.items(), reverse=True):
            rank += 1
            if total_value < 0:
                rank = None
            for athlete_object in athlete_list:
                ranks_dict[athlete_object] = rank
        return ranks_dict