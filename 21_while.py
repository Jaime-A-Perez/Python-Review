counter = 0

while counter < 20:
    counter += 1
    if counter % 2 == 0:
        print(f"counter = {counter}")

counter = 0        

while counter < 20:
    counter += 1
    if counter % 2 == 0:
        continue
    print(f"counter = {counter}")

counter = 0

while counter < 20:
    counter += 1
    if counter == 13:
        break
    print(f"counter = {counter}")