import secrets
from math import log2
from enum import IntEnum

# Enumerācija, kas reprezentē paroles stipruma līmeņus un to attiecīgās entropijas vērtības.
class StrengthToEntropy(IntEnum):
    Weak = 0
    Good = 30
    Strong = 50
    Powerful = 70

# Ģenerē jaunu nejaušu paroli ar norādīto garumu, izmantojot dotos simbolus.
def create_new(length: int, characters: str) -> str:
    return "".join(secrets.choice(characters) for _ in range(length))

# Aprēķina paroles entropiju, pamatojoties uz tās garumu un iespējamo simbolu skaitu.
def get_entropy(length: int, character_number: int) -> float:
    try:
        entropy = length * log2(character_number)
    except ValueError:
        return 0.0

    return round(entropy, 2)