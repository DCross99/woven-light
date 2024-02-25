# TODO: Fill these out with all valid lines (TFL API gave non-valid response when trying to figure out this)
VALID_LINES = ["bakerloo", "jubilee", "central", "victoria"]


def base_tfl_url(lines: list[str] | None = None) -> str:
    if lines is None or len(lines) == 0:
        raise Exception("No lines provided")

    valid_lines = [line for line in lines if line in VALID_LINES]
    if len(lines) != len(valid_lines):
        raise Exception(f"Some of the lines given are invalid. Here are the valid lines {VALID_LINES}")

    base_url = f"https://api.tfl.gov.uk/Line/{",".join(valid_lines)}/Disruption"
    return base_url
