"""The Intro Pipeline Template contains the example from the docs intro page"""

# mypy: disable-error-code="no-untyped-def,arg-type"

from typing import Optional
import pandas as pd
import sqlalchemy as sa

import dlt
from dlt.sources.helpers import requests


def load_api_data() -> None:
    """Load data from the chess api, for more complex examples use our rest_api source"""

    # Create a dlt pipeline that will load
    # chess player data to the DuckDB destination
    pipeline = dlt.pipeline(
        pipeline_name="chess_pipeline", destination='duckdb', dataset_name="player_data"
    )
    # Grab some player data from Chess.com API
    data = []
    for player in ["magnuscarlsen", "rpragchess"]:
        response = requests.get(f"https://api.chess.com/pub/player/{player}")
        response.raise_for_status()
        data.append(response.json())

    # Extract, normalize, and load the data
    load_info = pipeline.run(data, table_name="player")
    print(load_info)  # noqa: T201



@dlt.resource(write_disposition="replace")
def github_api_resource(api_secret_key: Optional[str] = dlt.secrets.value):
    from dlt.sources.helpers.rest_client import paginate
    from dlt.sources.helpers.rest_client.auth import BearerTokenAuth
    from dlt.sources.helpers.rest_client.paginators import HeaderLinkPaginator

    url = "https://api.github.com/repos/dlt-hub/dlt/issues"

    # Github allows both authenticated and non-authenticated requests (with low rate limits)
    auth = BearerTokenAuth(api_secret_key) if api_secret_key else None
    for page in paginate(
        url, auth=auth, paginator=HeaderLinkPaginator(), params={"state": "open", "per_page": "100"}
    ):
        yield page


@dlt.source
def github_api_source(api_secret_key: Optional[str] = dlt.secrets.value):
    return github_api_resource(api_secret_key=api_secret_key)


def load_data_from_source():
    pipeline = dlt.pipeline(
        pipeline_name="github_api_pipeline", destination='duckdb', dataset_name="github_api_data"
    )
    load_info = pipeline.run(github_api_source())
    print(load_info)  # noqa: T201


if __name__ == "__main__":
    load_api_data()
    load_pandas_data()
    load_sql_data()
