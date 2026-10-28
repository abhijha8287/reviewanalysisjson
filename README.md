# Review Analysis (JSON Schema)

A Streamlit app that turns a free-text review into structured fields defined by a JSON Schema.

## Why this exists
Third of three versions exploring LangChain structured output. This one uses a plain JSON Schema dictionary instead of a Pydantic model. See also [review-analysis](https://github.com/abhijha8287/review-analysis) and [reviewanalysis2](https://github.com/abhijha8287/reviewanalysis2).

## What it does
- Takes a product or service review
- Returns themes, summary, sentiment, pros, cons and reviewer name
- Restricts sentiment to `pos` or `neg` with an enum and treats some fields as optional

## Project structure
```
reviewanalysisjson/
├── jsonschema.py     Streamlit app and JSON schema
└── requirements.txt  Python dependencies
```

## Getting started
Requirements: Python 3.10+, an OpenAI API key.
```bash
git clone https://github.com/abhijha8287/reviewanalysisjson.git
cd reviewanalysisjson
pip install -r requirements.txt streamlit
mkdir -p .streamlit && echo 'api_key = "sk-..."' > .streamlit/secrets.toml
streamlit run jsonschema.py
```

## Configuration
| Variable | Purpose |
|:--|:--|
| `api_key` in `.streamlit/secrets.toml` | OpenAI API key |

## Tech stack
Python, LangChain, OpenAI GPT-4, Streamlit

## Notes
Live demo: https://reviewanalysisbyabhishek.streamlit.app (on the free Streamlit tier it may take a few seconds to wake up). `requirements.txt` lists more LangChain integrations than the app uses; only OpenAI is needed.
