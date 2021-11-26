from django.core.management.base import BaseCommand, CommandError
from requests.api import options
from django.core.mail import send_mail
import requests


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('email')

    def handle(self, *args, **options):
       value_email = options["email"]
       self.get_pharma(value_email)
       


    def get_pharma(self, value_email):
        
        response = requests.get('https://farmanet.minsal.cl/maps/index.php/ws/getLocalesTurnos', params={})

        if response.status_code == 200:
                response_api = response.json()
                name_dict = {}
                for vals in response_api:
                    local = vals['local_nombre']
                    if not local in name_dict:
                        name_dict[local] = 1
                    else:
                        name_dict[local] +=1
                total_pharma = 0
                for values in name_dict.values():
                    total_pharma += values
                list_ph = ''    
                for pharma,qty in name_dict.items():
                    list_ph += pharma + " => " + str(qty) + '\n'
                hola = 'Total => ' + str(total_pharma)
                send_mail(
                    'Desafío de Desarrollo Backend Medinet',
                    list_ph + '\n' + hola,
                    'from@example.com',
                    [value_email],
                    fail_silently=False,
                )
               
                

           



   
            
