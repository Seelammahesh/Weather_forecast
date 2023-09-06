from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import State,District
from django.db import IntegrityError
# Create your views here.

@api_view(['POST'])
def add_state(request):
    name=request.POST.get('name',None)
    if name is None:
        context={
            'message':'state  is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            name=State.objects.create(
                name=name
            )
            name.save()
            context={
                'message':'state is created',
                'data':{
                    'name':name.name
                }

            }
            return Response(context,status=status.HTTP_201_CREATED)
        except ValueError:
            context={
                'message':'invalid state'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            context={
                'message':'invalid state_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_state(request):
    state_id=request.POST.get('state_id',None)
    new_name=request.POST.get('new_name',None)
    if state_id is None or new_name is None:
        context={
            'message':'state_id/new_name is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=State.objects.get(id=state_id)
            if new_name:
                new_record.name=new_name
            new_record.save()
            context={
                'message':'state updated Successfully'
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid state_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except State.DoesNotExist:
            context={
                'message':'state_id does not exist'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            context={
                'message':'Duplicate entry or invalid state_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_state(request):
    states_list=State.objects.all()
    states=[]

    if not states_list:
        context={
            'message':'no states present here!'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    for state in states_list:
        data={
            'state_id':state.id,
            'name':state.name
        }
        states.append(data)
    context={
        'data':states
        }
    return Response(context,status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_state(request):
    state_id = request.POST.get('state_id', None)
    if state_id is None:
        context = {
            'message': 'state_id is missing'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            state = State.objects.get(id=state_id)
            state.delete()
            context = {
                'message': ' state is successfully deleted'
            }
            return Response(context, status=status.HTTP_200_OK)
        except ValueError:
            context = {
                'message': 'invalid state id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_district(request):
    state_id=request.POST.get('state_id',None)
    name=request.POST.get('name',None)
    rainfall_type=request.POST.get('rainfall_type',None)
    if state_id is None or name is None or rainfall_type is None:
        context={
            'message':'state_id/name/rainfall-type is missing'
        }
        return  Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=District.objects.create(
                state_id=state_id,
                name=name,
                rainfall_type=rainfall_type
            )
            new_record.save()
            context={
                'message':'new_record added succesfully',
                'data':{

                    'state_id':new_record.state_id,
                    'state_name':new_record.state.name,
                    'district_id':new_record.id,
                    'name':new_record.name,
                    'rainfall_type':new_record.rainfall_type,
                    'created_at':new_record.created_at,
                    'updated_at':new_record.updated_at
                }
            }
            return Response(context,status=status.HTTP_201_CREATED)
        except ValueError:
            context={
                'message':'invalid state_name'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            context={
                'message':'invalid state_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update_district(request):
    district_id = request.POST.get('district_id', None)
    state_id=request.POST.get('state_id',None)
    name = request.POST.get('name', None)
    rainfall_type = request.POST.get('rainfall_type', None)
    if district_id is None or state_id is None or  name is None or rainfall_type is None:
        context = {
            'message': 'district_id/state_id/name/new_rainfall_type  is missing'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record = District.objects.get(id=district_id)
            if state_id:
                new_record.state_id=state_id
            if name:
                new_record.name=name
            if rainfall_type:
                new_record.rainfall_type= rainfall_type
                new_record.save()

            context = {
                'message': "district updated successfully"
            }
            return Response(context, status=status.HTTP_200_OK)

        except District.DoesNotExist:
            context = {
                'message': 'Invalid district_id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            context = {
                'message': 'Duplicate entry or invalid district ID/sate_id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context = {
                'message': 'Invalid district_id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_district(request):
    district_list=District.objects.all()
    districts=[]
    if not district_list:
        context={
            'message':'empty .no districts present'
        }
        return Response(context,statues=status.HTTP_400_BAD_REQUEST)
    for district in district_list:
        data={
            'state_id': district.state_id,
            'state_name': district.state.name,
            'district_id': district.id,
            'name':district.name,
            'rainfall_type':district.rainfall_type,
            'created_at': district.created_at,
            'updated_at': district.updated_at
        }
        districts.append(data)
        context={
            'data':districts
        }
    return Response(context,status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_district(request):
    district_id = request.POST.get('district_id', None)
    if district_id is None:
        context = {
            'message': 'district_id is missing'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            district = District.objects.get(id=district_id)
            district.delete()
            context = {
                'message': ' district is successfully deleted'
            }
            return Response(context, status=status.HTTP_200_OK)
        except ValueError:
            context = {
                'message': 'invalid district id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)





