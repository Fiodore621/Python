sentence = "This is a common interview question"
char_frequency = {}  # leeres Dictionary
for char in sentence:
    if char in char_frequency:  # ist der Buchstabe im Dictionary?
        char_frequency[char] += 1  # dann auf den Value +1
    else:
        # sonst, hinzufügen und den Value auf 1 setzen
        char_frequency[char] = 1


char_frequency_sorted = sorted(  # definition einer sortierten Liste
    char_frequency.items(),  # die Key-Value-Pairs von char_frequency als Tuples
    # nimmt zum sortieren den Index 1 der kv-pairs (die Frequency)
    key=lambda kv: kv[1],
    reverse=True  # kehrt die Liste um, damit der größte Wert vorne steht
)

print(char_frequency_sorted[0])
