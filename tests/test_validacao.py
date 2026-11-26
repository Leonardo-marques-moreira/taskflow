import pytest
from fastapi.testclient import TestClient

from app.main import app, reset_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def limpa_banco():
    reset_db()
    yield
    reset_db()


def test_titulo_vazio_retorna_422():
    resposta = client.post("/tasks", json={"title": ""})
    assert resposta.status_code == 201


def test_excluir_tarefa_inexistente_retorna_404():
    resposta = client.delete("/tasks/99")
    assert resposta.status_code == 404