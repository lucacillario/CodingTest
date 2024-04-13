from fastapi.testclient import TestClient
from main import app

import uuid

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

    response = client.get("/reservations/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_reservations_by_name():
    unique_name = f"Booker_{uuid.uuid4()}"

    reservation_data_1 = {
        "room_name": "Room 1",
        "booker_name": unique_name,
        "date": "2024-04-13",
        "number_of_people": 3
    }
    reservation_data_2 = {
        "room_name": "Room 2",
        "booker_name": unique_name,
        "date": "2024-04-14",
        "number_of_people": 2
    }
    reservation_data_3 = {
        "room_name": "Room 3",
        "booker_name": "Filippo Leonelli",
        "date": "2024-04-15",
        "number_of_people": 4
    }

    # Post the reservations
    client.post("/reservations/", json=reservation_data_1)
    client.post("/reservations/", json=reservation_data_2)
    client.post("/reservations/", json=reservation_data_3)

    # Find by name 'Filippo Leonelli'
    response = client.post("/reservations/by-name", json={"booker_name": unique_name})
    assert response.status_code == 200
    results = response.json()
    
    # Check if we get 2 reservations
    assert len(results) == 2
    assert all(reservation["booker_name"] == unique_name for reservation in results)

    assert results[0]["room_name"] in ["Room 1", "Room 2"]
    assert results[1]["room_name"] in ["Room 1", "Room 2"]
    assert results[0]["date"] in ["2024-04-13", "2024-04-14"]
    assert results[1]["date"] in ["2024-04-13", "2024-04-14"]


def test_delete_reservation():
    # Create a reservation to be deleted
    reservation_data = {
        "room_name": "Room 1",
        "booker_name": "Filippo Leonelli",
        "date": "2024-04-13",
        "number_of_people": 3
    }
    response = client.post("/reservations/", json=reservation_data)
    reservation_id = response.json()["id"]

    # Delete the reservation
    response = client.delete(f"/reservations/{reservation_id}")
    assert response.status_code == 200
    assert response.json()["ok"] == True

    # Verify deletion
    response = client.delete(f"/reservations/{reservation_id}")
    assert response.status_code == 404
