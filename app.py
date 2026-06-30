def calculate_total(price: float, tax_rate: float) -> float:
    if price < 0 or tax_rate < 0:
        raise ValueError("Values must be non-negative")
    return price + (price * tax_rate)