def align_text(text):
    """
    Cleans and aligns all lines: removes extra spaces and pads to max length.
    """
    lines = text.splitlines()
    # Remove empty lines and trim each line
    cleaned = [line.strip() for line in lines if line.strip()]
    max_len = max((len(line) for line in cleaned), default=0)
    # Align all lines to same width
    aligned = [line.ljust(max_len) for line in cleaned]
    return '\n'.join(aligned)
