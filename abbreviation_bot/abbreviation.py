abbreviations = {
    "imo": "In my opinion",
    "tbh": "To be honest",
    "http": "Hypertext Transfer Protocol",
    "404": "Not Found"
}

def find_all():
    abbr_string = ""
    for abbr, description in abbreviations.items():
        abbr_string += f"{abbr.upper()}: {description}\n"

    return abbr_string

def find(abbr):
    abbr = abbr.lower()

    if abbr in abbreviations:
        return f"{abbr.upper()}: {abbreviations[abbr]}"
    else:
        return f"Abbreviation {abbr.upper()} was not found"