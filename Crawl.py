import	subprocess

file = open("raw_data.txt", "w")

cmd = 'curl -k https://ncov.moh.gov.vn/'

raw_data = subprocess.check_output(cmd, shell=True)

file.write(str(raw_data))


