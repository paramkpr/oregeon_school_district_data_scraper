import json

from scrape_table import scrape_table



def main():
    with open('links.json', 'r') as f:
        for row in json.load(f):
            scrape_table(row['dp1'], f"{row['name']}_dp1")
            scrape_table(row['dp2'], f"{row['name']}_dp2")
            scrape_table(row['dp3'], f"{row['name']}_dp3")
            scrape_table(row['dp4'], f"{row['name']}_dp4")

if __name__ == "__main__":
    main()
