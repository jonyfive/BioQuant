#!/usr/bin/python3
# =================================================
# Download user data, decopmress and write to file.
# =================================================


import requests
import time
import bz2
from time import localtime, strftime


def getData(url,prefix):
    s = requests.session()
    adapter = requests.adapters.HTTPAdapter(
        max_retries=5)  # Configure adapter and retries
    s.mount(prefix, adapter)  # Mount adapter
    response = s.get(url, timeout=5)  # Get response from server
    if response.status_code == requests.codes.ok:  # Verify server response
        binary = bz2.decompress(response.content)  # Decompress data
        decoded = binary.decode()  # Decode binary data
        archive = 'archive/allUsers/' + strftime("%d %b %y", localtime())
        current = 'current/allUsers'
        with open(current, 'w') as currentFile, open(archive, 'w') as archiveFile:
            currentFile.write(decoded)  # Dump all users data to file
            archiveFile.write(decoded)  # Dump all users data to archive
            print('\nSuccess')
    else:
        print('\nError')
    return(response.status_code)


# MAIN===========================================================================
tzero = time.time()  # Set inital time for runtime test
url = ''
prefix = ''
status = getData(url1,url2)
print(status)
print('Algo runtime is %s seconds' %
      (time.time() - tzero),'\n')  # Final code runtime
# ===============================================================================
