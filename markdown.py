def convert_markdown_to_text(file_path):
    # read Markdown File
    with open(file_path, 'r') as f:
        text = f.read()

    # convert Markdown to text and return
    return text