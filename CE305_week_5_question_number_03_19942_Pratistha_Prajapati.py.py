import datetime
def update_memory(memory_store, new_block):
    memory_store.update(new_block)
    return memory_store


def map_to_cache_assoc(cache_system, address, main_memory):
    cache_tag = address[:11]  
    memory_block = main_memory.get(address[:11] + '000')  

    if memory_block:
        
        available_line = next((key for key, value in cache_system.items() if value[2] == 0), None)
        if available_line is None:
            
            available_line = list(cache_system.keys())[0]
        
        cache_system[available_line] = [cache_tag, memory_block, 1]

    return cache_system


main_memory_store = {}
assoc_cache = {
    "line1": ["00000000000", [0]*8, 0],
    "line2": ["00000000000", [0]*8, 0],
    "line3": ["00000000000", [0]*8, 0],
    "line4": ["00000000000", [0]*8, 0]
}


memory_block_a = {"00000110101000": [0, 1, 2, 3, 4, 5, 6, 7]}
memory_block_b = {"00001110101000": [10, 11, 12, 13, 14, 15, 16, 17]}
memory_block_c = {"00011110101000": [20, 21, 22, 23, 24, 25, 26, 27]}
memory_block_d = {"00111110101000": [30, 31, 32, 33, 34, 35, 36, 37]}
memory_block_e = {"01111110101000": [40, 41, 42, 43, 44, 45, 46, 47]}


main_memory_store = update_memory(main_memory_store, memory_block_a)
main_memory_store = update_memory(main_memory_store, memory_block_b)
main_memory_store = update_memory(main_memory_store, memory_block_c)
main_memory_store = update_memory(main_memory_store, memory_block_d)
main_memory_store = update_memory(main_memory_store, memory_block_e)


mem_address_1 = "00000110101010"
mem_address_2 = "00001110101010"
mem_address_3 = "00011110101111"
mem_address_4 = "00111110101101"
mem_address_5 = "01111110101110"

assoc_cache = map_to_cache_assoc(assoc_cache, mem_address_1, main_memory_store)
assoc_cache = map_to_cache_assoc(assoc_cache, mem_address_2, main_memory_store)
assoc_cache = map_to_cache_assoc(assoc_cache, mem_address_3, main_memory_store)
assoc_cache = map_to_cache_assoc(assoc_cache, mem_address_4, main_memory_store)
assoc_cache = map_to_cache_assoc(assoc_cache, mem_address_5, main_memory_store)

print("Date: ", datetime.datetime.today())
print(assoc_cache)
