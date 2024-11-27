from subprocess import Popen, PIPE
import os

# Inputs to automate
# Use \n to replace enter
inputs = b'2\n2\n1\n2\n3\n4\n4\n4\n'

p = Popen(['python', 'main.py', 'productdata400.csv'], cwd=os.path.dirname(os.getcwd()), stdin=PIPE, stdout=PIPE, shell=False)
out = p.communicate(input=inputs, timeout=5)

# Uncomment to view output
#print(str(out[0]).replace('\\r\\n', '\n'))