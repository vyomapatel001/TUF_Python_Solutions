def isomorphicstrings(s:str, t:str)->bool:
    return t==s.translate(str.maketrans(s,t)) and s==t.translate(str.maketrans(t,s))


if __name__=="__main__":
    s="egg"
    t="add"
    print(isomorphicstrings(s,t))

    s="foo"
    t="bar"
    print(isomorphicstrings(s,t))

#Time Complexity: O(n)
#Space Complexity: O(1)

#Second Approach using dict

def isIsomorphic(s: str, t: str) -> bool:
        map_s_t, map_t_s = {}, {}

        for cs, ct in zip(s, t):
            if cs in map_s_t and map_s_t[cs] != ct:
                return False
            if ct in map_t_s and map_t_s[ct] != cs:
                return False
            map_s_t[cs] = ct
            map_t_s[ct] = cs

        return True

if __name__=="__main__":
     s="paper"
     t="title"
     print(isIsomorphic(s,t))

#Time Complexity: O(n)
#Space Complexity: O(1)