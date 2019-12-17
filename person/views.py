from django.http import HttpResponse, JsonResponse
from django.views import View
from person.models import Person
from datetime import datetime
from random import randrange
from datetime import timedelta
import random

from person.person_service import PersonService


class PersonView(View):

    def __init__(self):
        self.person_service = PersonService()

    def get(self, request):
        """
        Http get method to get all persons or person with given pesel
        Example url to get person by pesel: localhost:8000/person/12345678901
        :param request: has string parameter pesel
        :return: JSON response
        """
        pesel = request.GET.get('pesel')
        if pesel:
            person = list(Person.objects.filter(pesel=pesel).values())[0] #TODO exception if more than one
            return JsonResponse(person, safe=False)
        else:
            person_list = list(Person.objects.all().values())
            return JsonResponse(person_list, safe=False)

    def post(self, request, number=1):
        """
        Http method to generate persons and save them to database
        Example url to generate six persons: localhost:8000/person/6
        :param number: number of generated persons, default is 1
        :return: http status for created
        """
        for i in range(0, number):
            #creating new object
            person = self.person_service.generate_person()
            self.person_service.save_person(person) #TODO verify if pesel is not taken
        return HttpResponse(status=201)