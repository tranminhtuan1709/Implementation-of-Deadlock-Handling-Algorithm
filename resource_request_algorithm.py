import numpy as np
import sys

# -------------------------------------------------------
num_process = int(input("Enter number of processes: "))
num_resource_types = int(input("Enter number of resource types: "))

alloc = []
ne = []
maxx = []

maxx_or_need = "need"

print("Enter allocation: ")
for i in range(num_process):
    alloc_i = list(map(int, input().split()))

    if len(alloc_i) == 0:
        break

    alloc.append(alloc_i)

alloc = np.array(alloc)

print("Enter need (or skip if you have maxx instead): ")
for i in range(num_process):
    ne_i = list(map(int, input().split()))

    if len(ne_i) == 0:
        maxx_or_need = "maxx"
        break

    ne.append(ne_i)

if maxx_or_need == "maxx":
    print("Enter maxx: ")
    for i in range(num_process):
        maxx_i = list(map(int, input().split()))

        if len(maxx_i) == 0:
            break

        maxx.append(maxx_i)

if maxx_or_need == "need":
    ne = np.array(ne)
else:
    maxx = np.array(maxx)
    ne = maxx - alloc

    print("Calculate need = maxx - allocation: ")
    for i in ne:
        print(i)

print("Enter available: ")
avai = list(map(int, input().split()))
avai = np.array(avai)

print("Enter list processes requesting resource: ")
p_req = list(map(int, input().split()))

print("Enter requesting resources by the processes above respectively: ")
reqr = []
for i in range(len(p_req)):
    reqr_i = list(map(int, input().split()))

    if len(reqr_i) == 0:
        break

    reqr.append(reqr_i)

reqr = np.array(reqr)

if len(alloc) != num_process or len(ne) != num_process or len(avai) != num_resource_types:
    print("Invalid input!")
    sys.exit()

for i in range(num_process):
    if len(alloc[i]) != num_resource_types or len(ne[i]) != num_resource_types or len(maxx[i]) != num_resource_types:
        print("Invalid input!")
        sys.exit()

if len(reqr) != len(p_req):
    print("Invalid input!")
    sys.exit()

# -------------------------------------------------------
def compare(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
        
    return True

def banking_algorithm(a, b, c):
    print("Call Banker Algorithm...")
    allocation = a.copy()
    need = b.copy()
    available = c.copy()
    
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
    print(f"{"":5} {"Work":<20} {"Finish":<20}")
    print(f"{"":5} {str(available.tolist()):<20} {str([0] * num_process):<20}")

    print()

    for i in range(len(process_result)):
        print(f"{process_result[i]:5} {str(work_result[i]):<20} {str(finish_result[i]):<20}")

    print()
    print("====>", state_result)
    print()

    return state_result

def pretend_allocate(a, b, c, d, e):
    allocation = a.copy()
    need = b.copy()
    available = c.copy()
    process_requesting = d
    requesting_resource = e

    if compare(requesting_resource, need[process_requesting]) == False:
        print("Error: Process P" + str(process_requesting) + " has exceeded its maximum claim!")
        sys.exit()

    if compare(requesting_resource, available) == False:
        print("Process P" + str(process_requesting) + " must wait because resources are not available!")
        sys.exit()

    available -= requesting_resource
    allocation[process_requesting] += requesting_resource
    need[process_requesting] -= requesting_resource

    print()
    print("Pretend allocating resource for:", "P" + str(d))
    print("Allocation")
    for i in allocation:
        print(i.tolist())
    print()

    print("Need")
    for i in need:
        print(i.tolist())
    print()

    print("Available")
    print(available.tolist())
    print()

    check = banking_algorithm(allocation, need, available)

    if check == "Safe ✅":
        print("Allocated successfully!")
        return allocation, need, available
    else:
        print("Request cannot be allocated!")
        return None

print()
print("================================ RESULT HERE ============================================")
print()

for i in range(len(p_req)):
    print("Resolving request for:", "P" + str(p_req[i]))
    result = pretend_allocate(alloc, ne, avai, p_req[i], reqr[i])

    if result != None:
        alloc, ne, avai = result

    print()
    print("-----------------------------------------------------------------------------")
    print()