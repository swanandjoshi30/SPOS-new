def pass1_macroprocessor(source_code):
    mnt = {}
    mdt = []
    intermediate_code = []
    macro_def = False
    macro_name = None

    for line in source_code:
        tokens = line.strip().split()

        if tokens[0] == "MACRO":
            macro_def = True
        elif macro_def and not macro_name:
            macro_name = tokens[0]
            mnt[macro_name] = len(mdt)
        elif macro_def and tokens[0] == "MEND":
            macro_def = False
            macro_name = None
        elif macro_def:
            mdt.append(line.strip())
        else:
            intermediate_code.append(line.strip())

    return mnt, mdt, intermediate_code

source_code = [
    "MACRO", 
    "INCR &ARG", 
    "ADD &ARG, 1", 
    "MEND",
    "START", 
    "MOV A, B", 
    "INCR A", 
    "END"
]

mnt, mdt, intermediate_code = pass1_macroprocessor(source_code)

print("MNT:", mnt)
print("MDT:", mdt)
print("Intermediate Code:", intermediate_code)

def pass2_macroprocessor(mnt, mdt, intermediate_code):
    expanded_code = []

    for line in intermediate_code:
        tokens = line.split()

        if tokens[0] in mnt:
            macro_name = tokens[0]
            macro_start = mnt[macro_name]
            actual_arg = tokens[1]

            for macro_line in mdt[macro_start:]:
                expanded_line = macro_line.replace("&ARG", actual_arg)
                expanded_code.append(expanded_line)

        else:
            expanded_code.append(line)

    return expanded_code

expanded_code = pass2_macroprocessor(mnt, mdt, intermediate_code)

print("Expanded Code:")
for line in expanded_code:
    print(line)
