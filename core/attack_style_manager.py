def choose_attack_style():
    # Može se proširiti na osnovu meta, ranijih rezultata, AI logike...
    styles = {
        "loud": {
            "description": "Brutalan napad sa ogromnim brojem zahteva",
            "rate_limit": 100,
            "detection_risk": "high"
        },
        "stealth": {
            "description": "Diskretan napad sa razmakom između zahteva",
            "rate_limit": 5,
            "detection_risk": "low"
        },
        "hybrid": {
            "description": "Izbalansiran pristup",
            "rate_limit": 30,
            "detection_risk": "medium"
        }
    }

    # Za sad hardkodirano, kasnije AI neka bira na osnovu meta ponašanja
    chosen = "hybrid"

    return chosen, styles[chosen]
