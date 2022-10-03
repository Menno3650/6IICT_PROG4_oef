from sys import exec_prefix


engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }

nieuw = ""

zin = input("Geef een zin in het engels: ").split(" ")
for woord in zin:
    try:
        nieuw += f"{engels_nederlands[woord]} "
    except:
        nieuw += f"{woord} "

print(nieuw)