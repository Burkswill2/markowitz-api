# markowitz-api

FastAPI service that computes mean-variance-optimal portfolios using the
Markowitz model. Point it at a list of tickers and a date range; it returns
the efficient frontier and the max-Sharpe allocation.

## Endpoint

`POST /markowitz_model/`

```json
{
  "stocks": ["SPY", "TLT", "GLD", "DBC"],
  "start_date": "2020-01-01",
  "end_date": "2024-12-31"
}
```

Returns optimal weights, expected portfolio return, expected volatility,
Sharpe ratio, and the efficient-frontier scatter.

## How it works

- Downloads daily close prices via `yfinance`
- Computes log returns and annualized covariance matrix (252 trading days)
- Generates 10,000 random long-only portfolios to sketch the efficient frontier
- Solves for max-Sharpe allocation via SciPy SLSQP under sum-to-1 and
  non-negativity constraints

The math lives in `app/routers/helpers/markowitz_helper.py`.

## Running locally

```bash
pip install -r app/requirements.txt
uvicorn app.main:app --reload
# → http://localhost:8000/docs for the OpenAPI UI
```

## Stack

Python 3.12 · FastAPI · yfinance · NumPy · SciPy · Pandas · Plotly. Deployable
on Render via `render.yml`.
