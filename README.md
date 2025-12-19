# Personal Finance App

A personal Python application to manually track daily expenses and savings.

## Goal

Track expenses across three bank accounts:
- Revolut
- Banque Populaire
- Desjardins

And clearly see:
- Total expenses
- Expenses including rent
- Expenses excluding rent
- Current savings

## Scope (V1)

- Manually add an expense
- Categorize expenses (rent / other)
- View total spent amounts
- Savings calculated from total income minus expenses
- Data stored locally
- No authentication
- No cloud synchronization

## Tech Stack

- Python 3.12
- Poetry (dependency management)
- pyenv (Python version management)
- SQLite (local database – planned)

## Project Structure

src/
- finance_app/
  - __init__.py
  - main.py

## Setup

### Prerequisites

- pyenv
- poetry

### Installation

```bash
pyenv install 3.12.2
pyenv local 3.12.2
poetry install
poetry shell
```