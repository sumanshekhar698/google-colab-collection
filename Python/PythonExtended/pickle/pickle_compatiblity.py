import time, pickle


print("Default Pickle Protocol", pickle.DEFAULT_PROTOCOL) # 4
print("Highest Pickle Protocol", pickle.HIGHEST_PROTOCOL) # 5

# 0 5 

big = {"numbers": list(range(50_000)), "text": ["row"] * 10_000}

# for k,v in big.items():
#     print(f"{k} : {v}")


for proto in range(pickle.HIGHEST_PROTOCOL + 1):
    t0 = time.perf_counter()
    data = pickle.dumps(big, protocol=proto)
    elapsed = time.perf_counter() - t0
    print(f"  protocol {proto}: {len(data):>9,} bytes   {elapsed*1000:>6.1f} ms")