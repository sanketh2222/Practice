Sentences = ['This is good', 'python is good', 'python is not python snake','joke','python is best in best']
query = "is good"# query= input("enter query string")

def matching(sentence,query):
    score = 0
    words1=sentence.split(" ")
    # print(words1)
    words2=query.split(" ")
    # print(words2)
    for word1 in words1:
        for word2 in words2:
            if word1==word2:
                score+=1
    return score

# print(matching("python is good","python"))

scores=[(matching(sentence,query)) for sentence in Sentences ]
# print(scores)


sentscore=[ sentscore for sentscore in sorted(zip(scores,Sentences),reverse=True)]
sentscorelist=[j for i,j in sentscore if i!=0]#to filter the list by excluding 0 score. to find the no. of exact match
occurance=len(sentscorelist)# no. of match

print(f"{occurance} matched results\n")
for score,sent in sentscore:
    if score!=0:
        print(f"\"{sent}\"  matched with a score of {score}\n")