import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txxt")
else:
    print("The file doesn't exist")