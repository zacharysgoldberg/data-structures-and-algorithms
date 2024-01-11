# challenge 2

def palindrome(string):
    result = ""
    for i in range(len(string)):
        # left and right pointers
        l = i
        r = i
        while l > 0 and r < len(string) and string[l] == string[r]:
            l -= 1
            r += 1
        # temporary substring to check against
        sub = string[l + 1:r]
        print(sub)
        # print(sub)
        if len(sub) > len(result):
            result = sub

    # print(result)


palindrome("Ilikeracecarsthatanynagofast")

# palindrome("""
#     Fourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceiv
#     edinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedi
#     nagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlo
#     ngendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionoft
#     hatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisalto
#     getherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotco
#     nsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveco
#     nsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongre
#     memberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobed
#     edicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedI
#     tisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonore
#     ddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevoti
#     onthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGod
#     shallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeoplesh
#     allnotperishfromtheearth""")
