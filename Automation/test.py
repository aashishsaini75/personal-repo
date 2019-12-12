import json, codecs
#
with open("/Users/aashishsaini/Downloads/Bolzoni 05-nov.json") as fp:
    ds = json.loads(fp.read())
    # print(ds)
    unique_stuff = (list ({each['productUri']: each for each in ds}.values()))
    print((unique_stuff))
with open('/Users/aashishsaini/Downloads/data.json', 'w') as f:
    json.dump(unique_stuff, f)

unique = { each["general"]["model"] : each for each in ds }
print(unique)
with open("/Users/aashishsaini/Downloads/Bolzoni 05-nov.json") as fp:
    json.dump(unique_stuff, fp,ensure_ascii=False)

with open('/Users/aashishsaini/Downloads/data.json') as f:
    ds1 = json.load(f)
    print("Done")