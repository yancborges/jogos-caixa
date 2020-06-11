from Readers import Reader
import zipfile
import os
import requests
import io


class Loader:

    __directory = os.path.join('/data')
    __raw_html = None
    __df = None
    __valid_games = ['lotofacil']

    def __init__(self, game):

        if game not in self.__valid_games:
            raise KeyError('Invalid game name')
        self.game = game
        self.download()
        self.load_df()

    @property
    def data(self):
        return self.__df

    def load_df(self):
        self.__df = Reader(self.__raw_html).read()

    def download(self):

        # Downloading zipped file from url
        # It's encoded so i have to decode it as a UTF-8 text
        url = self.get_url()
        file = requests.get(url)
        if file.status_code != 200:
            raise ConnectionError('Erro de conexão')
        file = file.content

        # Now i have the file loaded, but it's Byte encoded
        # The ZipFile module does it for me
        #
        # The downloaded zipfile has 2 files within,
        # i have to use the .htm one
        filebytes = io.BytesIO(file)
        myzipfile = zipfile.ZipFile(filebytes)
        for file in myzipfile.filelist:
            if file.filename.endswith('htm'):
                self.__raw_html = myzipfile.read(file.filename).decode('latin-1')

    def get_url(self):

        path = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/'
        files = {
            'lotofacil': 'D_lotfac.zip'
        }

        return path + files[self.game]
