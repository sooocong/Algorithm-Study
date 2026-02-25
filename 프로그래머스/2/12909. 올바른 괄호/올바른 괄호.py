from collections import Counter

def solution(s):
    st = []
    
    if s[0] == ')' or len(s) % 2 != 0 or Counter(s)[')'] != Counter(s)['(']:
        return False
    
    for i in s:
        if i == '(':
            st.append('(')
        else:
            if len(st) == 0:
                return False
            else:
                st.pop()

    if st:
        return False
    else:
        return True