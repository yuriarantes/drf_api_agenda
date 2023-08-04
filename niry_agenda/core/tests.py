import json
from rest_framework.test import APITestCase

class TestSchedulingList(APITestCase):
    def test_listagem_vazia(self):
        response = self.client.get("/api/v1/scheduling/")
        data = json.loads(response.content)
        
        self.assertEqual(data,[])