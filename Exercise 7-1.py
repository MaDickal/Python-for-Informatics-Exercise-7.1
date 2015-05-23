# prompts for file name
fname = raw_input('Enter a file name: ')

# checks to see if file name is valid
try:
    fhandle = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

# removes \n and changes lines to upper case, then prints
for line in fhandle:
    line = line.rstrip()
    line = line.upper()
    print line


