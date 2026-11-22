

def matches_notandor(data: str, search: str) -> bool:
    """
    Evaluates a search expression like:
    "word1 word2 OR word3 word4 NOT word5 word6"

    Rules:
    - OR and NOT must be uppercase to be recognized.
    - Groups separated by OR.
    - Each positive group: all terms must be present.
    - Optional NOT group: if any term is present → exclude.

    Empty string or Spaces cannot be found
    """
    data_l = data.lower()
    search_raw = search.strip()

    # 1) Split NOT (uppercase only)
    if " NOT " in search_raw:
        positive_part, not_part = search_raw.split(" NOT ", maxsplit=1)
        not_terms = not_part.split()
    else:
        positive_part = search_raw
        not_terms = []

    # 2) Split OR (uppercase only)
    groups = [g.strip() for g in positive_part.split(" OR ") if g.strip()]

    # 3) Check positive groups: at least one must fully match
    def group_matches(group: str) -> bool:
        terms = group.split()
        return all(term.lower() in data_l for term in terms)

    positive_match = any(group_matches(g) for g in groups)

    # 4) Check NOT terms: if any found → exclude
    negative_hit = any(term.lower() in data_l for term in not_terms)

    return positive_match and not negative_hit

if __name__ == '__main__':
    print ("this is", __name__)
    result = matches_notandor ("this is my title", "his title")
    assert result == True, "no message"
    result = matches_notandor ("this is my title", "his title OR nix")
    assert result == True, "no message"
    result = matches_notandor ("word1 word2 word3", "word3 NOT word4")
    assert result == True, "no message"
    result = matches_notandor ("word1 word2 word3", "word3 NOT word1")
    assert result == False, "no message"
    result = matches_notandor ("word1 word2 word3", "")
    assert result == False, "no message"
    result = matches_notandor ("word1 word2 word3", "  ")
    assert result == False, "no message"