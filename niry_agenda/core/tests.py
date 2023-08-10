import json

from datetime import datetime, timezone

from rest_framework.test import APITestCase

from .models import Scheduling, Store, Schedule, Client

class TestSchedulingList(APITestCase):
    def set_store(self):
        self.store = Store.objects.create(
            social_name="Teste",
            cnpj="89871238000163",
            active = True
        )
    
    def set_client_info(self):
        self.client_info = Client.objects.create(
            name="Yuri Arantes",
            email="falaryuriarantes@gmail.com",
            phone="33999467305"
        )

    def test_listagem_vazia(self):
        response = self.client.get("/api/v1/scheduling/")
        data = json.loads(response.content)
        
        self.assertEqual(data,[])
    
    """
    def test_listagem_de_agendamento_criados(self):
        self.set_store()

        list = [
            {
                "id":1,
                "scheduling_date":"2023-08-10T10:00:00Z",
                "store":1,
                "client":1,
                "active":True,
            },
        ]

        Scheduling.objects.create(
            scheduling_date =datetime(2023,8,10,10,00,00).replace(tzinfo=timezone.utc),
            name= "Corte Cabelo",
            email= "faladaoyuriarantes@gmail.com.br",
            phone= "33999467304",
            active= True,
            store=self.store
        )

        response = self.client.get("/api/v1/scheduling/")

        data = json.loads(response.content)

        self.assertListEqual(data,list)
    """
    
    def test_criar_novo_agendamento(self):
        self.set_store()
        self.set_client_info()

        Schedule.objects.create(
            store=self.store,
            day=3,
            first_start_at='09:00:00',
            first_end_at='12:00:00'
        )

        dict = {
                "scheduling_date":"2023-08-10T10:00:00Z",
                "store":1,
                "client":1,
                "active":"True",
            }
        
        response = self.client.post(path="/api/v1/scheduling/", data=dict, format='json')

        response_data = response.content

        print(response_data)

        self.assertEqual(response.status_code,201)
        #self.assertListEqual()