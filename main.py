strings = ['a', 'b', 'c', 'd']
#4*4 = 16 bytes of storage is used
print('String array:',strings)

print('\n''Index 2 of string array:', strings[2])

#push 
strings.append('e') #O(1)
print('\n''Append e into string array:',strings)

#pop
strings.pop() #O(1)
print('Pop e out of string array',strings)
strings.pop()
print('Pop an element again',strings)

#add first element
strings.insert(0,'x') #O(n)
print('\n''Insert x into index 0 of array:',strings)

#splice
strings.insert(2,'alien') #O(n)
print('\n''Splice the word alien into string array index 2:',strings)
