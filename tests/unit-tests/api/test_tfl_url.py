import pytest
from api.tfl_url import base_tfl_url, VALID_LINES


# TODO: tests required - one line, multiple lines, invalid lines, capitalised lines, no lines
def get_test_base_url(given_lines: list[str]) -> str:
    return f"https://api.tfl.gov.uk/Line/{",".join(given_lines)}/Disruption"


@pytest.mark.parametrize("input_lines,expected_lines",
                         [
                             (["bakerloo"], ["bakerloo"]),
                             (["victoria", "central"], ["victoria", "central"])
                         ])
def test_base_tfl_url_valid_lines(input_lines: list[str], expected_lines: list[str]):
    output_url = base_tfl_url(input_lines)
    assert output_url == get_test_base_url(expected_lines)


@pytest.mark.parametrize("input_lines",
                         [
                             (["OH_NO_INVALID_LINE"]),
                             (["victoria", "CeNtRal"])
                         ])
def test_base_tfl_url_invalid_lines(input_lines: list[str]):
    with pytest.raises(Exception) as err:
        base_tfl_url(input_lines)
    assert err.value.args[0] == f"Some of the lines given are invalid. Here are the valid lines {VALID_LINES}"


def test_base_tfl_url_no_lines():
    with pytest.raises(Exception) as err:
        base_tfl_url([])
    assert err.value.args[0] == "No lines provided"


def test_base_tfl_url_lines_null():
    with pytest.raises(Exception) as err:
        base_tfl_url()
    assert err.value.args[0] == "No lines provided"
