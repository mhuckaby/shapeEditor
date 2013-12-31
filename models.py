from django.contrib.gis.db import models

# Create your models here.
class BaseMap(models.Model):
    name = models.CharField(max_length=50)
    geometry = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    def __unicode__(self):
        return self.name
    
class Shapefile(models.Model):
    filename = models.CharField(max_length=255)
    srs_wkt = models.TextField(max_length=1000)
    geom_type = models.CharField(max_length=50)
    encoding = models.CharField(max_length=20)
    def __unicode__(self):
        return self.filename

    
class Attribute(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    name = models.CharField(max_length=255)
    type = models.IntegerField()
    width = models.IntegerField()
    precision = models.IntegerField()

    
class Feature(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    geom_point = models.PointField(srid=4326,blank=True,null=True)
    geom_multipoint = models.MultiPointField(srid=4326,blank=True,null=True)
    geom_multilinestring = models.MultiLineStringField(srid=4326,blank=True,null=True)
    geom_multipolygon = models.MultiPolygonField(srid=4326,blank=True,null=True)
    geom_geometrycollection = models.GeometryCollectionField(srid=4326,blank=True,null=True)
    objects = models.GeoManager()

    
class AttributeValue(models.Model):
    feature = models.ForeignKey(Feature)
    attribute = models.ForeignKey(Attribute)
    value = models.CharField(max_length=255,blank=True, null=True)

