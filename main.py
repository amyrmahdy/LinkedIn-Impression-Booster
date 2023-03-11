import sys
from playfunc import playing

try:
    views = int(sys.argv[1])
    seconds = int(sys.argv[2])
except:
    print("Use default values.")
    views = 1000
    seconds = 5

with open("input.txt","r") as f:
    posts = f.read().split("\n")[:-1]

for post in posts:
    playing(post,views,seconds)