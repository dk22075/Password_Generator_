from string import ascii_lowercase, ascii_uppercase, digits, punctuation

from enum import Enum

# Enumerators, kas definē simbolu kopas dažādiem pogu kategorijām.
class Characters(Enum):
    button_upper = ascii_uppercase
    button_lower = ascii_lowercase
    button_digits = digits
    button_symbols = punctuation

# Vārdnīca, kurā poga identifikatori atbilst to attiecīgajām simbolu kopām pēc garuma.
CHARACTER_NUMBER = {
    'button_lower': len(Characters.button_lower.value),
    'button_upper': len(Characters.button_upper.value),
    'button_digits': len(Characters.button_digits.value),
    'button_symbols': len(Characters.button_symbols.value)
}

# Kortežs, kas satur pogu identifikatorus, kas saistīti ar paroles ģenerēšanu.
GENERATE_PASSWORD = (
    'button_refresh', 'button_lower', 'button_upper', 'button_digits', 'button_symbols'
)