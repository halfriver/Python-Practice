from urllib.request import urlopen
from time from sleep

# build list of vocab items to iterate through
url_base = "https://www.wanikani.com/vocabulary/"
page_base = urlopen(url_base)
html_base = page_base.read().decode("utf-8")

f = open("..\input\WK_vocab.txt", "w")
# iterate through the txt file to compile list of whatever lies in the <span class="character" lang="ja"> tag
f.close()

f = open("..\input\WK_vocab.txt", "r")
f = open("..\output\WK_vocab.txt", "w")
# iterate through the list and open each page following the format: url_base+(list item)
# the desired example sentences are in the <p lang="ja"> tag, and their translations are in the following <p> tag
# ideally, put each pair on the same line, in a tuple together


f.close()
