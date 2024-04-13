from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Reservation creation
def test_create_reservation():
    # Payload
    reservation_data = {
        "room_name": "Room 1",
        "booker_name": "Filippo Leonelli",
        "date": "2024-04-13",
        "number_of_people": 3
    }

    response = client.post("/reservations/", json=reservation_data)

    assert response.status_code == 200
    assert response.json()["room_name"] == reservation_data["room_name"]
    assert response.json()["booker_name"] == reservation_data["booker_name"]
    assert response.json()["date"] == reservation_data["date"]
    assert response.json()["number_of_people"] == reservation_data["number_of_people"]

# Test della lettura di tutte le prenotazioni
def test_read_reservations():
    # Effettua la chiamata API per leggere tutte le prenotazioni
    response = client.get("/reservations/")
    # Verifica che la chiamata sia andata a buon fine e che i dati restituiti siano una lista
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test della cancellazione di una prenotazione
def test_delete_reservation():
    # Effettua la chiamata API per cancellare una prenotazione che esiste
    response = client.delete("/reservations/1")
    # Verifica che la chiamata sia andata a buon fine e che i dati restituiti siano corretti
    assert response.status_code == 200
    assert response.json()["ok"] == True

    # Effettua la chiamata API per cancellare una prenotazione che non esiste
    response = client.delete("/reservations/999")
    # Verifica che la chiamata restituisca un errore 404
    assert response.status_code == 404
