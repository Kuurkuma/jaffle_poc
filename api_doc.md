# Documentation of the Jaffle API

https://github.com/dlt-hub/fast-api-jaffle-shop

This is a FastAPI version of the dbt jaffle shop project. The jaffle shop dataset is copied from dbt jaffle data.

When the API is running, docs are available at /docs. For all entities, there are collection and single entity endpoints to retrieve the data.

- The collection endpoints are paginated and have a limit of 100 items. 
- The link to the next page is returned in the response headers. 
- The orders endpoint includes the order items nested inside each order object.

## Endpoints documentation
https://jaffle-shop.dlthub.com/docs

1. **Authentication & Config**
*   Base URL: `https://jaffle-shop.dlthub.com/api/v1` 
*   Auth Method: no auth method (public APi)
*   Pagination:
    Pagination is controlled via the page query parameter (see page).
    Each page returns a fixed number of results (see page_size).
    If more results are available, the response will include a Link header with rel="next" that points to the next page.
*   Rate Limits: (e.g., 100 requests/minute? 429 Retry-After header?)

**2. Endpoints & Schema Strategy**

| Endpoint Path | Destination Table | Sync Mode | Primary Key | Notes                         |
| :--- | :--- | :--- | :--- | :---  |
| `/customers`  | `customers`       |           |   `id`     | 2 keys: `id`, `name`.          |
| `/orders`     | `orders`          |           |   `id`     | 3 keys: `id`, `order_id`, `sku`|  
| `/items`      | `items`           |           | `item_id`  |                                |
| `/products`   | `products`        |           | `sku`      | Small reference table.         |
| `/supplies`   | `supplies`        |           | `id`       |                                |
| `/stores`     | `stores`          |           | `id`       |"id", "name","opened_at","tax_rate"|
| `/`