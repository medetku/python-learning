ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet"
route = ospf_route.replace(",", " ").replace("[", "").replace("]", "")
route = route.split()
route1 = '''
{:25}{}
{:25}{}
{:25}{}
{:25}{}
{:25}{}
'''
print(route1.format(
        "Prefix", route[0],
        "AD/Metric", route[1],
        "Next-Hop", route[3],
        "Last update", route[4],
        "Outbound Interface", route[5],
))

