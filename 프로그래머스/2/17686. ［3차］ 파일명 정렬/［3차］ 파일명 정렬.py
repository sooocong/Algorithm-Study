def solution(files):
    parsed = []

    for idx, file in enumerate(files):
        head = ""
        number = ""
        i = 0
        while i < len(file) and not file[i].isdigit():
            head += file[i]
            i += 1

        while i < len(file) and file[i].isdigit():
            number += file[i]
            i += 1

        parsed.append((head.lower(), int(number), idx, file))
    
    parsed.sort()
    
    return [file for _, _, _, file in parsed]