"""Southampton Airport (SOU) destinations — verified via Google Flights."""

DESTINATIONS = {
    "SOU": {
        "name": "Southampton",
        "routes": {
            "AMS": "Amsterdam",
            "BHD": "Belfast City",
            "DUB": "Dublin",
            "EDI": "Edinburgh",
            "GCI": "Guernsey",
            "GLA": "Glasgow",
            "JER": "Jersey",
            "NCL": "Newcastle",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
