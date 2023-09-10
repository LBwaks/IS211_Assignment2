import argparse
import urllib.request
import logging
import datetime


def downloadData(url):
    """Downloads the data"""
    url = 'https://docs.google.com/spreadsheets/d/15HDKNRJcAaPkl4w1rDWSgR9kpMq11AIG8PTABjxRJfU/edit#gid=2006694583'
    with urllib.request.open(url) as response:
        response = response.read().decode("utf-8")
    print(response)
    return response


def processData(file_content):
    pass


def displayPerson(id, personData):
    pass


def main(url):
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
