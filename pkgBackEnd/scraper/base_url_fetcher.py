import logging
import pprint

from pkgBackEnd.FileIO import url_reader

#This class can eventually be used to read other URLs....

class BaseUrlFetcher:
    def __init__(self):
        self.base_url = None


    def get_base_url(self):
        self.base_url = url_reader.load_base_url()
        return self.base_url








