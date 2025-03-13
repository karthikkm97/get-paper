# PubMed Paper Fetcher

## Overview
This tool fetches research papers from PubMed based on a query and identifies papers with at least one author affiliated with a pharmaceutical or biotech company.

## Installation
1. Install Poetry if not already installed:
2. Clone the repository and navigate to the directory:
3. Install dependencies:


## Usage
Run the command:

poetry run get-paper-list "COVID-19" --file results.csv


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


## How to use this package in other project
# step 1 - pip install -i https://test.pypi.org/simple/ get-paper==0.3.0
open a new project and instal get-paper package

# step 2
create a main.py file

# Here is implementation how to access package and use in new project

# step 3  To run the file
python main.py   

### Code:

```python
from paper.fetch import fetch_pubmed_papers  # Import function to fetch papers from PubMed
from paper.utils import save_to_csv  # Import function to save results to a CSV file

def main():
    """
    Main function to fetch research papers and save them to a CSV file.
    """
    # Define the search query
    query = "diabetes treatment"

    # Define the output filename for saving results
    output_file = "results.csv"

    # Inform the user that fetching has started
    print(f"Fetching papers for query: {query}...")

    # Fetch research papers based on the given query
    papers = fetch_pubmed_papers(query)

    # Check if any papers were found
    if not papers:
        print("No papers found.")  # Display message if no papers are available
        return  # Exit the function

    # Save the fetched papers to a CSV file
    save_to_csv(papers, output_file)

    # Confirm that results have been saved
    print(f"Results saved in {output_file}")

# Ensure the script runs only when executed directly (not imported as a module)
if __name__ == "__main__":
    main()


