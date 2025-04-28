import re

def validate_credit_card(card_number):
    """
    Validates a credit card number and determines its 'bandeira' (brand).
    
    Args:
        card_number (str): The credit card number as a string.
    
    Returns:
        str: The card brand ('Visa', 'MasterCard', 'Elo', 'American Express', 'Discover', 'Hipercard') 
             or 'Invalid' if the card number does not match any brand.
    """
    # Remove spaces or dashes from the card number
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Check if the card number is numeric
    if not card_number.isdigit():
        return "Invalid"

    # Define regex patterns for each card brand
    patterns = {
        "Visa": r"^4\d{12}(\d{3})?$",  # Starts with 4, 13 or 16 digits
        "MasterCard": r"^(5[1-5]\d{14}|2(2[2-9]\d{2}|[3-6]\d{3}|7[01]\d{2}|720)\d{12})$",  # 51-55 or 2221-2720
        "Elo": r"^(4011|4312|4389|4514|4576|5041|5067|5090|6277|6362|6363)\d*$",  # Specific prefixes
        "American Express": r"^3[47]\d{13}$",  # Starts with 34 or 37, 15 digits
        "Discover": r"^(6011\d{12}|65\d{14}|64[4-9]\d{13})$",  # 6011, 65, or 644-649
        "Hipercard": r"^6062\d*$"  # Starts with 6062
    }

    # Match the card number against each pattern
    for brand, pattern in patterns.items():
        if re.match(pattern, card_number):
            return brand

    # If no match, return Invalid
    return "Invalid"

# Example usage
if __name__ == "__main__":
    card_number = input("Enter the credit card number: ")
    brand = validate_credit_card(card_number)
    print(f"Card Brand: {brand}")