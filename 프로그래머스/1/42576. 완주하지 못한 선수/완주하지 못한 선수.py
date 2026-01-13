def solution(participant, completion):
    
#     for com in completion:
#         if com in participant:
#             participant.remove(com)
#         else:
#             answer.append(com)

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
            break
        
    return participant[-1]
    
    # return participant[-1]