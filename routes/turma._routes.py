from flask import Blueprint, request, jsonify
from controllers.turma_controller import TurmaController
from controllers.professor_controller import consultar_professor

turma_bp = Blueprint('turma', __name__, url_prefix='/turma')

@turma_bp.route('/',methods=['GET'])
def listar_turmas():
  turmas = TurmaController.listar()
  return jsonify([{'id': t.id, 'descricao': t.descricao, 'ativo': t.ativo} for t in turmas])

@turma_bp.route('/', methods=['POST'])
def criar_turma():
    data = request.get_json()
    professor = consultar_professor(data.get("professor_id"))

    if professor:  
      turma = TurmaController.criar(data)  
      return jsonify([{'id': turma.id, 'descricao': turma.descricao, 'professor_id': turma.professor_id, 'ativo': turma.ativo}]), 201
    
    else:
       return jsonify([{'msg' : 'Professor não encontrado'}]), 400
    
@turma_bp.route('/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    data = request.get_json()
    turma = TurmaController.atualizar(id, data)
    return jsonify({'id': turma.id, 'descricao': turma.nome, 'professor_id': turma.professor_id, 'ativo': turma.ativo})


@turma_bp.route('/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    TurmaController.deletar(id)
    return jsonify({'message': 'Turma deletada'})