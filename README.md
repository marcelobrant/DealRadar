# DealRadar

DealRadar is a Python-based marketplace monitoring project for finding, tracking, and analyzing deals.

## Project structure

```
DealRadar/
├── src/
│   └── dealradar/
│       ├── __init__.py
│       ├── config.py
│       ├── models.py
│       ├── monitor.py
│       └── utils.py
├── tests/
│   └── test_monitor.py
├── data/
│   └── .gitkeep
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting started

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run tests with:

```bash
python -m pytest
```

## Development

Keep application code under `src/dealradar/`, tests under `tests/`, and local/generated data under `data/`.
Do not commit secrets, credentials, virtual environments, caches, or generated marketplace data.
