from subprocess import Popen, PIPE
import os

# Inputs to automate
# Use \n to replace enter
inputs = b'3\n2\n1\n99\n2\nElectronics\n3\n100\n500\n4\n3\n4\n'

p = Popen(['python', 'main.py', 'productdata200.csv'], cwd=os.path.dirname(os.getcwd()), stdin=PIPE, stdout=PIPE, shell=False)
out = p.communicate(input=inputs, timeout=5)

# Uncomment to view output
#print(str(out[0]).replace('\\r\\n', '\n'))