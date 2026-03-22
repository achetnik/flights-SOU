"""Southampton Airport (SOU) destinations."""

DESTINATIONS = {
    "SOU": {
        "name": "Southampton",
        "routes": {
            "AGP": "Malaga",
            "ALC": "Alicante",
            "AMS": "Amsterdam",
            "BER": "Berlin",
            "CDG": "Paris CDG",
            "DUB": "Dublin",
            "EDI": "Edinburgh",
            "FAO": "Faro",
            "GCI": "Guernsey",
            "GLA": "Glasgow",
            "JER": "Jersey",
            "PMI": "Palma",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
