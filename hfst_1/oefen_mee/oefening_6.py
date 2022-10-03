engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }

def vind_key(woord):
    for keys, values in engels_nederlands.items():
        if values == woord:
            return keys
    return woord

nieuw = ""

zin = input("Geef een zin: ").split(" ")
for woord in zin:
    try:
        nieuw += f"{engels_nederlands[woord]} "
        
    except:
        nieuw += f"{vind_key(woord)} "

print(nieuw)