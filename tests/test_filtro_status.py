import pytest
from fastapi.testclient import TestClient

from app.main import app, reset_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def limpa_banco():
    reset_db()
    yield
    reset_db()


def test_filtra_por_status():
    client.post("/tasks", json={"title": "Feita", "done": True})
    client.post("/tasks", json={"title": "Pendente", "done": False})
    resposta = client.get("/tasks", params={"done": "true"})
    assert resposta.status_code == 200
    assert [t["title"] for t in resposta.json()] == ["Feita"]


def test_sem_filtro_lista_tudo():
    client.post("/tasks", json={"title": "Feita", "done": True})
    client.post("/tasks", json={"title": "Pendente", "done": False})
    resposta = client.get("/tasks")
    assert len(resposta.json()) == 2