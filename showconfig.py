from re import *

filepath = input('Please Enter the Directory of Configuration File:')
with open(filepath, "r") as file:
    reinterface = compile(r"interface\s.*?/\d{1,3}")
    reipadd = compile(r"no\sip\saddress|ip address\s.*\d{1,3}")
    renameif = compile(r"no\snameif|nameif\s\w?")
    reacl = compile(r'access-list')
    reroute = compile(r'route')
    reobjectnet = compile(r'object\snetwork\s\w+')
    # ip = r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
    configInList = [x.strip() for x in file]
    # for intname in re.findall(interface,config):
    interface = [x.replace('interface ','') for x in configInList if match(reinterface,x)]
    ipadd = [x.strip('ip address') for x in configInList if match(reipadd,x)]
    nameif = [x.replace('nameif ','') for x in configInList if match(renameif,x)]
    acl = [x for x in configInList if match(reacl,x)]
    route = [x for x in configInList if match(reroute,x)]
    numObject = len([configInList.index(x) for x in configInList if match(reobjectnet,x)])
    # objectdetail =

    def show_int():
        print('{:25}{:42}{:25}'.format('Interface name', 'IP address', 'Nameif'))
        for a, b, c in zip(interface, ipadd, nameif):
            print('{:25}{:42}{:25}'.format(a, b, c))

    def show_route():
        print('{:25}{:25}{:25}{:25}{:10}'.format('Outbound Interface', 'IP address', 'Netmask', 'Next Hop IP','Metrix'))
        for x in route:
            routelist = x.split()
            print('{:25}{:25}{:25}{:25}{:10}'.format(routelist[1], routelist[2], routelist[3],routelist[4],routelist[5]))
    def show_object():
        objectindex = [configInList.index(x) for x in configInList if match(reobjectnet, x)]


