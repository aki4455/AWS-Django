
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Countries(models.Model):
    country = models.CharField(db_column='Country', max_length=50, primary_key=True,  blank=False, null=False)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    population_millions_field = models.FloatField(db_column='Population (millions)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hdi = models.FloatField(db_column='HDI', blank=True, null=True)  # Field name made lowercase.
    gdp_per_capita = models.CharField(db_column='GDP per Capita', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cropland_footprint = models.FloatField(db_column='Cropland Footprint', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grazing_footprint = models.FloatField(db_column='Grazing Footprint', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    forest_footprint = models.FloatField(db_column='Forest Footprint', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    carbon_footprint = models.FloatField(db_column='Carbon Footprint', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fish_footprint = models.IntegerField(db_column='Fish Footprint', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_ecological_footprint = models.FloatField(db_column='Total Ecological Footprint', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cropland = models.FloatField(db_column='Cropland', blank=True, null=True)  # Field name made lowercase.
    grazing_land = models.FloatField(db_column='Grazing Land', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    forest_land = models.FloatField(db_column='Forest Land', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fishing_water = models.IntegerField(db_column='Fishing Water', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    urban_land = models.FloatField(db_column='Urban Land', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_biocapacity = models.FloatField(db_column='Total Biocapacity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    biocapacity_deficit_or_reserve = models.FloatField(db_column='Biocapacity Deficit or Reserve', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    earths_required = models.FloatField(db_column='Earths Required', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    countries_required = models.FloatField(db_column='Countries Required', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_quality = models.CharField(db_column='Data Quality', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'countries'
