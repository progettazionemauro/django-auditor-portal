# Importing the above
# created module
import hello
from pathlib import Path

 
 
# Calling the method
# created inside the module
# hello.Ciao()
    
# printing the __file__
# variable

BASE_DIR1=Path(__file__)
BASE_DIR2=Path(__file__).resolve().parent
BASE_DIR3=Path(__file__).resolve().parent.parent
BASE_DIR4=Path(__file__).resolve().parent.parent.parent

# print(hello.__file__)

print ("Nome del presente file", BASE_DIR1)
print ("Directory in cui risiede il progetto Django",BASE_DIR2)
print (BASE_DIR3)
print (BASE_DIR4)
