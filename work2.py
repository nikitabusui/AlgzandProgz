word = 'test'

length = len(word)
mid = length // 2

if length % 2 == 0:
    result = word[mid-1:mid+1]
else:
    result = word[mid]

print(result)
