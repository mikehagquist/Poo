from django.db import models

class League(models.Model):
    leaguename = models.TextField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    League = models.ForeignKey(League, on_delete=models.CASCADE)
    coursename = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class CourseHoles(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    League = models.ForeignKey(League, on_delete=models.CASCADE)
    holenumber = models.PositiveSmallIntegerField()
    holepar = models.PositiveSmallIntegerField()
    holehandicapmen = models.PositiveSmallIntegerField()
    holehandicapladies = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

class Roster(models.Model):
    League = models.ForeignKey(League, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    #authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline