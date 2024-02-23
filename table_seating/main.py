import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add people as nodes
people = [
    'Alice',
    'Bob',
    'Charlie',
    'David',
    'Emma',
    'Frank',
]

guests = ["Filip Ekström", "David Delblanc", "Felix Jensen", "Sofie Löfstedt", "Markus Gerdtsson", "Oliver Malmberg", "Felix Blom", "Sebastian Palm", 
          "Louise Öhman", "Johanna Malmborg", "Pontus Svensson", "Melinda Widén", "Cecilia Ewerlöf", "Emelie Winquist"]




# Define relationships (edges)
relationships = [
('Filip Ekström', 'David Delblanc'),
    ('David Delblanc', 'Filip Ekström'),
    ('Felix Jensen', 'David'),
    ('Sofie Löfstedt', 'Filip Ekström'),
    ('Markus Gerdtsson', 'Filip Ekström'),
    ('Oliver Malmberg', 'Filip Ekström'),
    ('Felix Blom', 'Filip Ekström'),
    ('Sebastian Palm', 'Markus Gerdtsson'),
    ('Louise Öhman', 'David Delblanc'),
    ('Johanna Malmborg', 'Frank'),
    ('Pontus Svensson', 'Frank'),
    ('Melinda Widén', 'David Delblanc'),
    ('Cecilia Ewerlöf', 'Felix Blom'),
    ('Emelie Winquist', 'Markus Gerdtsson'),
]

rel = [
('Alice', 'Bob'),
    ('Alice', 'Charlie'),
    ('Alice', 'David'),
    ('Bob', 'Emma'),
    ('Charlie', 'David'),
    ('Emma', 'Frank'),
]


if __name__ == '__main__':

    G.add_nodes_from(guests)

    # Add relationships as edges
    G.add_edges_from(relationships)

    # Plot the graph
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_weight='bold')
    plt.title('People and Their Relations at Dinner')
    plt.show()