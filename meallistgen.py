import requests
import csv

url = "http://pastebin.com/raw/sKNP6999"


def format_csv_data(dirty_data: list) -> dict[str: int]:
    """makes dirty csv data into a dictionary with each key: value pair being 'name of item': weight"""
    for i, row in enumerate(dirty_data):
        if len(row) < 2:
            # append "1" as weight to row if row doesn't have weight value
            row.append("1")
        
        row[1] = int(row[1].strip())  # strip whitespaces from weight and convert to int
        dirty_data[i] = tuple(row)
    
    return {
        item: weight
        for item, weight
        in dirty_data
    }
    

def get_csv_data(url) -> list[list[str]]:
    request = requests.get(url)

    if (status := request.status_code) != 200:
        print(f"error: unexpected status code from response (expected 200, got {status})")
        exit(1)

    if not (content_type := request.headers["Content-Type"]).startswith("text/plain"):
        print(f"error: Content-Type is not plain text (got {content_type})")
        exit(1)

    return list(csv.reader(request.text.splitlines()))


data = format_csv_data(get_csv_data(url))
print(data)