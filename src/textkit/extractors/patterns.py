# Matches standard email addresses.
# Format username@domain.tld
EMAIL_PATTERN = r"""
(?<!\w)
[a-zA-Z0-9._%+-]+   # Username
@
[a-zA-Z0-9.-]+      # Domain
\.[a-zA-Z]{2,}      # TLD
(?!\w)
"""


# Matches URLs with optional scheme, www and resource path.
# Format [scheme://][www.]domain.tld[/path]
URL_PATTERN = r"""
(?<!\w)
(
    (?:https?://)?        # Optional scheme
    (?:www\.)?            # Optional www
    [a-zA-Z0-9.-]+        # Domain
    \.[a-zA-Z]{2,}        # TLD
    (?:/[^\s]*)?          # Optional resource path
)
(?!\w)
"""


# Matches European date formats
# Format DD/MM/YYYY, DD-MM-YYYY, DD.MM.YYYY
DATE_EU_PATTERN = r"""
(?<!\w)
(
    (?:0?[1-9]|[12][0-9]|3[01])  # Day 1-31
    [\./-]                      # Separator
    (?:0?[1-9]|1[0-2])          # Month
    [\./-]                      # Separator
    \d{4}                       # Year
)
(?!\w)
"""


# Matches phone numbers with country code and exactly 9 digits.
# Format [+][country code][number]
PHONE_EU_PATTERN = r"""
(?<!\w)                       # Not preceded by word character
(
    (?:\+\d{1,3}[\s-]?)?      # Optional +country code
    (?:\d[\s-]?){8}\d         # 9-digit number with optional separators
)
(?!\w)                        # Not followed by word character
"""
