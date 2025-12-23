sequence = input("num: ")

best_seq = ""
current_seq = ""

for i in range(len(sequence)):
    if i == 0 or int(sequence[i]) == int(sequence[i-1]) + 1:
        current_seq += sequence[i]
    else:
        current_seq = sequence[i]
    
    if len(current_seq) > len(best_seq):
        best_seq = current_seq

print(best_seq)
