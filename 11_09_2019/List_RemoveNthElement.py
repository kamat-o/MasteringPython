def RemoveNthElem(List,word,occr):
    tempocc = 0
    for i,s in enumerate(List):
        if s==word:
            tempocc+=1
            if tempocc==occr:
                List.pop(i)
                break
    else:
        print(word +" Word not found")
    
    return List

List=["onkar","n","kamat","onkar"]
print(RemoveNthElem(List,"onkar",1))