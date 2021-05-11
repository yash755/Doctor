

# file = open('name.txt','r')
#
# for f in file:
#     f = f.replace('\n','')
#     f = f.split('===')
#
#     error = open('refact.txt', 'a+')
#     error.write(f[0] + '\n')
#     error.close()



file = open('refact.txt','r')

arr = []

for f in file:
    f = f.replace('\n', '')

    arr.append(f)


# arr1 = []
#
# for a in arr:
#     if a not in arr1:
#         arr1.append(a)
#
# print (len(arr1))


file1 = open('zip.txt','r')

arr1 = []

for f1 in file1:
    f1 = f1.replace('\n', '')

    if f1 not in arr:
        arr1.append(f1)

        error = open('final_zip.txt', 'a+')
        error.write(f1 + '\n')
        error.close()

print (arr1)

print (len(arr1))
