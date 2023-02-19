import json

with open("sample-data.json", "r") as read_file:
    data = json.load(read_file)
    # print(data)
    print("""Interface Status================================================================================""")
    print("""DN                                             Description          Speed                      MTU """)
    for imdata in data["imdata"]:
        for i, k in imdata['l1PhysIf']["attributes"].items():
            if i == 'dn':
                print(k, end="                          ")
            if i == "speed":
                print(k, end="                                         ")
            if i == "mtu":
                print(k, end="                   ")
        print()