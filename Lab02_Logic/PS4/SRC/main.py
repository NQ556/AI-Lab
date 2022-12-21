import os
import os.path as p
from pathlib import Path

def readFile(fileName):
    with open(fileName, 'r') as f:
        clauses = f.read().splitlines() 
    return clauses

def inverseLiteral(literal):
    if literal[0] == '-':
        literal = literal[1:]
    else:
        literal = '-' + literal
    return literal

def inverseClause(clause):
    for i in range(0, len(clause)):
        tmp = inverseLiteral(clause[i])
        clause[i] = tmp
    return clause

def isInversedLiteral(literal1, literal2):
    res = False
    if literal1[0] == '-' and literal2[0] != '-' and literal1[-1] == literal2[-1]:
        res = True
    elif literal1[0] != '-' and literal2[0] == '-' and literal1[-1] == literal2[-1]:
        res = True
    return res

def resolve(clause1, clause2):
    res = []
    tmp = []
    count = 0

    for item in clause1:
        for item2 in clause2:
            if isInversedLiteral(item, item2):
                count += 1
                tmp.append(item)
                tmp.append(item2)
    
    if count == 1:
        res = clause1 + list(set(clause2) - set(clause1))
        for item in tmp:
            res.remove(item)

        if len(res) == 0:
            res.append('{}')   

    return res

def removeMinusSign(literal):
    if literal[0] == '-':
        literal = literal[1:]
    return literal

def sortAlphabetOrder(clause):
    for i in range(0, len(clause) - 1):
        minIdx = i
        for j in range(i+1, len(clause)):
            tmp1 = removeMinusSign(clause[minIdx])
            tmp2 = removeMinusSign(clause[j])
            if tmp1 > tmp2:
                minIdx = j

        clause[i], clause[minIdx] = clause[minIdx], clause[i]

    return clause

def rewriteClause(clause):
    if len(clause) > 1:
        clause = sortAlphabetOrder(clause)
        res = clause[0]

        for i in range(1, len(clause)):
            res += ' OR ' + clause[i]
    else:
        res = clause[0]

    return res

def isExisted(clauses, clause):
    clause = clause.split('OR')
    clause = removeSpaces(clause)

    for i in range(0, len(clauses)):
        curClause = clauses[i].split('OR')
        curClause = removeSpaces(curClause)
        if clause == curClause:
            return True

    return False

def checkEmptyClause(clauses):
    for item in clauses:
        if item == '{}':
            return True

    return False

def removeSpaces(clause):
    for i in range(0, len(clause)):
        clause[i] = clause[i].replace(" ", "")

    return clause

def writeFile(fileName, clauses):
    curPath = p.dirname(Path(__file__).parent.absolute())
    outputPath = curPath + '\\SRC\\' + '\\OUTPUT\\'

    with open(p.join(outputPath, fileName), 'w') as outfile:           
        for item in clauses:
            outfile.write(str(item))
            outfile.write(str('\n'))

def PL_Resolution(clauses, index):
    outputFileName = 'output' + str(index + 1) + '.txt'
    newClauses = clauses.copy()
    tmpClauses = clauses.copy()
    new = []
    output = []

    while True:
        for i in range(0, len(clauses)):
            curClause = clauses[i].split('OR')
            curClause = removeSpaces(curClause)

            for j in range(0, len(newClauses)):
                if clauses[i] != newClauses[j]:
                    nextClause = newClauses[j].split('OR')
                    nextClause = removeSpaces(nextClause)

                    newClause = resolve(curClause, nextClause)
                    
                    if len(newClause) != 0:
                        newClause = rewriteClause(newClause)
                        if not isExisted(tmpClauses, newClause):
                            new.append(newClause)
                            tmpClauses.append(newClause)

        if checkEmptyClause(new):
            length = str(len(new))
            output.append(length)
            output += new
            output.append('YES')    
            break
        elif len(new) == 0:
            output.append('NO') 
            break
        else:
            length = str(len(new))
            output.append(length)
            output += new
            clauses += new
            newClause = []
            newClauses = new.copy()
            new = []

    writeFile(outputFileName, output)

#-----Main-----
curPath = p.dirname(Path(__file__).parent.absolute())
inputPath = curPath + '\\SRC\\' + '\\INPUT\\'
inputFiles = os.listdir(Path(inputPath))

outputPath = curPath + '\\SRC\\' + '\\OUTPUT\\'
Path(outputPath).mkdir(parents = True, exist_ok = True)

for i in range(0, len(inputFiles)):
    fileName = inputPath + inputFiles[i]
    clauses = readFile(fileName)
    tmp = clauses[0].split('OR')
    tmp = removeSpaces(tmp)
    tmp = inverseClause(tmp)
    clauses += tmp
    clauses = clauses[2:]
    PL_Resolution(clauses, i)