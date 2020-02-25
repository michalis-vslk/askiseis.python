i=0
listword=[]
listlength=[]

f = open('keimeno.txt')
for word in f.read().split():
    print( "Word [%5d] : [%32s]  length: %d" %(i , word , len(word)) )
    listword.append(word)
    listlength.append(len(word))
    i=i+1

for k in range(5):
    i  = max(listlength)
    j  = listlength.index(max(listlength))
    w1 = listword[j]
    w2 = listword[j][::-1]
    w3 = w2
    
    for char in 'aAeEiIoOuUyY':
        w3=w3.replace(char,'')

    
    print( "Max length [%2d] at position [%3d]  words: [%s]=>[%s]=>[%s]"  %(i, j, w1 , w2 , w3 ) )
    del listlength[j]
    del listword[j]
