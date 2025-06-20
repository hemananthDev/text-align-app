def align_text(text):
    """
    Simple alignment logic – updates each line to have equal width.
    You can modify this function in the future.
    """
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    aligned_lines = [line.ljust(max_length) for line in lines]
    return '\n'.join(aligned_lines)
