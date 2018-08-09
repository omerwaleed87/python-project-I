# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

from django.http import JsonResponse
from .models import Type, Purpose, Location, Listing, User

# def index(request):
#     latest_question_list = Type.objects.all()[:1]
#     # for q in latest_question_list
#     #     output[] = q; 
#     # output = ', '.join([q.title for q in latest_question_list])
#     output = latest_question_list
#     return HttpResponse(output)

# -------------- Pass data set to provided view without shortcut

def listing(request):
    
    ######     PROPERTY TYPE CODE    #####

    typeObject = Type.objects.get(tid=request.GET.get("type", ""))
    typeId = typeObject.tid
    typeUrl = typeObject.url
    typeTitle = typeObject.type
    typeParent = typeObject.parent
    
    if typeParent == '0':
        childTypes = []
        counter = 0
        childTypeObject = Type.objects.filter(parent=typeId)
        while counter < len(childTypeObject):
            childTypes.append(childTypeObject[counter].tid)
            counter += 1
    else:
        childTypes = ""
        childTypes = typeId

    ##################################

    purposeObject = Purpose.objects.get(pid=request.GET.get("purpose", ""))
    purposeId = purposeObject.pid
    purposeUrl = purposeObject.url
    purposeTitle = purposeObject.purpose

    ######     LOCATION   CODE  ######

    locationObject = Location.objects.get(lid=request.GET.get("location", ""))
    locationId = locationObject.lid
    locationParent = locationObject.parent
    
    if locationParent == 0:
        childLocations = []
        counter = 0
        childLocationObject = Location.objects.filter(parent=locationId)
        while counter < len(childLocationObject):
            childLocations.append(childLocationObject[counter].lid)
            counter += 1
    else:
        childLocations = ""
        childLocations = locationId

    ########################     LOCATION   CODE   END  ######

    combined_queryset = Listing.objects.filter(purpose=purposeId, type_id__in=childTypes, location_id__in=childLocations)
    listingObject = combined_queryset.order_by('-listId')

    counter = 0
    propertyObj = {}
    while counter < len(listingObject):
        propertyObj[counter] = {}
        propertyObj[counter]['id'] = listingObject[counter].listId
        
        propertyObj[counter]['purposeDetail'] = {}
        propertyObj[counter]['purposeDetail']['id'] = purposeObject.pid
        propertyObj[counter]['purposeDetail']['title'] = purposeTitle
        propertyObj[counter]['purposeDetail']['url'] = purposeUrl
        
        typeObject1 = Type.objects.get(tid=listingObject[counter].type)
        typeId1 = typeObject1.tid
        typeTitle1 = typeObject1.type
        typeUrl1 = typeObject1.url
        
        propertyObj[counter]['typeDetail'] = {}
        propertyObj[counter]['typeDetail']['id'] = typeId1
        propertyObj[counter]['typeDetail']['title'] = typeTitle1
        propertyObj[counter]['typeDetail']['url'] = typeUrl1

        propertyObj[counter]['title'] = listingObject[counter].title
        propertyObj[counter]['description'] = listingObject[counter].description
        propertyObj[counter]['price'] = listingObject[counter].price
        propertyObj[counter]['area'] = listingObject[counter].areaCovered

        propertyObj[counter]['userDetail'] = {}
        userObject = User.objects.get(uid=listingObject[counter].user)
        propertyObj[counter]['userDetail']['username'] = userObject.username
        propertyObj[counter]['userDetail']['email'] = userObject.email
        propertyObj[counter]['userDetail']['phone'] = userObject.phone

        locationObject = Location.objects.get(lid=listingObject[counter].location)
        locationId = locationObject.lid
        locationTitle = locationObject.location
        locationParent1 = locationObject.parent

        parentLocationData = Location.objects.get(lid=locationParent1)
        parentLocationTitle = parentLocationData.location

        propertyObj[counter]['locationdetail'] = {}
        propertyObj[counter]['locationdetail']['locId'] = locationId
        propertyObj[counter]['locationdetail']['locationTitle'] = locationTitle
        propertyObj[counter]['locationdetail']['parentTitle'] = parentLocationTitle
        
        propertyObj[counter]['imagedetail'] = {}
        propertyObj[counter]['imagedetail'][0] = listingObject[counter].image

        propertyObj[counter]['url'] = {}
        propertyObj[counter]['url'][0] = "/"+ purposeUrl +"/"+ typeUrl1 +"/"+ locationObject.location_key +"/"+ listingObject[counter].title.replace(" ", "_") +"-"+listingObject[counter].listId 
        counter = counter+1

    context = {
        'listing' : propertyObj,
        'lising_count' : len(listingObject),
    }
    return JsonResponse(context)


