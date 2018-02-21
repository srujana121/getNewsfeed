# getNewsfeed
getparsedfeed in the file getfeed.py takes the arguments keyword and service ie either google or bing news. 
Eg : 

from getfeed import getparsedfeed

service = raw_input("Enter the news service to be used. Google/Bing")
#service = "google"
query = raw_input("Enter the keyword to be seaarched")
#query = "Pride and Prejudice"
feedlist = getparsedfeed(query,service)
