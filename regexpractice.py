import re

def displayMatch(match)->str:
    """
    input: re.match instances
    output: str display of match or 'False'
    time complexity: n^0
    """
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

def yieldConstructor(regexStr:str):
    """
    input: reg expression string
    output: re generator
    time complexity: n(re.compile) + n(.match)
    """
    valid = re.compile(regexStr)
    def matcher(strInp:str):
        yield valid.match(strInp)
    return matcher

def main(regexStr:str, inputs:list[str:str])->str:
    """
    input: regular expression string, list of string inputs
    output: display strings for 
    """
    res = yieldConstructor(regexStr)
    resList = []
    for i in inputs:
        resListPart = list(res(i))
        resList.append(resListPart[0])
    
    for x in resList:
        print(displayMatch(x) if displayMatch(x) else 'False')

if __name__ == "__main__":
    regex = r"^pa2-9tjqk]{5}$"
    inputs = ["akt5q", "akt5e", "akt", "727ak", "qtkk5", "kkkqt", "11225", "11115", "qqttk", "kkkkq", "11112"]
    main(regex, inputs)    
        
