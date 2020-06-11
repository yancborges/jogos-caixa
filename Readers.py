import pandas as pd
from bs4 import BeautifulSoup


class Reader:

    __df = None
    __json = None
    __soup = None
    __raw = None

    def __init__(self, raw):

        self.__raw = raw
        self.__soup = BeautifulSoup(raw, 'html.parser')

    def parse(self, headers, rows):

        def mount_json():

            _list = []
            for row in rows:
                current = {}
                for header in headers:
                    index = headers.index(header)
                    current[header] = row[index]

                _list.append(current)

            self.__json = _list

        def mount_pandas():
            self.__df = pd.DataFrame.from_records(self.__json)

        mount_json()
        mount_pandas()
        return self.__df

    def read(self):

        # These files have all the same structure:
        # A table as a <th> tag inside a <small> tag.
        # Then the rows are all in <tr>, which each
        # cell within a <td> tag. So beautiful soup
        # will do well here.

        # This will return a list with everything inside a
        # <font> tag. The first one is not part of the table
        def find_headers():
            return [h.text for h in self.__soup.find_all('font')[1:19]]

        # Same as headers, but each row is inside a <tr> tag
        # The first one is the header row
        def find_rows():
   
            clean = []
            for tr in self.__soup.find_all('tr')[1:]:
                if len(tr.contents) < 20:
                    continue
                clean_row = []
                for value in tr.contents[:36]:
                    if value != '\n':
                        clean_row.append(value.text)
                clean.append(clean_row)
            return clean

        headers = find_headers()
        rows = find_rows()

        return self.parse(headers, rows)
