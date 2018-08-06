# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

from django.http import JsonResponse
from .models import Type, Purpose, Location
# def index(request):
#     latest_question_list = Type.objects.all()[:1]
#     # for q in latest_question_list
#     #     output[] = q; 
#     # output = ', '.join([q.title for q in latest_question_list])
#     output = latest_question_list
#     return HttpResponse(output)

# -------------- Pass data set to provided view without shortcut

def listing(request):
    # latest_question_list = Listing.objects.all()[:5]
    # template = loader.get_template('polls/index.html')
    host_url = "localhost:3000"
    propertyObj = {
        "0" : {
            'id' : 1,
            'purposeDetail' : {
                'id' : 1,
                'title' : request.GET.get("purpose", ""),
                'url' : "for-sale",
            },
            'typeDetail' : {
                'id' : 4,
                'title' : request.GET.get("type", ""),
                'url' : "apartment",
            },
            'bed' : 3,
            'bath' : 2,
            'price' : 1200000,
            'areaCovered' : 1200,
            'areaLand' : 1500,
            'title' : "Awesome apartment in dubai marina",
            'description' : "Awesome apartment in dubai marina that you can count on",
            'url' : {
                '0' : "/for-sale/apartment/dubai/dubai-marina/Awesome_apartment_in_dubai_marina-1" 
            },
            'userdetail' : {
                'name' : "Omer waleed",
                'email' : "omer24waleed@gmail.com",
                'phone' : "+923228473603"
            },
            'locationdetail' : {
                'locId' : 4,
                'locationTitle' : "Dubai Marina",
                'locIds' : "1;4",
            }
        },
        "1" : {
            'id' : 1,
            'purposeDetail' : {
                'id' : 1,
                'title' : "for sale",
                'url' : "for-sale",
            },
            'typeDetail' : {
                'id' : 4,
                'title' : "apartment",
                'url' : "apartment",
            },
            'bed' : 3,
            'bath' : 2,
            'price' : 1200000,
            'areaCovered' : 1200,
            'areaLand' : 1500,
            'title' : "Awesome apartment in dubai marina",
            'description' : "Awesome apartment in dubai marina that you can count on",
            'url' : {
                '0' : "/for-sale/apartment/dubai/dubai-marina/Awesome_apartment_in_dubai_marina-1" 
            },
            'userdetail' : {
                'name' : "Omer waleed",
                'email' : "omer24waleed@gmail.com",
                'phone' : "+923228473603"
            },
            'locationdetail' : {
                'locId' : 4,
                'locationTitle' : "Dubai Marina",
                'locIds' : "1;4",
            }
        },
    }
    context = {
        'listing' : propertyObj,
        'lising_count' : 2,
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
        locationObj['breadcrumb']['locBreadcrumb'][index]['url'] = "/"+ typeTitle +"/"+ typeUrl +"/"+ locObject.location_key
        index = index + 1
        concateLocIds = concateLocIds + locObject.lid +";"
        defParentId = locObject.parent
        
    locationObj['breadcrumb']['locIds'] = concateLocIds

    context = {
        'breadcrumb' : locationObj,
    }
    return JsonResponse(context)


# Create your views here.