from mcp.server.fastmcp import FastMCP
import json
import os

mcp = FastMCP(name="flights")

FLIGHTS_PATH = os.path.join(os.path.dirname(__file__), "flights.json")

def _load_flights():
    with open(FLIGHTS_PATH, "r", encoding="utf-8") as f:
        return json.load(f).get("flights", [])

FLIGHTS_DATA = _load_flights()

@mcp.resource("flights://data")
def get_flights_resource() -> str:
    """Resource exposant toutes les données des vols"""
    with open(FLIGHTS_PATH, "r", encoding="utf-8") as f:
        return f.read()

@mcp.tool()
def find_flight(flight_number: str) -> str:
    """Trouve un vol par son numéro"""
    for flight in FLIGHTS_DATA:
        if flight["flight_number"].upper() == flight_number.upper():
            return f"Vol {flight['flight_number']} - {flight['airline']} - {flight['departure_city']} vers {flight['arrival_city']} - Départ: {flight['departure_time']} - Statut: {flight['status']}"
    return f"Vol {flight_number} non trouvé"

@mcp.tool()
def flights_to(destination: str) -> str:
    """Liste les vols vers une destination"""
    matches = [f for f in FLIGHTS_DATA if destination.lower() in f["arrival_city"].lower()]
    if not matches:
        return f"Aucun vol vers {destination}"
    result = f"Vols vers {destination}:\n"
    for f in matches:
        result += f"{f['flight_number']} - {f['airline']} - Départ: {f['departure_time']} - {f['status']}\n"
    return result

@mcp.tool()
def flights_by_status(status: str) -> str:
    """Filtre les vols par statut (ex: 'À l'heure', 'Retardé', 'Annulé')"""
    matches = [f for f in FLIGHTS_DATA if status.lower() in f["status"].lower()]
    if not matches:
        return f"Aucun vol avec le statut '{status}'"
    result = f"Vols avec statut '{status}' ({len(matches)} trouvé(s)):\n"
    for f in matches:
        result += f"{f['flight_number']} - {f['airline']} - {f['departure_city']} → {f['arrival_city']} - Départ: {f['departure_time']}\n"
    return result

@mcp.tool()
def get_flight_statistics() -> str:
    """Calcule des statistiques sur les vols (nombre total, par compagnie, par statut)"""
    total = len(FLIGHTS_DATA)
    
    # Statistiques par compagnie
    airlines = {}
    for f in FLIGHTS_DATA:
        airline = f["airline"]
        airlines[airline] = airlines.get(airline, 0) + 1
    
    # Statistiques par statut
    statuses = {}
    for f in FLIGHTS_DATA:
        status = f["status"]
        statuses[status] = statuses.get(status, 0) + 1
    
    result = f"📊 Statistiques des vols:\n\n"
    result += f"Total de vols: {total}\n\n"
    result += "Par compagnie:\n"
    for airline, count in airlines.items():
        result += f"  • {airline}: {count} vol(s)\n"
    result += "\nPar statut:\n"
    for status, count in statuses.items():
        result += f"  • {status}: {count} vol(s)\n"
    
    return result

if __name__ == "__main__":
    mcp.run()
