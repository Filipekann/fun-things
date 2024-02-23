import networkx as nx
import random

# Define the relationships
relationships = {
    'Filip Ekström': ['David Delblanc', 'Felix Jensen', 'Sofie Löfstedt', 'Markus Gerdtsson', 'Felix Blom', 'Oliver Malmberg', 'Louise Öhman'],
    'David Delblanc': ['Filip Ekström', 'Felix Jensen', 'Louise Öhman', 'Felix Blom', 'Markus Gerdtsson', 'Oliver Malmberg'],
    'Felix Jensen': ['Filip Ekström', 'David Delblanc', 'Markus Gerdtsson', 'Felix Blom'],
    'Sofie Löfstedt': ['Filip Ekström', 'David Delblanc', 'Felix Jensen'],
    'Markus Gerdtsson': ['Melinda Widén', 'Oliver Malmberg', 'Filip Ekström', 'Sebastian Palm', 'Pontus Svensson', 'David Delblanc', 'Felix Jensen', 'Felix Blom', 'Johanna Malmborg', 'Emelie Winquist'],
    'Oliver Malmberg': ["Filip Ekström", "David Delblanc", "Felix Jensen", "Markus Gerdtsson", "Felix Blom", "Sebastian Palm", "Johanna Malmborg", "Pontus Svensson", "Melinda Widén", "Emelie Winquist"],
    'Felix Blom': ["Filip Ekström", "David Delblanc", "Felix Jensen", "Markus Gerdtsson", "Oliver Malmberg", "Cecilia Ewerlöf"],
    'Sebastian Palm': ['Emelie Winquist', "Markus Gerdtsson", "Filip Ekström", "Oliver Malmberg", "Pontus Svensson", "Melinda Widén"],
    'Louise Öhman': ['Filip Ekström', 'David Delblanc', 'Felix Jensen', 'Sofie Löfstedt'],
    'Johanna Malmborg': ['Markus Gerdtsson', 'Oliver Malmberg', 'Pontus Svensson', 'Melinda Widén', 'Emelie Winquist'],
    'Pontus Svensson': ['Markus Gerdtsson', 'Oliver Malmberg', 'Emelie Winquist', 'Melinda Widén', 'Johanna Malmborg', 'Sebastian Palm'],
    'Melinda Widén': ['Emelie Winquist', 'Pontus Svensson', 'Johanna Malmborg', 'Sebastian Palm', 'Oliver Malmberg', 'Markus Gerdtsson'],
    'Cecilia Ewerlöf': ['Felix Blom'],
    'Emelie Winquist': ['Sebastian Palm', 'Melinda Widén', 'Pontus Svensson', 'Johanna Malmborg', 'Oliver Malmberg'],
}

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
for person, friends in relationships.items():
    G.add_node(person)
    G.add_edges_from((person, friend) for friend in friends)

# Randomly shuffle the nodes and attempt to find a valid seating arrangement
attempts = 1000  # You can adjust the number of attempts
for _ in range(attempts):
    permutation = list(G.nodes())
    random.shuffle(permutation)

    valid_arrangement = True
    for i, person in enumerate(permutation):
        known_people = set(relationships[person])
        neighbors = set(G.neighbors(person))
        unknown_people = neighbors - known_people

        if i == 0 or i == len(permutation) - 1:
            if len(unknown_people) == 0:
                valid_arrangement = False
                break
        else:
            if len(unknown_people) < 2 or (permutation[i - 1] in unknown_people and permutation[i + 1] in known_people):
                valid_arrangement = False
                break

    if valid_arrangement:
        print("Optimal seating arrangement:", permutation)
        break
    else:
        print("Attempt failed:", permutation)