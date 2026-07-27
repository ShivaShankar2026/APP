"""
child_safety_filter.py
A lightweight, free, no-API keyword-based content filter for flagging
comments that are unsafe or inappropriate for children.

Usage (inside userapp/views.py):
    from userapp.child_safety_filter import check_child_safety

    result = check_child_safety(comment_text)
    if result['is_safe']:
        # show comment normally
    else:
        # hide/flag comment, show result['matched_categories'] to admin

This is a FIRST-LINE filter only — it catches obvious cases via keyword
matching. It is not a substitute for a full moderation system, but it's
free, fast, and requires no external API or signup.
"""

import re

# Keyword categories — extend these lists as needed.
# Kept intentionally generic/high-level; add specific terms based on
# your own research into grooming, bullying, and unsafe content patterns.
UNSAFE_KEYWORDS = {
    "bullying": [
        "stupid", "idiot", "ugly", "loser", "fatty", "kill yourself",
        "nobody likes you", "hate you", "worthless",
    ],
    "profanity": [
        # Add explicit profanity terms here as needed for your region/language
    ],
    "violence": [
        "kill", "murder", "stab", "shoot", "weapon", "blood", "gun",
    ],
    "adult_content": [
        "sex", "nude", "naked", "porn", "xxx",
    ],
    "personal_info_request": [
        # Common grooming-pattern phrases requesting personal details
        "what's your address", "send me your number", "where do you live",
        "how old are you", "add me on", "meet me in person",
        "don't tell your parents", "our secret", "keep this between us",
    ],
}


def check_child_safety(text: str) -> dict:
    """
    Scans text against the unsafe keyword categories.

    Returns:
        {
            'is_safe': bool,
            'matched_categories': [list of category names that matched],
            'matched_terms': [list of the specific terms found],
        }
    """
    if not text:
        return {'is_safe': True, 'matched_categories': [], 'matched_terms': []}

    text_lower = text.lower()
    matched_categories = []
    matched_terms = []

    for category, terms in UNSAFE_KEYWORDS.items():
        for term in terms:
            if not term:
                continue
            # word-boundary match to avoid partial-word false positives
            pattern = r'\b' + re.escape(term.lower()) + r'\b'
            if re.search(pattern, text_lower):
                if category not in matched_categories:
                    matched_categories.append(category)
                matched_terms.append(term)

    return {
        'is_safe': len(matched_categories) == 0,
        'matched_categories': matched_categories,
        'matched_terms': matched_terms,
    }


if __name__ == "__main__":
    # Quick manual test
    test_comments = [
        "This video is so much fun, I love it!",
        "You're so stupid, nobody likes you",
        "What's your address? Don't tell your parents we're talking",
        "Great content, thanks for sharing!",
    ]
    for c in test_comments:
        result = check_child_safety(c)
        print(f"'{c}'\n  -> safe={result['is_safe']}, categories={result['matched_categories']}\n")