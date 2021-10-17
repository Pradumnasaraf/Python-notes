customer ={
   "name": "Pradumna",
   "list":{
       "element1": "One",
       "element2": "Two",
       "element3": "Three",
   },
   "age":30,
   "myArray":[1,3,5,6],
   "is_verfied":True 
   }
   
print(customer["list"]["element1"])
print(customer["myArray"][2])

# Example

phone =input("Phone: ")

digit_map={

    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

output =""
for Char in phone:
    output += digit_map.get(Char,"!") +" "
print(output)