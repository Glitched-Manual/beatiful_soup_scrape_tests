site = "www.google.com"

x = site.rindex('.')
#find last '.'
print(x)

#print after last '.'
print(site[x:])

#print before last '.'
print(site[:x])