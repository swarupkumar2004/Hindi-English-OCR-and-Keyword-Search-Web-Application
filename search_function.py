import re

def highlight_text(text, keyword):
    # Escape special characters in keyword
    keyword = re.escape(keyword)
    
    # Use regex to highlight the keyword in the text
    highlighted_text = re.sub(f"({keyword})", r"<mark>\1</mark>", text, flags=re.IGNORECASE)
    
    return highlighted_text
