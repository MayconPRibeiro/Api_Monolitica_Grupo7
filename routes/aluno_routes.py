from flask import Blueprint, request, jsonify
from controllers.aluno_controller import AlunoController

aluno_bp = Blueprint ('alunos', __name__, url_prefix='/alunos')

@aluno_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = AlunoController.listar()
    return jsonify([
        {
            'id': aluno.id,
            'nome': aluno.nome,
            'idade': aluno.idade,
            'turma_id': aluno.turma_id,
            'data_nascimento': aluno.data_nascimento.isoformat() if aluno.data_nascimento else None,
            'nota_primeiro_semestre': aluno.nota_primeiro_semestre,
            'nota_segundo_semestre': aluno.nota_segundo_semestre,
            'media_final': aluno.media_final
        }
        for aluno in alunos
    ]), 200

@aluno_bp.route('/alunos', methods=['POST'])
def criar_aluno():
    data = request.get_json()
    if not data or 'nome' not in data or 'idade' not in data:
        return jsonify({'erro': 'Campos obrigatórios: nome e idade'}), 400

    novo_aluno = AlunoController.criar(data)
    return jsonify({
        'mensagem': 'Aluno criado com sucesso!',
        'id': novo_aluno.id,
        'nome': novo_aluno.nome,
        'idade': novo_aluno.idade
    }), 201

@aluno_bp.route('/alunos/<int:aluno_id>', methods=['PUT'])
def atualizar_aluno(aluno_id):
    data = request.get_json()
    aluno_atualizado = AlunoController.atualizar(aluno_id, data)
    return jsonify({
        'mensagem': 'Aluno atualizado com sucesso!',
        'id': aluno_atualizado.id,
        'nome': aluno_atualizado.nome,
        'idade': aluno_atualizado.idade
    }), 200

@aluno_bp.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def deletar_aluno(aluno_id):
    AlunoController.deletar(aluno_id)
    return jsonify({'mensagem': 'Aluno deletado com sucesso!'}), 200

