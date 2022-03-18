from matplotlib import scale
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

### BUSSES
busses_list = [1,2,4,6,7,8,9,10]

### STATIONS
bus_no_1 = ["Železničná stanica Nitra",	"Rázcestie Autobusová stanica",	"CENTRUM, Mlyny","Fraňa Mojtu",	"Predmostie", "Pod Zoborom",
	"Vinárske závody","Amfiteáter","ZŠ pod Zoborom","Jánskeho","Zariadenie pre seniorov Zobor",	"Strmá","Chmeľová dolina","Urbancova",	
	"Hornozoborská","Klinčeková","Nemocnica Zobor",]

bus_no_2 = ["Kmeťova","Bizetova","Edisonova","Golianova","Nedbalova","Mestská hala","Kostolná","Tehelná","Dolnočermánska","Murgašova",
	"Stavebná škola","Rázcestie Železničná stanica","Rázcestie Autobusová stanica","CENTRUM, Mlyny","Univerzity","Andreja Hlinku","Centro",	
	"Nábrežie mládeže","Lomnická","Pod Zoborom","Amfiteáter","ZŠ pod Zoborom","Veterinárska","Šindolka", "Dolnohorská"]

bus_no_4 = [
    "Kmeťova","Bizetova","Edisonova","Golianova","Nedbalova","Mestská hala","Kostolná","Tehelná","Dolnočermánska","Murgašova","Stavebná škola",	
	"Rázcestie Železničná stanica","Rázcestie Autobusová stanica","CENTRUM, Mlyny","Univerzity","Andreja Hlinku, Centro","Nábrežie mládeže",
	"Lomnická","Pod Zoborom","Amfiteáter","ZŠ pod Zoborom","Veterinárska","Šindolka, Dolnohorská","Priemyselný park VII","Priemyselný park IV",	
	"Priemyselný park V","Priemyselný park III","Priemyselný park II","Priemyselný park I","Rázcestie Priemyselný park","PD Dražovce",
	"Pri kríži","Belopotockého","Dražovce"]

bus_no_6 = ["Gorazdova","Bohúňova","Ďurčanského","Chrenovský cintorín","Vašinova","Chrenovská, MAX","Pod Zoborom","Predmostie","Fraňa Mojtu",
	"Palárikova","CENTRUM, Mlyny","Hollého","Kavcova","Poliklinika Klokočina","Mikovíniho","ZŠ Škultétyho","Mestská hala","Nedbalova","Golianova",
	"Edisonova"]


def Add_nodes(list1):
    G.add_nodes_from(list1)


def add_edges():
    for edge in bus_no_1: 
        G.add_edge(edge, busses_list[0])

def add_edges2():
    for edge in bus_no_2: 
        G.add_edge(edge, busses_list[1])

def add_edges3():
    for edge in bus_no_4: 
        G.add_edge(edge, busses_list[2])

def add_edges4():
    for edge in bus_no_6: 
        G.add_edge(edge, busses_list[3])
        


# Creating_nodes_list(10)
Add_nodes(bus_no_1)
add_edges()
add_edges2()
add_edges3()
add_edges4()


color_map = []

for node in G:
    if node == 1 or node == 2 or node == 4 or node == 6:
        color_map.append('red')
    else: 
        color_map.append('lightblue')   


# pos = nx.spring_layout(G, scale=9)
# nx.draw(G, node_color=color_map, node_size=600, with_labels = True, pos=pos,font_size=10)

pos = nx.spring_layout(G, k=0.8)
nx.draw(G, pos , with_labels = True, width=0.4, node_color=color_map, node_size=400)


plt.show()
