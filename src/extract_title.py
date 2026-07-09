def extract_title(markdown):
    for line in markdown.split('\n'):
        cleaned_line = line.strip()
        if cleaned_line.startswith('#') and not cleaned_line.startswith('##'):
            return cleaned_line[1:].strip()
    raise Exception("No h1 header found.")
