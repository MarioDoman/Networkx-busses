import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

G = nx.Graph()

### STATIONS
bus_no_1 = ["Železničná stanica Nitra",	"Rázcestie Autobusová stanica",	"CENTRUM, Mlyny","Fraňa Mojtu",	"Predmostie", "Pod Zoborom",
	"Vinárske závody","Amfiteáter","ZŠ pod Zoborom","Jánskeho","Zariadenie pre seniorov Zobor",	"Strmá","Chmeľová dolina","Urbancova",	
	"Hornozoborská","Klinčeková","Nemocnica Zobor",]

bus_no_32 = ["Gorazdova", "Bohúňova", "Sitnianska", "Poliklinika Chrenová", "Výstavisko", "Andreja Hlinku, Centro", "Univerzity", "CENTRUM, Mlyny",	"Hollého",	
	"Kavcova", "Poliklinika Klokočina", "Mikovíniho", "Čajkovského", "Edisonova", "Bizetova", "Kmeťova", "Murániho", "Tokajská","Viničky"]

bus_no_12 = ["Gorazdova","Bohúňova","Ďurčanského","Atletický štadión","Andreja Hlinku, Centro","Univerzity","CENTRUM, Mlyny","Rázcestie Autobusová stanica",	
	"Rázcestie Železničná stanica","Kasárne Krškany","Rázcestie Priemyselná","Horné Krškany","Nitrafrost","Mevak","ZŠ Krškany","Na Priehon","Dvorčianska",	
	"Nitrianske strojárne","Záborského","Trans Motel","Idea","Ivanka pri Nitre, Texiplast","Ivanka pri Nitre, železničná stanica","Ivanka pri Nitre, kultúrny dom",	
	"Ivanka pri Nitre, Orolská","Ivanka pri Nitre, Luk","Branč, Arkuš","Branč, Veľkoveská","Branč, kultúrny dom","Branč, pneuservis","Branč, Kurucká",	
	"Branč, železničná stanica"
    ]

bus_no_27 = ["Železničná stanica Nitra","Rázcestie Autobusová stanica","Palárikova","Fraňa Mojtu","Predmostie","Pod Zoborom","Rázcestie Panská dolina",
	"Rázcestie Metodova","Metodova","Moskovská","Rázcestie Moskovská","Nitr. Hrnčiarovce, Pod Sokolom","Nitr. Hrnčiarovce, Krajná","Nitr. Hrnčiarovce, ZŠ",
	"Nitr. Hrnčiarovce","Nitr. Hrnčiarovce, Šopronská","Nitr. Hrnčiarovce, vinohrady","Štitáre, Šöpröš","Štitáre, Ku Gáborke","Štitáre"]


def Add_nodes(list1):
    G.add_nodes_from(list1)


def add_edges():
    for x in range(len(bus_no_1)-1): 
        G.add_edge(bus_no_1[x], bus_no_1[x+1], color='red', weight=4)

def add_edges32():
    for x in range(len(bus_no_32)-1): 
        G.add_edge(bus_no_32[x], bus_no_32[x+1], color="blue", weight=4)

def add_edges12():
    for x in range(len(bus_no_12)-1): 
        G.add_edge(bus_no_12[x], bus_no_12[x+1], color="green", weight=4)

def add_edges27():
    for x in range(len(bus_no_27)-1): 
        G.add_edge(bus_no_27[x], bus_no_27[x+1],color="yellow",weight=4)
        


# Creating nodes
Add_nodes(bus_no_1)
Add_nodes(bus_no_32)
Add_nodes(bus_no_12)
Add_nodes(bus_no_27)

# Creating edges
add_edges()
add_edges32()
add_edges12()
add_edges27()

legend_elements = [Line2D([0], [0], color='r', lw=4, label='BUS no. 1'),
                   Line2D([0], [0], color='g', lw=4, label='BUS no. 12'),
                   Line2D([0], [0], color='y', lw=4, label='BUS no. 27'),
                   Line2D([0], [0], color='b', lw=4, label='BUS no. 32')
                   ]

edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
weights = [G[u][v]['weight'] for u,v in edges]
nx.draw(G, with_labels=True, font_size=7, node_size=100, edge_color=colors, width=weights)
plt.legend(handles=legend_elements)
plt.savefig("Graph.png", format="PNG",  dpi=500)
plt.show()
