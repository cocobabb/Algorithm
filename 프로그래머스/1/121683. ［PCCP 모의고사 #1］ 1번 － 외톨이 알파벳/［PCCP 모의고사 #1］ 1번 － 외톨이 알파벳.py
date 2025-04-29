def solution(input_string):
    last = input_string[0]
    alones = set()
    previous = {last}

    for current in input_string[1:]:
        if last == current:
            continue

        if current in previous:
            alones.add(current)
        else:
            previous.add(current)

        last = current

    if not alones:
        return "N"

    return "".join(sorted(alones))