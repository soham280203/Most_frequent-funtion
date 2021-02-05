from collections import Counter
def most_frequent(string):
    d={}
    for key in string:

        if key not in d:
            d[key] = 1
        else:

            d[key]=d[key]+1
    final=Counter(d)#counter autosorts in descending order in dictionary
    print(final)


fun=input("Enter a string:")
most_frequent(fun)#function call