# -------------- PAss data set to provided view with shortcut

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)

def breadcrumb(request):
    
    typeObject = Type.objects.get(tid=request.GET.get("type", ""))
    typeUrl = typeObject.url
    typeTitle = typeObject.type

    purposeObject = Purpose.objects.get(pid=request.GET.get("purpose", ""))
    purposeUrl = purposeObject.url
    purposeTitle = purposeObject.purpose

    locationObject = Location.objects.get(location_key=request.GET.get("location_key", ""))
    locationId = locationObject.lid
    locationTitle = locationObject.location
    locationLevel = locationObject.level

    locationObj = {'breadcrumb' : {}}
    locationObj['breadcrumb']['locId'] = locationId
    locationObj['breadcrumb']['locationTitle'] = locationTitle
    locationObj['breadcrumb']['level'] = locationLevel
    locationObj['breadcrumb']['breadcrumbTitle'] = typeTitle + " " + purposeTitle + " in " + locationTitle

    index = 0
    locationObj['breadcrumb']['locBreadcrumb'] = {}
    defParentId = locationId
    concateLocIds = "";
    while defParentId != 0:
        locObject = Location.objects.get(lid=defParentId)
        locationObj['breadcrumb']['locBreadcrumb'][index] = {}
        locationObj['breadcrumb']['locBreadcrumb'][index]['id'] = locObject.lid
        locationObj['breadcrumb']['locBreadcrumb'][index]['title'] = locObject.location
        locationObj['breadcrumb']['locBreadcrumb'][index]['key'] = locObject.location_key
        locationObj['breadcrumb']['locBreadcrumb'][index]['breadcrumbTitle'] = typeTitle +" "+ purposeTitle +" in "+ locObject.location
        locationObj['breadcrumb']['locBreadcrumb'][index]['url'] = "/"+ purposeUrl +"/"+ typeUrl +"/"+ locObject.location_key +"/"
        index = index + 1
        concateLocIds = concateLocIds + locObject.lid +";"
        defParentId = locObject.parent
        
    locationObj['breadcrumb']['locIds'] = concateLocIds

    context = {
        'breadcrumb' : locationObj,
    }
    return JsonResponse(context)


def location(request):
    locObject = Location.objects.all()

    counter = 0
    locationData = {}
    while counter < len(locObject):
        
        locationData[counter] = {}
        locationData[counter]['id'] = locObject[counter].lid
        locationData[counter]['title'] = locObject[counter].location
        locationData[counter]['level'] = locObject[counter].level
        locationData[counter]['key'] = locObject[counter].location_key
        locationData[counter]['parentId'] = locObject[counter].parent

        counter += 1

    context = {
        'location' : locationData,
    }
    return JsonResponse(context)

def type(request):
    typeObject = Type.objects.all()

    counter = 0
    typeData = {}
    while counter < len(typeObject):
        
        typeData[counter] = {}
        typeData[counter]['id'] = typeObject[counter].tid
        typeData[counter]['title'] = typeObject[counter].type
        typeData[counter]['url'] = typeObject[counter].url
        typeData[counter]['parent'] = typeObject[counter].parent

        counter += 1

    context = {
        'type' : typeData,
    }
    return JsonResponse(context)

def purpose(request):
    purposeObject = Purpose.objects.all()

    counter = 0
    purposeData = {}
    while counter < len(purposeObject):
        
        purposeData[counter] = {}
        purposeData[counter]['id'] = purposeObject[counter].pid
        purposeData[counter]['title'] = purposeObject[counter].purpose
        purposeData[counter]['url'] = purposeObject[counter].url

        counter += 1

    context = {
        'purpose' : purposeData,
    }
    return JsonResponse(context)
    
