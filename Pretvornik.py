# -*- coding: utf-8 -*-
print "Pozdravljeni, tu lahko pretvorite kilometre v milje."
x = int(raw_input("Prosim vnesite število kilometrov: "))
y = x * 0.621371
print x, "km je", y ,"milj."
print "Želite storiti še kakšno pretvorbo (da/ne)?"
a = raw_input()
while a=="da":
    x = int(raw_input("Prosim vnesite število kilometrov: "))
    print x, "km je", y, "milj."
    print "Želite storiti še kakšno pretvorbo?"
    a = raw_input()
else :
    print "Želim vam lep dan, nasvidenje!"