from django.db import models


class EnteringPerson(models.Model):
    unique_numbers = models.PositiveIntegerField('identifier')
    full_name = models.TextField('initials', max_length=128)
    role = models.TextField('role', max_length=128)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    unique_numbers = models.PositiveIntegerField('identifier')
    full_name = models.TextField('initials', max_length=128)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    

class Teacher(models.Model):
    unique_numbers = models.PositiveIntegerField('identifier')
    full_name = models.TextField('initials', max_length=128)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
    

