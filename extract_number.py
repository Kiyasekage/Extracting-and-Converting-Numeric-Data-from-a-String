custom_string = 'X-MAPDS-Confidence:0.8475' 
output = custom_string.find(":")
taken = custom_string[output+1:custom_string.find("5")+1]
data = float(taken)
print(data)
print(type(data))
