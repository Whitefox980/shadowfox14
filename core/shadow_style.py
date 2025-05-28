def get_headers(style="stealth"):
    base_headers = {
        "X-Chupko-Sign": "ChupkoWasHere",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US",
        "Connection": "close"
    }

    if style == "stealth":
        base_headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        base_headers["X-Stealth-Level"] = "Max"

    elif style == "mimic":
        base_headers["User-Agent"] = "Chrome/119.0.0.0 Safari/537.36"
        base_headers["X-Mimic-Mode"] = "Enabled"

    elif style == "aggressive":
        base_headers["User-Agent"] = "ChupkoBot/1.0"
        base_headers["X-Attack-Mode"] = "Active"
        base_headers["Referer"] = "https://whitefox980.sh"
    
    elif style == "whitelist":
        base_headers["User-Agent"] = "Googlebot"
        base_headers["X-Bypass"] = "true"

    else:
        base_headers["User-Agent"] = "ShadowFox/Probe"

    return base_headers
