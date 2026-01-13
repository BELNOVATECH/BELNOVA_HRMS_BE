from num2words import num2words
from decimal import Decimal


def amount_to_words(amount: Decimal | float) -> str | None:
    if amount is None:
        return None

    words = num2words(amount, to="currency", lang="en_IN")
    return (
        words.replace("Rupees,", "Rupees")
        .replace("Paise,", "Paise")
        .replace("and", "")
        .strip()
        + " Only"
    )
