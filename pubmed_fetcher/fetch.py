import requests
import pandas as pd
from typing import List, Dict, Optional

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_pubmed_papers(query: str, max_results: int = 10) -> List[Dict]:
    """Fetches papers from PubMed API based on the search query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    
    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    data = response.json()
    
    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    return fetch_paper_details(paper_ids)

def fetch_paper_details(paper_ids: List[str]) -> List[Dict]:
    """Fetches detailed information about papers given their PubMed IDs."""
    if not paper_ids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    
    response = requests.get(PUBMED_SUMMARY_URL, params=params)
    response.raise_for_status()
    details = response.json().get("result", {})

    papers = []
    for pid in paper_ids:
        paper = details.get(pid, {})
        papers.append({
            "PubmedID": pid,
            "Title": paper.get("title", "N/A"),
            "Publication Date": paper.get("pubdate", "N/A"),
            "Authors": paper.get("authors", []),
            "Company Affiliations": find_non_academic_authors(paper.get("authors", [])),
            "Corresponding Author Email": paper.get("correspondence", "N/A")
        })
    
    return papers

def find_non_academic_authors(authors: List[Dict]) -> Optional[List[str]]:
    """Identifies non-academic authors based on affiliations."""
    non_academic_authors = []
    for author in authors:
        if "affiliation" in author and ("Inc" in author["affiliation"] or "Ltd" in author["affiliation"]):
            non_academic_authors.append(author["name"])
    
    return non_academic_authors if non_academic_authors else None
