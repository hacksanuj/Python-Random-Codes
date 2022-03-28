days= int(input("ENter days::"))

y = int(days / 365)
w = int((days % 365) / 7)
d = int((days-((y *365) + (w * 7))))

print("\nYEARS:",y)
print("\nWeeks:",w)
print("\nDays :",d)