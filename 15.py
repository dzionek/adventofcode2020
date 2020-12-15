data = [20, 9, 11, 0, 1, 2]

# Part A and B together
history = {}
i = 0
last = None
while i != 30000000:
    i += 1
    if i > len(data):
        last_row = history.get(last)
        if last_row and len(last_row) == 2:
            last = last_row[1] - last_row[0]
        else:
            last = 0
        history_last = history.get(last)
        if not history_last:
            history[last] = [i]
        else:
            if len(history_last) == 2:
                history[last][0] = history[last][1]
                history[last][1] = i
            else:
                history[last] += [i]
    else:
        last = data[i-1]
        history[last] = [i]

    if i == 2020:
        print(last)

print(last)
