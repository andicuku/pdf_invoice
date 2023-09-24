import re

from dateutil import parser


def extract_regex_value(text: str, regexes: list[str], group: int = None, flags=0):
    """
    Use the list of regexes to extract a value from a text.
    Return first match.

    Args:
        text: The text from which to extract the data
        regexes: A list of regex patterns to use for the extraction of information
        group: If None, return the entire matched value, otherwise extract the given group
        flags: Flags to be used for the regexes
    """
    for regex in regexes:
        try:
            match = re.search(regex, text, flags=flags)
            if group is None:
                return match.group()
            else:
                return match.group(group)
        except AttributeError:
            pass


def safe_float(text: str):
    text = text.replace(".", "").replace(",", ".")
    try:
        return float(text)
    except ValueError:
        return


def extract_spv(text: str):
    spv_patterns = [r"(.*\bSPV\b.*)"]
    spv = extract_regex_value(text, regexes=spv_patterns)
    if spv:
        return spv.split('SPV')[-1]


def extract_address(text: str):
    via_lines = re.findall(r'.*Via.*', text)
    if via_lines:
        return "Via" + via_lines[0].split("Via")[-1]

    address_lines = re.findall(r'.*Address.*', text)
    if address_lines:
        return "Address" + address_lines[0].split("Address")[-1]

    street_lines = re.findall(r'.*Street.*', text)
    if street_lines:
        return "Street" + street_lines[0].split("Street")[-1]


def extract_description(text):
    # taking an assumption that fee is always in the description
    return extract_regex_value(text, regexes=[r'(.*?) fee.*?(\b2023\b)'])


def extract_date(text: str) -> str:
    date_regex = [
        "Data \d{1,2}\/\d{1,2}\/\d{4}"
        "\d{1,2}\/\d{1,2}\/\d{4}",
        "\d{1,2}\-\d{1,2}\-\d{4}",
        "Invoice Date \d{1,2}\-\d{1,2}\-\d{4}",
        "\d{1,2}\.\d{1,2}\.\d{4}",
        "\d{1,2}\/\d{1,2}\/\d{2}",
        "\d{1,2}\-\d{1,2}\-\d{2}",
        "\d{1,2}\.\d{1,2}\.\d{2}",
        "\d{4}\/\d{1,2}\/\d{1,2}",
        "\d{4}\-\d{1,2}\-\d{1,2}",
        "\d{4}\.\d{1,2}\.\d{1,2}",
        "\w+\s\d{4}",
        "\w+\s\d{2}",
        "\w+\s\d{1,2}",
        "\w+\s\d{1,2}\,\s\d{4}",
        "\w+\s\d{1,2}\,\s\d{2}",
    ]
    date = extract_regex_value(text, date_regex, group=0)
    if date:
        return str(parser.parse(date).date())


def extract_total(text: str, position: int) -> float | None:
    amount_pattern = r'\b\d{1,3}(?:[,.]\d{3})*(?:,\d{2})?\b'
    amounts = set(re.findall(amount_pattern, text))
    amounts = sorted([safe_float(amount) for amount in amounts if safe_float(amount) is not None], reverse=True)
    try:
        return amounts[position]
    except IndexError:
        return


def dump_dict_to_excel(data: dict, filename: str):
    """Dump dictionary to Excel file"""
    import pandas as pd
    df = pd.DataFrame(data, index=[0])
    df.to_excel(filename, index=False)
