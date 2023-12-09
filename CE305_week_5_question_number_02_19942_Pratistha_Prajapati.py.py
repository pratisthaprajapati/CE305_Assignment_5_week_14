import datetime
def update_memory(memory, block):
    memory.update(block)
    return memory


def map_to_cache(cache, address, memory):
    tag_segment, block_segment, _ = address[:7], address[7:11], address[11:]
    block_data = memory.get(address[:11] + '000', None)

    if block_data is not None:
        cache[block_segment] = [tag_segment, block_data, 1]

    return cache


def cache_hit_or_miss(cache, address):
    tag_segment, block_segment, _ = address[:7], address[7:11], address[11:]
    cache_line = cache.get(block_segment, None)

    if cache_line and cache_line[0] == tag_segment and cache_line[2] == 1:
        return "Hit"
    else:
        return "Miss"
    
memory_state = {}
cache_state = {f"{i:04b}": ["0000000", [0]*8, 0] for i in range(16)}


block_a = {"00001110101000": [10, 11, 12, 13, 14, 15, 16, 17]}  
block_b = {"00000110101000": [0, 1, 2, 3, 4, 5, 6, 7]}  
block_c = {"00001110111000": [20, 21, 22, 23, 24, 25, 26, 27]}  


memory_state = update_memory(memory_state, block_a)
memory_state = update_memory(memory_state, block_b)
memory_state = update_memory(memory_state, block_c)


address_2 = "00001110101010"  
address_1 = "00000110101010"  
address_3 = "00001110111111"  

cache_state = map_to_cache(cache_state, address_2, memory_state)
cache_state = map_to_cache(cache_state, address_1, memory_state)
cache_state = map_to_cache(cache_state, address_3, memory_state)


result_1 = cache_hit_or_miss(cache_state, address_1)
result_2 = cache_hit_or_miss(cache_state, address_2)
result_3 = cache_hit_or_miss(cache_state, address_3)

print("Date: ", datetime.datetime.today())

print("Hit or Miss for address 1 (equivalent to adr1):", result_1)
print("Hit or Miss for address 2 (equivalent to adr2):", result_2)
print("Hit or Miss for address 3 (equivalent to adr3):", result_3)

