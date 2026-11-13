# News Headline Fetcher

A lightweight Python command-line application by Omar Shemis that fetches news headlines from NewsAPI by country and category. Each result includes the article title and a link to the original story.

## Features

- Interactive country and category selection.
- Numbered article titles with links to the original stories.
- Messages for empty results and errors returned by the API.
- Local API-key configuration through environment variables.

## Requirements

- Python 3.13 or newer
- A NewsAPI key
- An internet connection
- uv (for the setup commands below)

## Getting started

Run these commands from the project folder.

1. Install the project dependencies:

   ```sh
   uv sync --locked
   ```

2. Copy the example configuration to a local `.env` file.

   PowerShell:

   ```powershell
   Copy-Item .env.example .env
   ```

   macOS / Linux:

   ```sh
   cp .env.example .env
   ```

   If you already have a configured `.env`, keep that file instead of replacing it.

3. Open `.env` and replace the placeholder with your own key:

   ```dotenv
   API_KEY=your_newsapi_key_here
   ```

4. Start the app:

   ```sh
   uv run main.py
   ```

Enter a country code and a category when prompted. The app prints article titles and URLs, reports when no articles are found, or displays the API's error message.

## Project structure

```text
News Headline Fetcher/
|-- docs/
|   `-- usage.md      # Detailed usage and current limitations
|-- main.py           # Application entry point
|-- pyproject.toml    # Project metadata and dependencies
|-- uv.lock           # Locked dependency versions
|-- .python-version  # Python version for local tooling
|-- .env.example     # Configuration template without credentials
|-- .gitignore       # Local files excluded from Git
`-- README.md        # Setup and usage instructions
```

The local `.env`, virtual environment, editor settings, and tool caches are excluded from Git. Keep your actual API key in `.env`; share only `.env.example`.

The single-file application stays at the root for straightforward execution. See the [usage guide](docs/usage.md) for examples and current limitations.

## Dependencies

- `requests` sends the HTTP request.
- `python-dotenv` loads the API key from `.env`.

## Troubleshooting

- **Missing API key:** Check that `.env` contains `API_KEY` with a value and sits in the project folder.
- **API error:** Read the message printed by the app and check your key and request inputs.
- **No articles found:** Try a different country or category combination.
