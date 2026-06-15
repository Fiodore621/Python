max = int(input("Maximale Punktzahl: "))
real = int(input("Erreichte Punktzahl: "))

prozent = real * 100 / max
print(f"Es wurden {prozent}% erreicht.")


def note(p):
    if p >= 92:
        return "sehr gut"
    elif p >= 81:
        return "gut"
    elif p >= 67:
        return "befriedigend"
    elif p >= 50:
        return "ausreichend"
    elif p >= 30:
        return "mangelhaft"
    else:
        return "ungenügend"


print(f"Das entspricht der Note: {note(prozent)}.")
