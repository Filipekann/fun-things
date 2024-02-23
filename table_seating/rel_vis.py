import networkx as nx
import matplotlib.pyplot as plt

guest_relationships = {
'Filip Ekström': ['David Delblanc', 'Felix Jensen', 'Sofie Löfstedt', 'Markus Gerdtsson', 'Felix Blom', 'Oliver Malmberg', 'Louise Öhman', 'Sebastian Palm'], 
'David Delblanc': ['Filip Ekström', 'Felix Jensen', 'Louise Öhman', 'Felix Blom', 'Markus Gerdtsson', 'Oliver Malmberg', 'Sofie Löfstedt'], 
'Felix Jensen': ['Filip Ekström', 'David Delblanc', 'Markus Gerdtsson', 'Felix Blom', 'Sofie Löfstedt', 'Oliver Malmberg', 'Louise Öhman'], 
'Sofie Löfstedt': ['Filip Ekström', 'David Delblanc', 'Felix Jensen', 'Louise Öhman'], 
'Markus Gerdtsson': ['Melinda Widén', 'Oliver Malmberg', 'Filip Ekström', 'Sebastian Palm', 'Pontus Svensson', 'David Delblanc', 'Felix Jensen', 'Felix Blom', 'Johanna Malmborg', 'Emelie Winquist'], 
'Oliver Malmberg': ['Filip Ekström', 'David Delblanc', 'Felix Jensen', 'Markus Gerdtsson', 'Felix Blom', 'Sebastian Palm', 'Johanna Malmborg', 'Pontus Svensson', 'Melinda Widén', 'Emelie Winquist'], 
'Felix Blom': ['Filip Ekström', 'David Delblanc', 'Felix Jensen', 'Markus Gerdtsson', 'Oliver Malmberg', 'Cecilia Ewerlöf'], 
'Sebastian Palm': ['Emelie Winquist', 'Markus Gerdtsson', 'Filip Ekström', 'Oliver Malmberg', 'Pontus Svensson', 'Melinda Widén'], 
'Louise Öhman': ['Filip Ekström', 'David Delblanc', 'Felix Jensen', 'Sofie Löfstedt'], 
'Johanna Malmborg': ['Markus Gerdtsson', 'Oliver Malmberg', 'Pontus Svensson', 'Melinda Widén', 'Emelie Winquist'], 
'Pontus Svensson': ['Markus Gerdtsson', 'Oliver Malmberg', 'Emelie Winquist', 'Melinda Widén', 'Johanna Malmborg', 'Sebastian Palm'], 
'Melinda Widén': ['Emelie Winquist', 'Pontus Svensson', 'Johanna Malmborg', 'Sebastian Palm', 'Oliver Malmberg', 'Markus Gerdtsson'], 
'Cecilia Ewerlöf': ['Felix Blom'], 
'Emelie Winquist': ['Sebastian Palm', 'Melinda Widén', 'Pontus Svensson', 'Johanna Malmborg', 'Oliver Malmberg', 'Markus Gerdtsson']
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for person, relations in guest_relationships.items():
    G.add_node(person)
    for relation in relations:
        G.add_edge(person, relation)

# Plotting the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=800, node_color='skyblue', font_weight='bold', font_size=10, arrowsize=10)
plt.title('Guest Relationships')
plt.show()
