import datetime as dt
from pathlib import Path
from bs4 import BeautifulSoup
import re

def update_footer_metadata():
    # Get the current date in the desired format
    current_date = dt.datetime.now().strftime("%d-%m-%Y")

    # Define the path to the index.html file
    index_file_path = Path(__file__).parent.parent / "index.html"
    html = index_file_path.read_text(encoding="utf-8")

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html, "html.parser")

    # Find the <time> element with id="lastupdate"
    time_element = soup.find("time", id="lastupdate")
    if time_element:
        # Update the text of the <time> element with the current date
        time_element.string = current_date

        # Write the updated HTML back to the index.html file
        index_file_path.write_text(str(soup), encoding="utf-8")
        print(f"Updated last updated date to: {current_date}")
    else:
        print("Element with id='lastupdate' not found.")

if __name__ == "__main__":
    update_footer_metadata()