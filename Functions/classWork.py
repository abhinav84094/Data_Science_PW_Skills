# 1 
pp = ["BJP", "INC", "AAP", "TMC", "NCP"]
ipp = iter(pp)
print(next(ipp))
print(next(ipp))
print(next(ipp))
print(next(ipp))
print(next(ipp))
print()

#  2
print("Q - 2")
ipp = iter(pp)
while True:
    try:
        party = next(ipp)
        print(party)
    except StopIteration:
        print("No more parties to display.")
        break
print()

print("Q - 3")
#  3
def ElectionYears(start, end):
    while start <= end:
        yield start
        start += 5

ey = ElectionYears(2000, 2040)
while True:
    try:
        year = next(ey)
        print(year)
    except StopIteration:
        break
print()


print("Q - 4")
#  4
def PartyMembers(n):
    for i in range(1, n+1):
        yield i


pm = PartyMembers(5)
while True:
    try:
        member = next(pm)
        print(member)
    except StopIteration:
        break
print()


print("Q - 5")
#  5
def slogans():
    yield "Vote for Development (BJP)"
    yield "Har Ghar Congress (INC)"
    yield "Sabka Hoga Vikas (AAP)"

slog = slogans()
while True:
    try:
        slogan = next(slog)
        print(slogan)
    except StopIteration:
        break
print()


print("Q - 6")
#  6
names = ["Rahul Gandhi", "Narendra Modi", "Arvind Kejriwal"]
def candidate_names(names):
    i=0
    while i<len(names):
        yield names[i]
        i+=1  

cn = candidate_names(names)
print(next(cn))
print()


print("Q - 7")
#  7
parties = ["BJP", "INC", "AAP"]
def generateSlogan(parties):
    i = 0
    while i < len(parties):
        yield "Vote for " + parties[i]
       

partySlogan = generateSlogan(parties)
print(next(partySlogan))
print(next(partySlogan))
print(next(partySlogan))
print() 


print("Q - 8" )
#  8
def party_list():
    return ["BJP", "INC", "AAP", "TMC", "NCP"]

parties = party_list()

def party_gen():
    for party in parties:
        yield party


print(parties)

p = party_gen()
print(next(p))
print(next(p))
print(next(p))
print(next(p))


print(parties.__sizeof__())
print(p.__sizeof__())
print()


print("Q - 9")
#  9
def regional_parties():
    rp = ["DMK", "TDP", "Shiv Sena"]
    for party in rp:
        yield party

def national_parties():
    np = ["BJP", "INC", "CPI"] 
    for party in np:
        yield party

def all_parties():
    yield from regional_parties()
    yield from national_parties()

parties = all_parties()
while True:
    try:
        party = next(parties)
        print(party)
    except StopIteration:
        break

print()


print("Q - 10")
#  10
def party_symbols():
    symbols = {
        "BJP": "Lotus",
        "INC": "Hand",
        "AAP": "Broom"
    }
    for party, symbol in symbols.items():
        yield (party, symbol)

ps = party_symbols()
print(next(ps))