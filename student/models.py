from django.db import models

# Create your models here.


class StudentProfile(models.Model):
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
    )

    STATUS = (
        ("Active", "Acitive"),
        ("Offline", "Offline"),
        ("Do Not Disturb", "Do not Disturb"),
        ("Idle", "Idle"),
    )

    name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    studid = models.IntegerField()
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=50, null=True)
    bdate = models.DateField()
    placebirth = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


# relations per teacher = subject
class Subject(models.Model):
    subcode = models.ManyToManyField('Profsub')


class StudGrades(models.Model):
    studgrades = models.ForeignKey(
        'Grades', on_delete=models.SET_NULL, null=True)


# class Group(models.Model):
# Twillo


# relations to all the upcoming assignments, quizz, and activities
class Reminder(models.Model):
    reminders = models.ForeignKey(
        'Schoolworks', on_delete=models.SET_NULL, null=True)


##############################################
# Prof Models

class ProfessProfile(models.Model):
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
    )

    STATUS = (
        ("Active", "Acitive"),
        ("Offline", "Offline"),
        ("Do Not Disturb", "Do not Disturb"),
        ("Idle", "Idle"),
    )

    name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    numofstud = models.IntegerField()
    contactno = models.IntegerField()
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=50, null=True)
    bdate = models.DateField()
    placebirth = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Schoolworks(models.Model):
    WORKS = (
        ("Assignments", "Assignments"),
        ("Quiz", "Quiz"),
        ("Activities", "Activities"),
        ("Projects", "Projects"),
    )

    schoolwork = models.CharField(max_length=60, choices=WORKS)
    title = models.CharField(max_length=100, null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    duedate = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class Schedule(models.Model):
    days = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.days


class Profsub(models.Model):
    subcode = models.CharField(max_length=50, null=True)
    subname = models.CharField(max_length=200, null=True)
    lec = models.FloatField(max_length=3)
    lab = models.FloatField(max_length=3)
    unit = models.FloatField(max_length=3)
    schedule = models.ForeignKey(
        'Schedule', on_delete=models.SET_NULL, null=True)
    name = models.ForeignKey(
        ProfessProfile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.subname


class Grades(models.Model):
    grades = models.FloatField()
