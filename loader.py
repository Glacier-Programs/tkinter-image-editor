def save(alist,file):
    file = open(file,'w+')
    file.seek(0)
    for i in range(0,int(file.readline())):
        file.seek(i)
        file.write('')
    file.seek(0)
    file.write(len(alist))
    for i in range(0,len(alist)):
        file.seek(i+1)
        cur = alist[i]
        curData = ''
        for i in range(0,len(alist)):
            curData.append(str(alist[i])+' ')
        file.write(curData)