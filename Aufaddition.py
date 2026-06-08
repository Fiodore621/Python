def sum(end):
    total = 0
    for num in range(1, end + 1):
        total += num
    print(f"Die Summe aus allen Zahlen von 1 bis {end} ist {total}.")


sum(100)
sum(int(input("Endpunkt der Addition: ")))
