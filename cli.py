import argparse
from pubmed_fetcher.fetch import fetch_pubmed_papers
from pubmed_fetcher.utils import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Save output to CSV file")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    
    args = parser.parse_args()
    
    if args.debug:
        print(f"Fetching papers for query: {args.query}")
    
    papers = fetch_pubmed_papers(args.query)
    
    if args.file:
        save_to_csv(papers, args.file)
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
