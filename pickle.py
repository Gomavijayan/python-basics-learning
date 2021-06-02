import pickle

mydict = {'1': 'a' , '2': 'b'}
pickle_file = open("pocklefile.txt","wb")
pickle.dump(mydict, pickle_file)

pickle_file = open ("pocklefile.txt","rb")
new_dict = pickle.load(pickle_file)

print(new_dict)