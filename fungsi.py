# import package yang dibutuhkan untuk phishing detection
from urllib.parse import urlparse,urlencode
import re

# https in scheme
def httpsURL(url):
  # Parse the URL to extract the scheme/protocol
  parsed_url = urlparse(url)
  scheme = parsed_url.scheme

  # Check if the scheme/protocol is "https"
  if scheme == "https":
    return 0  # Legitimate
  else:
    return 1  # Phishing
  
# http in scheme
def httpURL(url):
  # Parse the URL to extract the scheme/protocol
  parsed_url = urlparse(url)
  scheme = parsed_url.scheme

  # Check if the scheme/protocol is "https"
  if scheme == "http":
    return 1 # Phishing
  else:
    return 0  # Legitimate

# Domain of the URL (Domain)
def getDomain(url):
  domain = urlparse(url).netloc
  if re.match(r"^www.",domain):
    domain = domain.replace("www.","")
  return domain

# Fungsi untuk memeriksa jumlah ? dalam domain URL
def count_question_mark_domain(url):
    domain = getDomain(url)
    count_question_mark_count = domain.count('?')
    return 0 if count_question_mark_count == 0 else 1

# Fungsi untuk memeriksa jumlah & dalam domain URL
def count_ampersand_domain(url):
    domain = getDomain(url)
    count_ampersand_count = domain.count('&')
    return 0 if count_ampersand_count == 0 else 1

# Fungsi untuk memeriksa jumlah * dalam domain URL
def count_asterisk_domain(url):
    domain = getDomain(url)
    count_asterisk_count = domain.count('*')
    return 0 if count_asterisk_count == 0 else 1

# Fungsi untuk menghitung rasio panjang URL terhadap panjang path
def calculate_url_path_ratio(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    if len(path) == 0:
        return 0
    else:
        ratio = len(url) / len(path)
        if ratio < 3:
            return 0
        else:
            return 1
        
def main(url):

    status = []

    status.append(httpsURL(url))
    status.append(httpURL(url))

    status.append(count_question_mark_domain(url))
    status.append(count_ampersand_domain(url))
    status.append(count_asterisk_domain(url))

    status.append(calculate_url_path_ratio(url))

    return status