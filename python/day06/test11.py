text = ''' The first statement of the function body can optionally be a string literal; this string literal is the function’s documentation string, or docstring. (More about docstrings can be found in the section Documentation Strings.) There are tools which use docstrings to automatically produce online or printed documentation, or to let the user interactively browse through code; it’s good practice to include docstrings in code that you write, so make a habit of it. '''


dic = dict();
for c in text:
    if c.isalpha() == False:
        continue
    c = c.lower()
    if c not in dic:
        dic[c] = 1
    else:
        dic[c] +=1

print(dic)
ks = list(dic.keys());
ks.sort()
for k in ks:
    print('%s : %d' %(k,dic[k]))

# print(ks)
# list_dic = list(dic)
print(sorted(dic.items(),key=lambda x : -x[1]))
# key_data = list(dic.keys())
# print(key_data);
# key_data.sort();
# print(key_data)

# for a in key_data:
#     print('%s = %d개' %(a,dic[a]));


