# Opcode Table (for the pseudo-machine)
OPTAB = {
    'LOAD': '01',
    'ADD': '02',
    'STORE': '03',
    'WORD': None,  # Data directive, no opcode needed
    'END': None,   # No opcode needed for END
}

# Symbol Table
SYMTAB = {}

# Intermediate Code List
intermediate_code = []

# Sample Assembly Program (addition of two numbers)
assembly_code = [
    "START 0",
    "LOAD A",
    "ADD B",
    "STORE C",
    "A WORD 5",
    "B WORD 10",
    "C WORD 0",
    "END"
]

# Pass-I: Generate Symbol Table and Intermediate Code
def pass_one(assembly_code):
    location_counter = 0
    for line in assembly_code:
        parts = line.split()
        if len(parts) == 0:  # Skip empty lines
            continue
        
        # Handle START directive
        if parts[0] == 'START':
            location_counter = int(parts[1])
            intermediate_code.append(f"{location_counter}: {line}")
            continue

        label = None
        opcode = None
        operand = None
        
        # Check if line has a label
        if len(parts) == 3:  # Label, Opcode, Operand
            label, opcode, operand = parts
            SYMTAB[label] = location_counter  # Add label to the symbol table
        elif len(parts) == 2:  # Opcode, Operand (no label)
            opcode, operand = parts
        else:
            opcode = parts[0]  # Only opcode (like END)

        # Handle WORD directive (allocate memory)
        if opcode == 'WORD':
            SYMTAB[label] = location_counter  # Store memory location of the label
            intermediate_code.append(f"{location_counter}: {line}")
            location_counter += 1  # WORD takes up one memory location
        elif opcode in OPTAB:
            intermediate_code.append(f"{location_counter}: {line}")
            location_counter += 1  # Each instruction takes one memory location

    return intermediate_code, SYMTAB

# Pass-II: Generate Final Machine Code
def pass_two(intermediate_code, SYMTAB):
    machine_code = []
    
    for line in intermediate_code:
        address, instruction = line.split(": ")
        parts = instruction.split()
        
        if len(parts) == 3:
            label, opcode, operand = parts
        elif len(parts) == 2:
            opcode, operand = parts
        else:
            opcode = parts[0]

        # Generate machine code using the opcode table and symbol table
        if opcode in OPTAB and OPTAB[opcode]:  # Ignore directives like WORD/END
            op_code = OPTAB[opcode]
            if operand in SYMTAB:  # Operand is a label
                machine_code.append(f"{address} {op_code} {SYMTAB[operand]}")
            else:
                machine_code.append(f"{address} {op_code} {operand}")
        elif opcode == 'WORD':  # Handle WORD directive (store data)
            machine_code.append(f"{address} {operand}")
    
    return machine_code

# Execute Pass-I
intermediate_code, symbol_table = pass_one(assembly_code)

# Print intermediate code and symbol table
print("Intermediate Code:")
for line in intermediate_code:
    print(line)

print("\nSymbol Table:")
for symbol, address in symbol_table.items():
    print(f"{symbol}: {address}")

# Execute Pass-II
machine_code = pass_two(intermediate_code, symbol_table)

# Print final machine code
print("\nFinal Machine Code:")
for line in machine_code:
    print(line)
