from django.db import models

class League(models.Model):
    leaguename = models.TextField()
    active = models.BooleanField(default=True)
    createdate = models.DateTimeField()
    lastupdate = models.DateTimeField()
    
    def __str__(self):
        return self.name

class Course(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    coursename = models.CharField(max_length=200)
    coursepar = models.PositiveSmallIntegerField()
    frontpar = models.PositiveSmallIntegerField()
    backpar = models.PositiveSmallIntegerField()
    active = models.BooleanField(default=True)
    createdate = models.DateTimeField()
    lastupdate = models.DateTimeField()

    def __str__(self):
        return self.name

class CourseHoles(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    holenumber = models.PositiveSmallIntegerField()
    holepar = models.PositiveSmallIntegerField()
    holehandicapmen = models.PositiveSmallIntegerField()
    holehandicapladies = models.PositiveSmallIntegerField()
    frontback = (
        ('F', 'Front Nine'),
        ('B', 'Back Nine'),
    )
    createdate = models.DateTimeField()
    lastupdate = models.DateTimeField()

    def __str__(self):
        return self.name

class Player(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    playerfirstname = models.CharField(max_length=200)
    playerlastname = models.CharField(max_length=200)
    playeremail = models.CharField(max_length=200)
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    secretary = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    createdate = models.DateTimeField()
    lastupdate = models.DateTimeField()

    def __str__(self):
        return self.name
        
class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    teamname = models.CharField(max_length=200)
    createdate = models.DateTimeField()
    lastupdate = models.DateTimeField()

    def __str__(self):
        return self.name

class Teammates(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    teamname = models.CharField(max_length=200)
    createdate = models.DateTimeField()
    lastupdate = models.DateTimeField()

    def __str__(self):
        return self.name

class Teampairings(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    teamname = models.CharField(max_length=200)
    createdate = models.DateTimeField()
    lastupdate = models.DateTimeField()

    def __str__(self):
        return self.name