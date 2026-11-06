def search_by_category(items, category):
    return [dvd for dvd in items if dvd.category == category]


def search_by_title(items, keyword):
    """Return DVDs whose titles contain keyword."""
    return [dvd for dvd in items if keyword in dvd.title]