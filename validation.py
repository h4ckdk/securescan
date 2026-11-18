from urllib.parse import urlparse


# it is checking url scheme [ https,http ] and hostname

print("validation.py is loading")

def checks(url):
    weburl = url.strip()
    if weburl == "":
        return "u did not enter url"

    urlparts = urlparse(weburl)
    
    if urlparts.scheme not in  ("http", "https"):
        return "url is must be start with https or http"
    
    if urlparts.hostname == None: 
        return "Error! hostname is not given from u "

    return None


