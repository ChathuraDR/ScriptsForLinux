import re

class SplitMod:
    def splitmod(self, startfrm, ending, strr):

        obj = strr.split(startfrm)  # splitting by start signature

        # adding signature start
        for index, line in enumerate(obj):
            if line.find(signatureEnd) != -1:
                obj[index] = startfrm + line

        # split by starting and ending signature
        for index, line in enumerate(obj):
            matchObj = re.search(r"(.*)%s(.*)%s" % (startfrm, ending), line)
            if matchObj:
                obj[index] = matchObj.group()

        del obj[0]  # remove unwanted 1st string
        return obj  # final array


strr = "aaaaaachrccccccraneeeeeeaaaaaachrccccccraneeeeeeaaaaaachrccccccraneeeeeeaaaaaachrccccccraneeeeee"
signatureStart = 'chr'
signatureEnd = 'ran'

sp = SplitMod()
print(sp.splitmod(signatureStart,signatureEnd,strr))