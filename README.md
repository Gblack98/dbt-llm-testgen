# dbt-llm-testgen

This is a learning project. I want to understand if an LLM can write good dbt tests and good documentation, just by looking at the data.

## The idea

I build a small data pipeline with real loan data (Kiva) and financial inclusion data (Findex). I load everything in DuckDB, then I clean and model it with dbt.

For the tests and the docs, I do two versions:
- one that I write myself, by hand
- one that an LLM writes, based only on column stats (nulls, distinct values, min/max)

Then I compare the two. Which tests are correct? Which ones are just noise? That is the real question of this project.

## Stack

- Python for the extraction scripts
- DuckDB as the local warehouse
- dbt for the models and tests
- Airflow to run the pipeline
- Mistral or Groq API for the LLM part

## Status

Early stage. Folders are set up, pipeline is not built yet.

## Folders

- `data/raw` : raw extracted data (not committed)
- `dbt_llm_quality` : the dbt project
- `dags` : Airflow DAGs
- `scripts` : extraction and profiling scripts
- `docs` : notes and project guide

## Setup

More details will come once the pipeline is ready. For now you need:
- Python 3.10+
- Docker (for Airflow, later)
- a free API key from Mistral or Groq

Never commit your API key. It goes in a local `.env` file, which is ignored by git.

## Contributing

Work happens on branches, not directly on `main`. Open a pull request and get it reviewed before merging.
