import subprocess
import time

# Perform Crawl and Clean data
subprocess.check_output('python3 Crawl.py', shell=True)
print('\n Done Crawl! \n')

subprocess.check_output('python3 Clean_data.py', shell=True)
print('\n Done Clean \n')


