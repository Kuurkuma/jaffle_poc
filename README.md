# Steps

1. API indentification
    obsere the Jaffle endpoints & create a documentation

2. Ingestion
    createt the ingestion client using dlt pipeline from rest api sources

3. Transformation
***where the fun begins****: 
- check data type and modify accordingly
- normalise data by flaten dictionnary and list into child table and create a relevant database schema

4. Loading
based on the schema, choosing the right ingestion methodology (append, merge...)

5. Storage 
build SQL data validation in the duckdb database

6. Deployment
- build the cloud infrastructure (motherduck, GCP cloud storage,bigquery, cloud functions...) using Terraform
- store secrets and credentials in vault like Bitwarden or GitHub secrets
- push to version control (gitHub)
- create  CI/CD pipeline using GitHub Actions to automate the ingestion pipeline. It could also run in Cloud function if needs of more compute.
