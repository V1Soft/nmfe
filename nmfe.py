import sys
import os

global catagory, author, name

def parseheader(header):
    global catagory, author, name

    catagory = header.split('-')[0]
    author = header.split('-')[1]
    name = header.split('-')[2]

def openfile(f):
    global catagory, author, name

    if open(f, 'r+').read().split('\n')[0].split(' ')[0] == 'ftype':
        for value in open(os.environ['HOME'] + '/.config/nmfe/defaults', 'r+').read().split('\n'):
            if value.split(' ')[0] == open(f, 'r+').read().split('\n')[0].split(' ')[1]:
                os.system(value.split(' ')[1] + ' ' + f)
                sys.exit(0)
        parseheader(open(f, 'r+').read().split('\n')[0].split(' ')[1])
        die('No default application set for ftype ' + author[0].upper() + author[1:] + ' ' + name.upper() + ' of type "' + catagory + '"\nReview ~/.config/nmfe/defaults and set for ' + open(f, 'r+').read().split('\n')[0].split(' ')[1])

def die(message):
    print(message)
    sys.exit(1)
        
if len(sys.argv) > 1:
    openfile(sys.argv[1])
else:
    die('File to open not specified')
