import numpy as np
import sys

# -------------------------------------------------------
num_process = int(input("Enter number of processes: "))
num_resource_types = int(input("Enter number of resource types: "))

allocation = []
request = []

print("Enter allocation: ")
for i in range(num_process):
    allocation_i = list(map(int, input().split()))

    if len(allocation_i) == 0:
        break

    allocation.append(allocation_i)

print("Enter request: ")
for i in range(num_process):
    request_i = list(map(int, input().split()))

    if len(request_i) == 0:
        break

    request.append(request_i)

allocation = np.array(allocation)
request = np.array(request)

print("Enter available: ")
available = list(map(int, input().split()))
available = np.array(available)

if len(allocation) != num_process or len(request) != num_process or len(available) != num_resource_types:
    print("Invalid input! Ngu vl")
    sys.exit()

for i in range(num_process):
    if len(allocation[i]) != num_resource_types or len(request[i]) != num_resource_types:
        print("Invalid input! Ngu vl")
        sys.exit()

# ----------------------------------------------------------

def compare(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
        
    return True

def equal_to_zero(a):
    for i in a:
        if i != 0:
            return False
    
    return True

work = available.copy()
finish = []

for i in range(num_process):
    if equal_to_zero(allocation[i]) == False or equal_to_zero(request[i]) == False:
        finish.append(0)
    else:
        finish.append(1)

clone_of_initialized_finish = finish.copy()

work_result = []
finish_result = []
process_result = []
state_result = "There is no deadlock! 🎉"

while (True):
    is_found = False

    for i in range(num_process):
        if finish[i] == 0 and compare(request[i], work) == True:
            finish[i] = 1
            work += allocation[i]

            work_result.append(work.copy())
            finish_result.append(finish.copy())
            process_result.append("P" + str(i))
            is_found = True
            break
    
    if is_found == False:
        break

processes_in_deadlock = []

for i in range(len(finish)):
    if finish[i] == 0:
        state_result = "Deadlock 💀"
        processes_in_deadlock.append("P" + str(i))

print()
print("---------------------------------------------------------------")
print(f"{"":5} {"Work":<20} {"Finish":<20}")
print(f"{"":5} {str(available.tolist()):<20} {str(clone_of_initialized_finish):<20}")

print()

for i in range(len(process_result)):
    print(f"{process_result[i]:5} {str(work_result[i]):<20} {str(finish_result[i]):<20}")

print()
print("====>", state_result)
print()