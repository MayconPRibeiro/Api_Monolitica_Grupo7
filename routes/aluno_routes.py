from flask import Blueprint, request, jsonify
from controllers.aluno_controller import AlunoController

aluno_bp = Blueprint ('alunos', __name__, url_prefix='/alunos')
