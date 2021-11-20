from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F

# Create your models here.
class CurrentGroup(models.Model):
    CurrentGroupID = models.AutoField(primary_key=True, null=False)

class Template(models.Model):
    TemplateID = models.AutoField(primary_key=True, null=False)
    Name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.Name

class ActivityCategory(models.Model):
    ActivityCategoryID = models.AutoField(primary_key=True, null=False)
    Name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.Name


class QuotationStatus(models.Model):
    QuotationStatusID = models.AutoField(primary_key=True, null=False)
    Name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.Name

class Activity(models.Model):
    ActivityID = models.AutoField(primary_key=True, null=False)
    Name = models.CharField(max_length=100, null=False)
    PricePH = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    ActivityCategoryID = models.ForeignKey(ActivityCategory,on_delete=models.CASCADE , null=False)
    Quantity = models.IntegerField(null=False)

    def __str__(self):
        return self.Name

class TemplateListItem(models.Model):
    TemplateID = models.ForeignKey(Template,on_delete=models.CASCADE , null=False)
    TemplateListID = models.AutoField(primary_key=True,  null=False)
    ActivityID = models.ForeignKey(Activity, on_delete=models.CASCADE , null=False)

    def __str__(self):
        return str(self.ActivityID)

class BuildingType(models.Model):
    BuildingTypeID = models.AutoField(primary_key=True, null=False)
    Name = models.CharField(max_length=100, null=False)
    Area = models.DecimalField(max_digits=20, decimal_places=5,null=True)
    Rooms = models.IntegerField(null=True)
    Bathrooms = models.IntegerField(null=True)
    Kitchens = models.IntegerField(null=True)

    def __str__(self):
        return self.Name

class RoomType(models.Model):
    RoomTypeID = models.AutoField(primary_key=True, null=False)
    RoomName = models.CharField(max_length=100, null=False)
    BuildingTypeID = models.ForeignKey(BuildingType,on_delete=models.CASCADE , null=False)

    def __str__(self):
        return self.RoomName

class Quotation(models.Model):
    QuotationID = models.AutoField(primary_key=True, null=False)
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    QuotationStatusID = models.ForeignKey(QuotationStatus,on_delete=models.CASCADE , null=False)
    BuildingTypeID = models.ForeignKey(BuildingType,on_delete=models.CASCADE , null=False)
    Area = models.DecimalField(max_digits=20, decimal_places=5,null=False)
    Rooms = models.IntegerField(null=False)
    Bathrooms = models.IntegerField(null=False)
    Kitchens = models.IntegerField(null=False)

    def __str__(self):
        return str(self.QuotationID)


class ActivityListItem(models.Model):
    ActivityListID = models.AutoField(primary_key=True, null=False)
    ActivityID = models.ForeignKey(Activity, on_delete=models.CASCADE ,null=False)
    QuotationID = models.ForeignKey(Quotation,on_delete=models.CASCADE, null=False)
    # CurrentGroupID = models.ForeignKey(CurrentGroup,on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.ActivityListID)

class RoomList(models.Model):
    RoomListID = models.AutoField(primary_key=True, null=False)
    RoomTypeID = models.ForeignKey(RoomType,on_delete=models.CASCADE , null=False)
    QuotationID = models.ForeignKey(Quotation,on_delete=models.CASCADE , null=False)

    def __str__(self):
        return self.RoomListID

class BuildingTypeData(models.Model):
    buildingType = models.CharField(max_length=100, null=False)
    buildingName = models.CharField(max_length=100, null=False)
    buildingTypeLength = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.buildingType

class BuildingItem(models.Model):
    buildingItem = models.CharField(max_length=100, null=False)
    itemName = models.CharField(max_length=100, null=False)
    buildingType = models.ForeignKey(BuildingTypeData, on_delete=models.CASCADE, null=False)
    buildingItemLength = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.buildingItem


class rowData(models.Model):
    buildingItem = models.ForeignKey(BuildingItem, on_delete=models.CASCADE, null=False)
    dataRowID = models.CharField(max_length=100, null=False)
    data1td = models.CharField(max_length=100, null=False)
    data2td = models.CharField(max_length=100, null=True)
    data3td = models.CharField(max_length=100, null=False)
    data4td = models.CharField(max_length=100, null=True)
    data5td = models.CharField(max_length=100, null=True)
    data6td = models.CharField(max_length=100, null=True)
    data7td = models.CharField(max_length=100, null=False)
    data8td = models.CharField(max_length=100, null=True)
    data9td = models.CharField(max_length=100, null=True)
    data10td = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.dataRowID
