import numpy as np

# repetable random
np.random.seed(68)

dice_roll_1000 = np.random.randint(1,7, 1000)
print(dice_roll_1000[:10])
print(dice_roll_1000.mean())