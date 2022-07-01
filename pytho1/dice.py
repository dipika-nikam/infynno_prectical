import random

# num_dice = 5
# roll_results = []
# for _ in range(num_dice):
#         roll = random.randint(1, 6)
#         roll_results.append(roll)
#         if roll == 6:
#             while roll < 6:
#                 roll_results.append(roll)
#         continue
# print(roll_results)


roll_results = '66666666'
num_dice = 0
for i in range(len(roll_results)):
    if int(roll_results[i]) <= 6:
        if int(roll_results[i]) != 6:
            num_dice=num_dice+1
        continue
print(num_dice)

