"""
Korean Minimalist Aesthetic Design Tokens
Extracted from the master Korean exhibition presentation.
"""

# Color Palette (Gamseong Minimalist)
BG_IVORY = "#F8F6F2"        # Warm ivory / paper cream canvas
TEXT_DARK = "#1F1F1F"       # Charcoal black (high contrast headers)
TEXT_MOCHA = "#7D6652"      # Warm earthy taupe (secondary title split & badges)
TEXT_BODY = "#3E3E3E"       # Crisp dark grey for body copy
TEXT_MUTED = "#6A6A6A"      # Slate grey for subtitles and captions

# Background Pastel Blobs (Layered gouache/watercolor accents)
BLOB_TERRACOTTA = "#F4DDD6" # Soft blush / peachy terracotta (~46% alpha)
BLOB_SAGE = "#D9DDD6"       # Muted sage / olive slate (~30% alpha)
BLOB_SAND = "#EFECE6"       # Oatmeal / warm stone (~50% alpha)
BLOB_WARM_SHADOW = "#F2EBE5"# Warm taupe shadow (~13% alpha)
CONTOUR_LINE = "#C48D80"    # Delicate 1.5px organic curved line art

# Pebble Badge Palettes (Curved asymmetrical badges)
PEBBLES = [
    {
        "id": "01",
        "name": "Sage",
        "bg": "#DDE2D8",
        "text": "#4A5445",
        "border": "#CBD3C4"
    },
    {
        "id": "02",
        "name": "Blush",
        "bg": "#F5E5E0",
        "text": "#80524B",
        "border": "#E8D0C9"
    },
    {
        "id": "03",
        "name": "Warm Stone",
        "bg": "#EAE6E0",
        "text": "#5E5B55",
        "border": "#DDD6CD"
    },
    {
        "id": "04",
        "name": "Oat Sand",
        "bg": "#F0EAE1",
        "text": "#736756",
        "border": "#E2D9CC"
    },
    {
        "id": "05",
        "name": "Clay",
        "bg": "#EDE0D4",
        "text": "#6D5344",
        "border": "#DECBC0"
    },
    {
        "id": "06",
        "name": "Slate",
        "bg": "#E1E6E8",
        "text": "#475960",
        "border": "#CFD9DC"
    }
]

# Typography & Spacing
FONT_HEADING = "Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
FONT_BODY = "Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
BORDER_RADIUS_PEBBLE = "48% 52% 54% 46% / 46% 54% 46% 54%"
BORDER_RADIUS_CARD = "18px"
