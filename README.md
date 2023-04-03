# Markdown Translator

This Python script translates Markdown files from one language to English using the OpenAI GPT-3.5 API.

## Prerequisites

To use this script, you will need:

- An OpenAI API key.
- Markdown files that you would like to translate.
- Python 3 installed on your system.

## Installation

1. Clone this repository to your local machine.
`git clone git@github.com:steveyiyo/TranslateMD.git`
2. Install `pipenv` by running `pip install pipenv` in the terminal.
3. Navigate to the root directory of the project in the terminal.
4. Run `pipenv install` to install the required packages specified in the Pipfile.
5. Create a .env file in the root directory of the project and add your OpenAI API key, source path (where your Markdown files are located), and new path (where the translated files will be saved) as environment variables. For example:

```
OPENAI_API_KEY=your_api_key_here
SOURCE_PATH=/path/to/source/folder
NEW_PATH=/path/to/new/folder
```

## Usage

1. Run the script by executing `pipenv run python app.py` in the terminal.
2. The script will read all Markdown files in the source path, translate them to English, and save them to the new path.
3. The translated files will have the same name as the original files.

Note: This README.md was generated by ChatGPT.