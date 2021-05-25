dict1 = {'Janet' : 87, 'Logan' : 62, 'Whitaker' : 46, 'Alyssa' : 100, 'Stefanie' : 80, 'Jeff' : 88, 'Kim' : 52, 'Sylvia' : 95}
dict2 = {'Logan' : 62, 'Kim' : 52, 'Whitaker' : 52, 'Jeff' : 88, 'Stefanie' : 80, 'Brian' : 60, 'Lisa' : 83, 'Sylvia' : 87}
result1 = {}

print ("1st dictionary", dict1)
print ("2nd dictionary", dict2)

# intersect dictionaries
# Create a new dictionary which is the intersection of two dictionaries.  
# Both key & value must match

#method one
result1 = dict((set(dict1.items()) & set(dict2.items())))

print ("intersection method 1 is", result1)
# Your code should print 
#     intersection is {'Logan': 62, 'Stefanie': 80, 'Jeff': 88, 'Kim': 52}

# method two
result2 = {}
for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        result2[key] = dict1[key]
print('interesection method 2 is', result2)