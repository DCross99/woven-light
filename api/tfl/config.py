
def base_tfl_url(lines: list | None = None) -> str:
    if lines is None or len(lines) == 0:
        raise (Exception("ERROR NO LINES GIVEN"))
    base_url = f"https://api.tfl.gov.uk/Line/{lines}/Disruption"
    return base_url

