# PubMed Paper Fetcher

## Overview
This tool fetches research papers from PubMed based on a query and identifies papers with at least one author affiliated with a pharmaceutical or biotech company.

## Installation
1. Install Poetry if not already installed:
2. Clone the repository and navigate to the directory:
3. Install dependencies:


## Usage
Run the command:

poetry run get-papers-list "COVID-19" --file results.csv


## Options
- `-h` or `--help`: Display usage instructions.
- `-d` or `--debug`: Print debug information.
- `-f` or `--file`: Specify filename for saving results.

## Dependencies
- `requests`: Fetch data from PubMed API.
- `pandas`: Process and save data as CSV.
- `argparse`: Parse command-line arguments.

## License
MIT
