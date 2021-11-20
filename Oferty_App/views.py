from django.shortcuts import render
from django.db.models import Max
from .models import BuildingType,Template,Activity,TemplateListItem,ActivityListItem,ActivityCategory,BuildingTypeData,BuildingItem,rowData
from django.http import JsonResponse

# Create your views here.
def dashboard(request):

    buildingType = BuildingTypeData.objects.order_by('buildingType','buildingTypeLength','buildingName')
    buildingItem = BuildingItem.objects.order_by('buildingType','buildingItem','itemName','buildingItemLength')
    itemRowData = rowData.objects.order_by('buildingItem','dataRowID') 

    for building in buildingType:
        # print("build")
        for item in buildingItem:
            # print("item",building.id,item.buildingType.id)
            if building.id == item.buildingType.id:
                for row in itemRowData:
                    # print("row",item.id,row.buildingItem.id)
                    if item.id == row.buildingItem.id:
                        print("building:",building.buildingType,", Item:",item.buildingItem," , Data:",row)

    buildingTypes = BuildingType.objects.all()
    templates = Template.objects.all()
    categories = ActivityCategory.objects.all()
    activities = Activity.objects.all()

    
    subactivities = ActivityListItem.objects.all()

    return render(request, 'index.html', {"buildingTypes":buildingTypes,"templates":templates,"activities":activities,"subactivities":subactivities,'buildingType':buildingType,'buildingItem':buildingItem,'itemRowData':itemRowData,"categories":categories} )


# ====================================================

def getSections(request):
    buildingTypeID = request.GET.get('buildingtype_Id')
    data = BuildingType.objects.filter(BuildingTypeID=buildingTypeID).values()
    templates = Template.objects.all().values()
    categories = ActivityCategory.objects.all().values('ActivityCategoryID','Name')
    activities = Activity.objects.all().values('ActivityID','Name','ActivityCategoryID')

    buildingData = list(data)
    templatesData = list(templates)
    categoriesData = list(categories)
    activitiesData = list(activities)
    return JsonResponse({'buildingData':buildingData,'templatesData':templatesData,'categoriesData':categoriesData,'activitiesData':activitiesData})

def addCustomActivity(request):
    templates = Template.objects.all().values()
    categories = ActivityCategory.objects.all().values('ActivityCategoryID','Name')
    activities = Activity.objects.all().values('ActivityID','Name','ActivityCategoryID')
    
    templatesData = list(templates)
    categoriesData = list(categories)
    activitiesData = list(activities)

    return JsonResponse({'templatesData':templatesData,'categoriesData':categoriesData,'activitiesData':activitiesData})

def getTemplates(request):
    templateID = request.GET.get('template_id')
    data = TemplateListItem.objects.filter(TemplateID=templateID).values('TemplateID__Name','ActivityID__Name','ActivityID__PricePH','ActivityID__Quantity','ActivityID__ActivityCategoryID__Name')
    templates = list(data)
    return JsonResponse({'templates':templates})



def getActivity(request):
    activityID = request.GET.get('activityId')
    activityListItemsDetails = ActivityListItem.objects.filter(ActivityID=activityID).values('ActivityID__Name','ActivityID__PricePH','ActivityID__Quantity','ActivityID__ActivityCategoryID__Name','QuotationID__TotalAmount','QuotationID__Area','QuotationID__Rooms','QuotationID__Bathrooms','QuotationID__Kitchens')
    # details = Activity.objects.filter(ActivityID=activityID).values()
    ActivityDetail = list(activityListItemsDetails)
    print(activityListItemsDetails)
    return JsonResponse({'ActivityDetail':ActivityDetail})

