import numpy as np
import sys

# -------------------------------------------------------
num_process = int(input("Enter number of processes: "))
num_resource_types = int(input("Enter number of resource types: "))

allocation = []
need = []
maxx = []

maxx_or_need = "need"

print("Enter allocation: ")
for i in range(num_process):
    allocation_i = list(map(int, input().split()))

    if len(allocation_i) == 0:
        break

    allocation.append(allocation_i)

allocation = np.array(allocation)

print("Enter need (or skip if you have max instead): ")
for i in range(num_process):
    need_i = list(map(int, input().split()))

    if len(need_i) == 0:
        maxx_or_need = "maxx"
        break

    need.append(need_i)

if maxx_or_need == "maxx":
    print("Enter maxx: ")
    for i in range(num_process):
        maxx_i = list(map(int, input().split()))

        if len(maxx_i) == 0:
            break

        maxx.append(maxx_i)

if maxx_or_need == "need":
    need = np.array(need)
else:
    maxx = np.array(maxx)
    need = maxx - allocation

    print("Calculate need = maxx - allocation: ")
    for i in need:
        print(i)

print("Enter available: ")
available = list(map(int, input().split()))
available = np.array(available)

if len(allocation) != num_process or len(need) != num_process or len(available) != num_resource_types:
    print("Invalid input! Ngu vl")
    sys.exit()

for i in range(num_process):
    if len(allocation[i]) != num_resource_types or len(need[i]) != num_resource_types or len(maxx[i]) != num_resource_types:
        print("Invalid input! Ngu vl")
        sys.exit()
    

# -------------------------------------------------------

def compare(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
        
    return True

work = available.copy()
finish = [0] * num_process

work_result = []
finish_result = []
process_result = []
state_result = "Safe ✅"

while (True):
    is_found = False
    
    for i in range(num_process):
        if finish[i] == 0 and compare(need[i], work) == True:
            finish[i] = 1
            work += allocation[i]

            finish_result.append(finish.copy())
            work_result.append(work.copy())
            process_result.append("P" + str(i))
            is_found = True
            break
    
    if is_found == False:
        break

for i in finish:
    if i == 0:
        state_result = "Unsafe ❌"

print()
print("---------------------------------------------------------------")
print()

print(f"{"":5} {"Work":<20} {"Finish":<20}")
print(f"{"":5} {str(available.tolist()):<20} {str([0] * num_process):<20}")

print()

for i in range(len(process_result)):
    print(f"{process_result[i]:5} {str(work_result[i]):<20} {str(finish_result[i]):<20}")

print()
print("====>", state_result)
print()