# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TestTable(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=30)  # Field name made lowercase.
    doj = models.DateField(db_column='DOJ')  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    salary = models.FloatField(db_column='Salary')  # Field name made lowercase.
    profile_image = models.ImageField(db_column='Profile_image', max_length=30)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=30)
    permanent_employee=models.BooleanField(db_column='Permanent_Employee')# Field name made lowercase.
    bio = models.TextField(db_column='Bio')  # Field name made lowercase.
    preffered_shifts = models.TextField(db_column='Preffered_Shifts')  # Field name made lowercase.
    age=models.IntegerField(db_column='Age')

    class Meta:
        managed = False
        db_table = 'test_table'