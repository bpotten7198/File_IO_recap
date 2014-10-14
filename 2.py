#Write a program which takes a list of six names and writes them to a file. Check that the file contains the six names on six separate lines.
Names = ["Potato","is","love",",","potato","is","life"]
with open("Shoppinglist.txt", mode="w",encoding="utf-8") as SwegLikeNames:
    for x in Names:
          SwegLikeNames.write(x+" ")
