from

class TurmaController:
    @staticmethod
    def listar_turmas():
        return Turmas.query.all()