import operator

def run(program: list) -> list:
    variables = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    ops = {"ADD": operator.add, "SUB": operator.sub, "MUL": operator.mul}

    ifs = {"==": operator.eq, "!=": operator.ne, "<": operator.lt, ">": operator.gt, "<=": operator.le, ">=": operator.ge}

    output = []
    k = 0
    whileloop = True
    while True:
        for i in program[k:]:
            k += 1
            whileloop = False
            part = i.split(" ")
            
            if part[0] == "MOV":
                variables[part[1]] = int(part[2]) if part[2] not in variables else variables[part[2]]
                
            elif part[0] in ops:
                if part[2] not in variables:
                    variables[part[1]] = ops[part[0]](variables[part[1]], int(part[2]))
                else:
                    variables[part[1]] = ops[part[0]](variables[part[1]], variables[part[2]])
            
            elif part[0] == "IF":
                if part[3] not in variables:
                    condition = ifs[part[2]](variables[part[1]],int(part[3]))
                else:
                    condition = ifs[part[2]](variables[part[1]],variables[part[3]])

                if condition:
                    k = program.index(part[5]+":")
                    break
                elif k == len(program): 
                    whileloop = True
                    break
                else:
                    continue       
            
            elif part[0] == "PRINT":
                output.append(int(part[1])) if part[1] not in variables else output.append(variables[part[1]])
                    
            elif part[0] == "JUMP":
                k = program.index(part[1]+":")
                break
            
            if part[0] == "END" or k == len(program):
                whileloop = True
                break
        
        if whileloop:
            break
    
    return output