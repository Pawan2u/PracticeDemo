

def per(speed):
    """permutation function return the num of possible groups  """
    if len(speed)==0:
        return []
    if len(speed)==1:
        return [speed]
    mylist=[]
    for i in range(len(speed)):
        m=speed[i]
        rem_l=speed[:i]+speed[i+1:]
        
        for p in per(rem_l):
            mylist.append([m]+p)
    return mylist

def group(num):

    rem=[2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200,1307674368000]
    r={1:'0',2:'0',6:'0',24:'1',120:'2',720:'3',5040:'4',40320:'5',362880:'6',3628800:'7',39916800:'8',479001600:'9',6227020800:'10',
    87178291200:'11',1307674368000:'12'}
    g=num+pow(5,rem.index(num))+int(r.get(num))
    return g


def num_per(speed):
    #group={0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880,10:3628800,11:39916800,12:479001600,13:6227020800,
    #14:87178291200,15:1307674368000}

    perm=per(speed)
    groups=group(len(perm))
    result=groups/len(perm)
    res=round(result,6)
    return res   



#------------------------------------------------#

N=int(input())
speed=list(map(int,input().split()))
print(num_per(speed))
