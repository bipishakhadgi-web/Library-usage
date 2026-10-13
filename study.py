from tqdm import tqdm
import time

for i in tqdm(range(20), desc="Study Progress"):
    time.sleep(0.2)

print("All 20 study tasks completed")