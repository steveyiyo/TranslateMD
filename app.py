import os
import openai
import markdown

apiKey = os.getenv("OPENAI_API_KEY")
source_path = os.getenv("SOURCE_PATH")
new_path = os.getenv("NEW_PATH")

# Read the Markdown file and convert it to text.
i = 0
for filename in os.listdir(source_path):
    total_posts = len(os.listdir(source_path))
    i += 1

    if filename.endswith('.md'):
        file_path = os.path.join(source_path, filename)
        markdown_content = markdown.convert_markdown_to_text(file_path)
        translate_result = openai.complete_chat(apiKey, markdown_content)

        # Create a new Markdown file.
        new_file_path = os.path.join(new_path, filename)
        with open(new_file_path, 'w') as f:
            f.write(translate_result)

        print(f'({i}/{total_posts}) Translate Completed! {filename}')
