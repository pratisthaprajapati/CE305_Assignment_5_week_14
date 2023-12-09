import datetime

init_mem = {}  
a = {800: 123}  
b = {900: 1000}  

def store(memory, element):
    address, value = element.popitem()
    memory[address] = value
    return memory

print("Date: ", datetime.datetime.today())

mem = store(init_mem, a)
print("mem =", mem)  

mem = store(mem, b)
print("mem =", mem)  

c = {800: 900}
mem = store(mem, c)
print("mem =", mem)  

d = {1500: 700}
mem = store(mem, d)
print("mem =", mem)  

def imm_load_ac(val):
    return val

ac = imm_load_ac(800)
print("ac =", ac)  

def dir_load_ac(memory, val):
    return memory.get(val, 0)

ac = dir_load_ac(mem, 800)
print("ac =", ac)  

def indir_load_ac(memory, val):
    indir_address = memory.get(val, 0)
    return memory.get(indir_address, 0)

ac = indir_load_ac(mem, 800)
print("ac =", ac)  

def idx_load_ac(memory, idx, val):
    idx_address = memory.get(val, 700) + idx
    return memory.get(idx_address,700)

idxreg = 700
ac = idx_load_ac(mem, idxreg, 800)
print("ac =", ac)  

