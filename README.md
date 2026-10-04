# dbt-llm-testgen

This is a learning project. We want to know if an LLM can write good dbt tests and good docs, just by looking at the data.

## The idea

We build a small data pipeline with real loan data from Kiva. We load it in DuckDB, then clean and model it with dbt.

For the tests and the docs, we do two versions:
- one written by hand
- one written by an LLM, based only on column stats (nulls, distinct values, min/max)

Then we compare the two. Which tests are correct? Which ones are just noise? That is the real question here.

Findex data may come later as an extra, once the Kiva pipeline works well. Not needed for now.

## Stack

- Python for the extraction scripts
- DuckDB as the local warehouse
- dbt for the models and tests
- Airflow to run the pipeline
- Mistral API, with free OpenRouter models as backup when rate limited

## Status

Early stage. Folders are set up, pipeline is not built yet.

## Folders

- `data/raw` : raw extracted data (not committed)
- `dbt_llm_quality` : the dbt project
- `dags` : Airflow DAGs
- `scripts` : extraction, profiling, and LLM scripts
- `docs` : project notes

## Setup

More details come once the pipeline is ready. For now, you need:
- Python 3.10+
- Docker (for Airflow, later)
- a free API key from Mistral, and one from OpenRouter

Never commit an API key. It goes in a local `.env` file, ignored by git.

## Contributing

Work happens on branches, not directly on `main`. Open a pull request and get it reviewed before merging.
