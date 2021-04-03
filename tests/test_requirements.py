# Check the versions of libraries
import subprocess

def getModule(module):
    subprocess.call("pip install " + module + " --user", shell=True)
 
# Python version
import sys
print('Python: {}'.format(sys.version))

# scipy
try:
    import scipy
    print('scipy: {}'.format(scipy.__version__))
except:
    getModule("scipy")
    print("--Downloaded--")
    
# numpy
try:
    import numpy
    print('numpy: {}'.format(numpy.__version__))
except:
    getModule("numpy")
    print("--Downloaded--")
    
# matplotlib
try:
    import matplotlib
    print('matplotlib: {}'.format(matplotlib.__version__))
except:
    getModule("matplotlib")
    print("--Downloaded--")
    
# pandas
try:
    import pandas
    print('pandas: {}'.format(pandas.__version__))
except:
    getModule("pandas")
    print("--Downloaded--")

# scikit-learn
try:
    import sklearn
    print('sklearn: {}'.format(sklearn.__version__))
except:
    getModule("sklearn")
    print("--Downloaded--")
