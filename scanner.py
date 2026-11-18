import requests
import urllib3
from validation import checks
from Engine import full_header_check

url= input("enter your website address: ").strip()
problem = checks(url)

if problem:
    print("it is invalid address", problem)
else:
        try:
            result_get = full_header_check(url)
            
        except requests.exceptions.ConnectionError:
            print("could not connect, check the address or your internet")
        except requests.exceptions.Timeout as tymeout:
            print("the website took a very long time")
            print("reason", tymeout)
        except requests.exceptions.RequestException as error:
            print("could not the scan the website")
            print("reason", error)
        except urllib3.exceptions.LocationParseError:
            print("the website name is not valid")

        else:
            if "error" in result_get:
                print("Scanning Warning", result_get["error"])
            else:
                for header,availble in result_get.items():
                    if availble:
                        print("available ", header)
                    else:
                        print("missing ", header)

