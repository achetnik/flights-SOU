"""Southampton Airport (SOU) destinations — verified March 2026."""

DESTINATIONS = {
    "SOU": {
        "name": "Southampton",
        "routes": {
            "ACI": "Alderney",
            "ALC": "Alicante",
            "AMS": "Amsterdam",
            "BCN": "Barcelona",
            "BHD": "Belfast City",
            "CDG": "Paris CDG",
            "DUB": "Dublin",
            "EDI": "Edinburgh",
            "FAO": "Faro",
            "GCI": "Guernsey",
            "GLA": "Glasgow",
            "GVA": "Geneva",
            "JER": "Jersey",
            "MAN": "Manchester",
            "NCL": "Newcastle",
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
