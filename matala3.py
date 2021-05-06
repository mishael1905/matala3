def Read():
    file= input('enter a file path:')
    handle=open(file, encoding='utf-8')
    dictionery(handle)
               
def dictionery(handle:str):
    idList=list()
    fileList=list()
    Data=dict()
    counter=-1
    for line in handle:
        counter+=1
        if counter==1:
            nStart=line.find(' "')
            nEnd=line.find('" ',nStart)
            chat_name=line[nStart+1:nEnd]
            creatAnd=line.find(',')
            creation_date=line[0:creatAnd-1]
        try:
            float(line[0])
            endDate=line.find('-')
            sNum=line.find('-')
            endNum=line.find(':',sNum)
            num=line[sNum+1:endNum].rstrip()
            if endNum != -1:
                if num not in idList:
                    idList.append(num)
                    index=idList.index(num)
                    fileList.append({"datetime":line[0:endDate],"id":index, "text":line[endNum:].rsplit()},)        
        
        except:
            continue
    Data = {'chat_name': chat_name , 'creation_date':creation_date , 'num_of_purtic':len(idList) , 'creator':idList[0] }
    fileList.append(Data)
    import json
    extFile=Data['chat_name']+".txt"
    with open(extFile, 'w', encoding='utf8') as extFile:
        json.dump(fileList, extFile, ensure_ascii=False)