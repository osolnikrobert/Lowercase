# -*- coding: utf-8 -*-
while True:
    print "Pozdravljeni, tu lahko pretvorite kilometre v milje."
    x = int(raw_input("Prosim vnesite število kilometrov: "))
    y = x * 0.621371
    print x, "km je", y, "milj."
    new = raw_input("Želite storiti še kakšno pretvorbo (da/ne): ")
    if new == "ne":
        break

print "Želim vam lep dan, nasvidenje!"
