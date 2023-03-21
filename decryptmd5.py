import hashlib

hash="5e7d28e2cfff93edefb2d15abad07ec5"                                         # Challenge to be broken

                                                                                # range to limited to lowercase letter (less time)
minletter=97                                                                    # ASCII code for a
maxletter=122                                                                   # ASCII code for z

answer=''
def tryBruteForce(depth):
    global answer, hash
    c=minletter
    notFound=True

    while notFound:
        if (depth>0):
            notFound=tryBruteForce(depth-1)                                     # Try Bruteforce by increment the letter recursively
        
        if(notFound==False):                                                    # if answer found, exit loop
            return False
        answer = answer[:depth] + chr(c)+ answer[depth + 1:]
        if (hashlib.md5(answer.encode()).hexdigest()== hash):                   # test if match
            return False
        if (c<maxletter ):
            c=c+1                                                               # next combination
        else:
            return True                                                         # no match between a-z
    return False

tryBruteForce(20)
print(answer)
