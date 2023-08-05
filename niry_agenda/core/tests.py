import json

from datetime import datetime, timezone

from rest_framework.test import APITestCase

from .models import Scheduling, Store

class TestSchedulingList(APITestCase):
    

    def test_listagem_vazia(self):
        response = self.client.get("/api/v1/scheduling/")
        data = json.loads(response.content)
        
        self.assertEqual(data,[])
    
    def test_listagem_de_agendamento_criados(self):
        Store.objects.create(
            social_name="Teste",
            cnpj="89871238000165",
            active = True
        )

        store = Store.objects.all().first()

        Scheduling.objects.create(
            scheduling_date =datetime(2023,8,10,10,00,00).replace(tzinfo=timezone.utc),
            name= "Corte Cabelo",
            email= "faladaoyuriarantes@gmail.com.br",
            phone= "33999467304",
            active= True,
            store=store
        )

        obj = Scheduling.objects.all()

        response = self.client.get("/api/v1/scheduling/")

        data = json.loads(response.content)

        print(type(data))

        #self.assertDictEqual(data)