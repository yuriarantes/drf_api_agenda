# API

- Lista horários => GET /api/v1/times/

        ['7:00','11:00']

- Listas agendamentos => GET /api/v1/schedules/

        [
            {
                "name":"João Lopes",
                "phone":"33999991212",
                "email":"joaolopes@gmail.com",
            },
            {
                "name":"Pedro Gonçalves",
                "phone":"33999991233",
                "email":"pedro@gmail.com",
            }
        ]

- Detalhar agendamento: GET /api/v1/schedules/<id>/

        {
            "id":<id>
            "name":"João Lopes",
            "phone":"33999991212",
            "email":"joaolopes@gmail.com",
        }

- Criar agendamento: POST /api/v1/schedules/

- Excluir agendamento: DELETE /api/v1/schedules/<id>

- Editar agendamento: PUT/PATCH /api/v1/schedules/<id>