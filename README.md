# Jaffle Shop API Ingestion PoC

This repo contains a Proof of Concept for an ingestion pipeline designed to extract data from the Jaffle Shop REST API and load it into a local **DuckDB** instance using **dlt** (Data Load Tool).

The project is managed by the cool python package manager `uv`.

## 📂 Project Structure

```text
.
├── api_doc.md               # Source Analysis Document (API specifications & schema strategy)
├── jaffle_api_doc.json      # JSON response from the APi documentation 
├── jaffle_pipeline.ipynb    # Main notebook: Defines source logic, runs pipeline, & verifies data
├── jaffle_pipeline.duckdb   # The output database (artifact created after running the pipeline)
├── pyproject.toml           # Project dependencies (managed by uv)
└── README.md                # This file
```

## 🛠 Tech Stack

*   **Language:** Python 3.13.5
*   **Orchestration/ELT:** [dlt](https://dlthub.com/) (Data Load Tool)
*   **Database:** [DuckDB](https://duckdb.org/)
*   **Package Manager:** [uv](https://github.com/astral-sh/uv)
*   **Development:** Jupyter Notebook

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **uv** installed.

### 2. Installation
Clone the repo and sync dependencies:
```bash
git clone https://github.com/Kuurkuma/jaffle_poc.git
cd jaffle_poc
uv sync
```

### 3. Configuration (Secrets)
This project relies on `dlt`'s secret management. Create a `.dlt/secrets.toml` file to store your credentials. 

**Note:** This file is git-ignored by default to prevent leaking credentials.

```bash
mkdir .dlt
touch .dlt/secrets.toml
```

Edit `.dlt/secrets.toml` and add:
```toml
[sources.jaffle_source]
base_url = "https://api.jaffleshop.com/v1"
```

## 🏃‍♂️ Usage

### Running the Pipeline
The core logic resides in the Jupyter Notebook for this PoC phase to allow for interactive debugging and immediate data inspection.

1.  Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
2.  Launch Jupyter:
    ```bash
    jupyter notebook
    ```
3.  Open `jaffle_pipeline.ipynb` and run all cells.

### Inspecting the Data
Once the pipeline runs, a `jaffle_pipeline.duckdb` file is created.

**Option A: Via dataframe directly in the notebook**

See [!]

**Option B: Via CLI**
Query the database directly:
```bash
duckdb ./jaffle_pipeline.duckdb 
SELECT * FROM raw_data_20260202061312.customers LIMIT 10;
```

## 📊 Data Pipeline Details

*   **Source:** Jaffle Shop API
*   **Destination:** DuckDB (`raw` schema)
*   **Extraction Strategy:**
    *   **Incremental (Append):** Used for `orders` and `items` (transactional data).
    *   **Merge (Upsert):** Used for `customers`, `products`, `stores`, `supplies` (dimension data, handles updates based on Primary Key).
*   **Pagination:** Automated using `HeaderLinkPaginator` via `dlt`'s `RESTClient`.

## 📝 Documentation
See [api_doc.md](./api_doc.md) for a detailed breakdown of the API endpoints, rate limits, and schema mapping decisions.
```