import json, codecs

with open('/Users/aashishsaini/PycharmProjects/BVR_SUIT/Json/Husqvarna Construction by nitin 13-september (2).json') as fp:
    ds = json.loads(fp.read())
    # print(ds)
try:
    unique_stuff = (list ({each['productUri']: each for each in ds}.values()))
    print(len(unique_stuff))
except:
    pass



# print(len(mem.keys()))
# unique = { each["general"]["model"] : each for each in ds }
# print(unique)
# with open('ATC4JULY(dup_removed).json', 'w') as fp:
#     json.dump(unique_stuff, fp,ensure_ascii=False)
#
# with open('/Users/aashishsaini/PycharmProjects/BVR_SUIT/ATC4JULY(dup_removed).json') as f:
#     ds1 = json.load(f)
#     print("Done")

