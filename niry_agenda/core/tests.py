import json

from datetime import datetime, timezone

from rest_framework.test import APITestCase

from .models import Scheduling, Store, Schedule, Client

class TestSchedulingList(APITestCase):
    def setUp(self) -> None:
        self.store = Store.objects.create(
            social_name="Teste",
            cnpj="89871238000163",
            active = True
        )

        self.client_info = Client.objects.create(
            name="Yuri Arantes",
            email="falaryuriarantes@gmail.com",
            phone="33999467305"
        )

        self.schedules = Schedule.objects.create(
            store=self.store,
            day=5,
            first_start_at='09:00:00',
            first_end_at='12:00:00'
        )

    def test_listagem_vazia(self):
        response = self.client.get("/api/v1/scheduling/")
        data = json.loads(response.content)
        
        self.assertEqual(response.status_code,200)
        self.assertListEqual(data,[])
    
    def test_listagem_de_agendamento_criados(self):
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
            client=self.client_info,
            active= True,
            store=self.store
        )

        response = self.client.get("/api/v1/scheduling/")

        data = json.loads(response.content)

        self.assertListEqual(data,list)
        self.assertEqual(response.status_code,200)
    
    def test_criar_novo_agendamento(self):
        dict = {
                "id":1,
                "scheduling_date": datetime(2030,8,10,9, tzinfo=timezone.utc) ,# "2030-08-10T09:00:00Z",
                "store":1,
                "client":1,
                "active":True,
            }
        
        response = self.client.post(path="/api/v1/scheduling/", data=dict, format='json')

        response_data = json.loads(response.content)

        print(response_data)
        print(dict)

        self.assertDictEqual(response_data,dict)
        self.assertEqual(response.status_code,201)