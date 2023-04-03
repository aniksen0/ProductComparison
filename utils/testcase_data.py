from utils.openpyxlfunction import *
import pathlib
# Search Keyword
account = "xohef93592@activesniper.com"
password = "asdfghqwerty#123"

filename = "JOBLISTING.xlsx"
bdjobsheet = "BDJOB"

ConfigPage = "config"
filepath = pathlib.Path(__file__).parent / f"{filename}"
searchkeyword = "oppo"
RequiredParameter = read_data(filepath, ConfigPage, 4, 2)