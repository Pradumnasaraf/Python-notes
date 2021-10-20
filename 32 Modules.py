#Imported a module.
import Converter

#Here we import a #ingle function from the module.
from Converter import kg_to_lbs 

# Here we imported the Hello.
from Converter import Hello

# Here we import util module
import Utils

print(kg_to_lbs(120))

print(Converter.kg_to_lbs(100))

# hello() methof drom Hello Class
Hello.hello()

#calling max_num() function from utils 

print(Utils.max_num([3,4,5,890,8,5,43,3]))




  