def saveRowData(request):

    print(request.GET.get('buildingType'),request.GET.get('buildingItem'))

    if not BuildingTypeData.objects.filter(buildingType=request.GET.get('buildingType')):
        buildTypeID = BuildingTypeData(
            buildingType = request.GET.get('buildingType'),
            buildingName = request.GET.get('buildingTypeName'),
            buildingTypeLength = request.GET.get('buildingTypeLength'),
        )
        buildTypeID.save()
        print("got:",buildTypeID)
    else:
        buildTypeID = BuildingTypeData.objects.get(buildingType=request.GET.get('buildingType'))
        buildTypeID.buildingName = request.GET.get('buildingTypeName')
        buildTypeID.buildingTypeLength = request.GET.get('buildingTypeLength')
        buildTypeID.save()

    
    # print('id', buildTypeID.id)
    # buildTypeObj = BuildingTypeData.objects.get(id=buildTypeID.id)
    # print(buildTypeObj,'obj')

    if not BuildingItem.objects.filter(buildingType=buildTypeID,buildingItem=request.GET.get('buildingItem')):
        buildItemID = BuildingItem(
            buildingType=buildTypeID,
            buildingItem = request.GET.get('buildingItem'),
            itemName = request.GET.get('buildingItemName'),
            buildingItemLength = request.GET.get('buildingItemLength'),
        )
        buildItemID.save()
    else:
        buildItemID = BuildingItem.objects.get(buildingType=buildTypeID,buildingItem=request.GET.get('buildingItem'))
        buildItemID.itemName = request.GET.get('buildingItemName')
        buildItemID.buildingItemLength = request.GET.get('buildingItemLength')
        buildItemID.save()
        
        
    # buildItemObj = BuildingItem.objects.get(pk=buildItemID)

    if not rowData.objects.filter(buildingItem=buildItemID,dataRowID=request.GET.get('dataRowID')):
        rowData(
            buildingItem = buildItemID,
            dataRowID = request.GET.get('dataRowID'),
            data1td = request.GET.get('data1td'),
            data2td = request.GET.get('data2td'),
            data3td = request.GET.get('data3td'),
            data4td = request.GET.get('data4td'),
            data5td = request.GET.get('data5td'),
            data6td = request.GET.get('data6td'),
            data7td = request.GET.get('data7td'),
            data8td = request.GET.get('data8td'),
            data9td = request.GET.get('data9td'),
            data10td = request.GET.get('data10td'),
        ).save()
    else:
        rowID = rowData.objects.get(buildingItem=buildItemID,dataRowID=request.GET.get('dataRowID'))
        rowID.data1td = request.GET.get('data1td')
        rowID.data2td = request.GET.get('data2td')
        rowID.data3td = request.GET.get('data3td')
        rowID.data4td = request.GET.get('data4td')
        rowID.data5td = request.GET.get('data5td')
        rowID.data6td = request.GET.get('data6td')
        rowID.data7td = request.GET.get('data7td')
        rowID.data8td = request.GET.get('data8td')
        rowID.data9td = request.GET.get('data9td')
        rowID.Data10td = request.GET.get('data10td')
        rowID.save()
        
    print('SUCCESS')

    return JsonResponse({})

















# ===================================================================

# ===================================================================

# ===================================================================

# ===================================================================


def activities(request):
    templateID = request.GET.get('template_id')
    activities = TemplateListItem.objects.filter(TemplateID=templateID).values('ActivityID__Name','ActivityID')
    activities = list(activities)
    subactivities = ActivityListItem.objects.all().values('QuotationID__Rooms','QuotationID__Bathrooms','QuotationID__Kitchens','ActivityListID','ActivityID__Name')
    subactivities = list(subactivities)
    return JsonResponse({'activities':activities,'subactivities':subactivities})


def subactivities(request):
    activityID = request.GET.get('activity_id')
    subactivities = ActivityListItem.objects.filter(ActivityID=activityID).values('QuotationID__Rooms','QuotationID__Bathrooms','QuotationID__Kitchens')
    subactivities = list(subactivities)
    return JsonResponse({'subactivities':subactivities})


    # return render(request, 'activities.html',{"activities":activities})