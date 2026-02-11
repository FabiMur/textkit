import re

# Matches standard email addresses.
# Format: username@domain.tld
EMAIL_RE = re.compile(
    r"""
    (?<!\w)
    [a-zA-Z0-9._%+-]+   # Username
    @
    [a-zA-Z0-9.-]+      # Domain
    \.[a-zA-Z]{2,}      # TLD
    (?!\w)
    """,
    re.VERBOSE,
)

# Matches URLs with optional scheme, www and resource path.
# Format: [scheme://][www.]domain.tld[/path]
URL_RE = re.compile(
    r"""
    (?<!\w)
    (
        (?:https?://)?        # Optional scheme
        (?:www\.)?            # Optional www
        [a-zA-Z0-9.-]+        # Domain
        \.[a-zA-Z]{2,}        # TLD
        (?:/[^\s]*)?          # Optional resource path
    )
    (?!\w)
    """,
    re.VERBOSE,
)

# Matches European date formats
# Format: DD/MM/YYYY, DD-MM-YYYY, DD.MM.YYYY
DATE_EU_RE = re.compile(
    r"""
    (?<!\w)
    (
        (?:0?[1-9]|[12][0-9]|3[01]) # Day 1-31
        [\./-]                      # Separator
        (?:0?[1-9]|1[0-2])          # Month
        [\./-]                      # Separator
        \d{4}                       # Year
    )
    (?!\w)
    """,
    re.VERBOSE,
)

# Matches phone numbers with country code and exactly 9 digits.
# Format: [+][country code][number]
PHONE_EU_RE = re.compile(
    r"""
    (?<!\w)                       # Ensure pattern is not preceded by a word character
    (
        (?:\+\d{1,3}[\s-]?)?      # Optional +country code
        (?:\d[\s-]?){8}\d         # 9-digit number with optional separators
    )
    (?!\w)                        # Ensure pattern is not followed by a word character
    """,
    re.VERBOSE,
)