def details(request):
    
    ######     PROPERTY TYPE CODE    #####

    typeObject = Type.objects.get(tid=request.GET.get("type", ""))
    typeId = typeObject.tid
    typeUrl = typeObject.url
    typeTitle = typeObject.type
    typeParent = typeObject.parent
    
    if typeParent == '0':
        childTypes = []
        counter = 0
        childTypeObject = Type.objects.filter(parent=typeId)
        while counter < len(childTypeObject):
            childTypes.append(childTypeObject[counter].tid)
            counter += 1
    else:
        childTypes = ""
        childTypes = typeId

    ##################################

    purposeObject = Purpose.objects.get(pid=request.GET.get("purpose", ""))
    purposeId = purposeObject.pid
    purposeUrl = purposeObject.url
    purposeTitle = purposeObject.purpose

    ######     LOCATION   CODE  ######

    locationObject = Location.objects.get(lid=request.GET.get("location", ""))
    locationId = locationObject.lid
    locationParent = locationObject.parent
    
    if locationParent == 0:
        childLocations = []
        counter = 0
        childLocationObject = Location.objects.filter(parent=locationId)
        while counter < len(childLocationObject):
            childLocations.append(childLocationObject[counter].lid)
            counter += 1
    else:
        childLocations = ""
        childLocations = locationId

    ########################     LOCATION   CODE   END  ######

    combined_queryset = Listing.objects.filter(purpose=purposeId, type_id__in=childTypes, location_id__in=childLocations, listId=request.GET.get("selector", ""))
    listingObject = combined_queryset.order_by('-listId')

    counter = 0
    propertyObj = {}
    while counter < len(listingObject):
        propertyObj[counter] = {}
        propertyObj[counter]['id'] = listingObject[counter].listId
        
        propertyObj[counter]['purposeDetail'] = {}
        propertyObj[counter]['purposeDetail']['id'] = purposeObject.pid
        propertyObj[counter]['purposeDetail']['title'] = purposeTitle
        propertyObj[counter]['purposeDetail']['url'] = purposeUrl
        
        typeObject1 = Type.objects.get(tid=listingObject[counter].type)
        typeId1 = typeObject1.tid
        typeTitle1 = typeObject1.type
        typeUrl1 = typeObject1.url
        
        propertyObj[counter]['typeDetail'] = {}
        propertyObj[counter]['typeDetail']['id'] = typeId1
        propertyObj[counter]['typeDetail']['title'] = typeTitle1
        propertyObj[counter]['typeDetail']['url'] = typeUrl1

        propertyObj[counter]['title'] = listingObject[counter].title
        propertyObj[counter]['description'] = listingObject[counter].description
        propertyObj[counter]['price'] = listingObject[counter].price
        propertyObj[counter]['area'] = listingObject[counter].areaCovered
        propertyObj[counter]['area'] = listingObject[counter].areaCovered

        propertyObj[counter]['userDetail'] = {}
        userObject = User.objects.get(uid=listingObject[counter].user)
        propertyObj[counter]['userDetail']['username'] = userObject.username
        propertyObj[counter]['userDetail']['email'] = userObject.email
        propertyObj[counter]['userDetail']['phone'] = userObject.phone

        locationObject = Location.objects.get(lid=listingObject[counter].location)
        locationId = locationObject.lid
        locationTitle = locationObject.location
        locationParent1 = locationObject.parent

        parentLocationData = Location.objects.get(lid=locationParent1)
        parentLocationTitle = parentLocationData.location

        propertyObj[counter]['locationdetail'] = {}
        propertyObj[counter]['locationdetail']['locId'] = locationId
        propertyObj[counter]['locationdetail']['locationTitle'] = locationTitle
        propertyObj[counter]['locationdetail']['parentTitle'] = parentLocationTitle
        
        propertyObj[counter]['imagedetail'] = {}
        propertyObj[counter]['imagedetail'][0] = listingObject[counter].image

        propertyObj[counter]['url'] = {}
        propertyObj[counter]['url'][0] = "/"+ purposeUrl +"/"+ typeUrl1 +"/"+ locationObject.location_key +"/"+ listingObject[counter].title.replace(" ", "_") +"-"+listingObject[counter].listId 
        counter = counter+1

    context = {
        'details' : propertyObj,
    }
    return JsonResponse(context)
# Create your views here.