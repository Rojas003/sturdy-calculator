# Sturdy Calculator

A strong command-line calculator app written in Python using VS code. It supports addition, subtraction, multiplication, and division, with proper input validation, error handling, and 100% automated test coverage using GitHub Actions.
## How to Run

1. **Clone the repository:**

   ```bash
   git clone git@github.com:your-Rojas003/sturdy-calculator.git
   cd sturdy-calculator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
## Running Tests

To run the tests and check that all calculator features work :

1. **Activate your virtual environment**

   ```bash
   source venv/bin/activate
pytest
## GitHub Actions

This project includes actively synching with GitHub Actions.

Each time you push changes to GitHub, tests are automatically run using `pytest` to guarantee the calculator works how it should.

Doublecheck the status of the latest runs on the **Actions** tab in this repository.
