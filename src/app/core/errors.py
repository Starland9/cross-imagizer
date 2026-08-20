"""Types d'erreurs du moteur de conversion."""


class ConversionError(Exception):
    """Erreur de conversion avec un message actionnable pour l'utilisateur."""


class UnsupportedFormatError(ConversionError):
    """Format source ou cible non pris en charge."""


class UnreadableImageError(ConversionError):
    """Image source illisible ou corrompue."""


class OutputWriteError(ConversionError):
    """Impossible d'écrire le fichier de sortie."""
