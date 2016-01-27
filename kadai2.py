#coding: utf8
i = int(raw_input())
if i/400 == 0:
    print "閏年です。"
else:
    if i/100 == 0:
        print "閏年ではありません。"
    else:
        if i/4 == 0:
            print "閏年です。"
        else:
            print "閏年ではありません。"
 
    
