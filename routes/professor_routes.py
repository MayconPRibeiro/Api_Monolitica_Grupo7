from flask import Blueprint, request, jsonify
from controllers.professor_controller import ProfessorController

professor_bp = Blueprint('professores', __name__, url_prefix='/professores')

@professor_bp.route('/', methods=['GET'])
def listar_professores():
    professores = ProfessorController.listar()
    return jsonify([{'id': p.id, 'nome': p.nome, 'idade': p.idade, 'materia': p.materia, 'observacoes': p.observacoes} for p in professores])

@professor_bp.route('/', methods=['POST'])
def criar_professor():
    data = request.get_json()
    professor = ProfessorController.criar(data)
    return jsonify({'id': professor.id, 'nome': professor.nome, 'idade': professor.idade, 'materia': professor.materia, 'observacoes': professor.observacoes}), 201

@professor_bp.route('/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    data = request.get_json()
    professor = ProfessorController.atualizar(id, data)
    return jsonify({'id': professor.id, 'nome': professor.nome, 'idade': professor.idade, 'materia': professor.materia, 'observacoes': professor.observacoes})

@professor_bp.route('/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    ProfessorController.deletar(id)
    return jsonify({'message': 'Professor deletado'})
