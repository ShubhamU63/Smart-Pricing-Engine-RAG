
VAT_RATES = {
    "FR": 0.20,  # France
    "DE": 0.19,  # Germany
    "UK": 0.20,  # United Kingdom
    "ES": 0.21,  # Spain
}

def get_vat_rate(country_code: str) -> float:
    """
    Get the VAT rate for a given country code.
    Defaults to 20% if not found.
    """
    return VAT_RATES.get(country_code.upper(), 0.20)