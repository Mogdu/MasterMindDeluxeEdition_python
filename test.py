


import time


count = 100000

start = time.time()
for c in range(count):
    proposition = [1,2,3,4]
    for i in range(len(proposition)):  # on reinitialise proposition
            proposition.pop()
end = time.time()
print("for:", end-start)

start = time.time()
for c in range(count):
    proposition = [1,2,3,4]

    proposition = []
end = time.time()
print("assignement:", end-start)