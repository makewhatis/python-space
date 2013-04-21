from bbfreeze import Freezer
import os
import sys
f = Freezer("space-build", includes=("prettytable","space","argparse"))
python_path = os.path.dirname(sys.executable) + "/"
f.addScript(python_path + "space")
f.use_compression = 0
f.include_py = True
f()

