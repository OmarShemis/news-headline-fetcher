# Usage guide

Run commands from the repository root so the local `.env` is available.

## Configuration

1. Install Python 3.13 or newer and [uv](https://docs.astral.sh/uv/).
2. Run `uv sync --locked`.
3. Copy `.env.example` to `.env` and set `API_KEY` to your NewsAPI key.
4. Run `uv run main.py`.
5. Enter a country code and category at the prompts.

Example input:

```text
Enter country code (exemple: us, jp, eg): us
Enter category code (exemple: technology, sports, business): technology
```

Results contain numbered article titles and links. Availability depends on NewsAPI coverage and your account. Check the [endpoint documentation](https://newsapi.org/docs/endpoints/top-headlines) for supported inputs and account restrictions.

## Troubleshooting

| Result | What to check |
| --- | --- |
| API error message | API key, account limits, country, and category |
| No articles found | Try another supported country/category combination |
| Connection error | Internet access and service availability |
| Configuration issue | Ensure `.env` contains `API_KEY` and run from the repository root |

## Current scope

This is a lightweight interactive script. It does not currently implement input validation, request timeouts, retries, or handling for network failures and invalid JSON. Errors returned by the API are displayed when the HTTP status is not 200.

Keep your actual API key private. `.env.example` is a template; `.env` is excluded from version control.
