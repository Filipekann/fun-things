import itertools

def create_seating_arrangement(guests, relationships):
    best_arrangement = None
    best_happiness = float('-inf')

    for arrangement in itertools.permutations(guests):
        happiness = calculate_happiness(arrangement, relationships)
        if happiness > best_happiness:
            best_happiness = happiness
            best_arrangement = arrangement

    return best_arrangement

def calculate_happiness(arrangement, relationships):
    happiness = 0
    for i in range(len(arrangement)):
        guest = arrangement[i]
        next_guest = arrangement[(i + 1) % len(arrangement)]
        if next_guest in relationships[guest]:
            happiness += 1
    return happiness

def get_seating_positions(guests, arrangement):
    num_guests = len(guests)
    seating_positions = {}
    for i, guest in enumerate(arrangement):
        position = "Left" if i < num_guests / 2 else "Right"
        seat_number = i + 1 if i < num_guests / 2 else i - num_guests / 2 + 1
        seating_positions[guest] = {"Position": position, "Seat": seat_number}
    return seating_positions

# Example guest list and relationships (you can modify these)
guest_list = ["Filip Ekström", "David Delblanc", "Felix Jensen", "Sofie Löfstedt", "Markus Gerdtsson", "Oliver Malmberg", "Felix Blom", "Sebastian Palm", 
          "Louise Öhman", "Johanna Malmborg", "Pontus Svensson", "Melinda Widén", "Cecilia Ewerlöf", "Emelie Winquist"]
guest_relationships = {
    'Filip Ekström': ['David Delblanc', 'Felix Jensen', 'Sofie Löfstedt', 'Markus Gerdtsson', 'Felix Blom','Oliver Malmberg','Louise Öhman'],
    'David Delblanc': ['Filip Ekström', 'Felix Jensen', 'Louise Öhman', 'Felix Blom','Markus Gerdtsson','Oliver Malmberg'],
    'Felix Jensen': ['Filip Ekström', 'David Delblanc', 'Markus Gerdtsson','Felix Blom'],
    'Sofie Löfstedt': ['Filip Ekström', 'David Delblanc','Felix Jensen'],
    'Markus Gerdtsson': ['Melinda Widén', 'Oliver Malmberg', 'Filip Ekström', 'Sebastian Palm', 'Pontus Svensson','David Delblanc','Felix Jensen','Felix Blom','Johanna Malmborg','Emelie Winquist'],
    'Oliver Malmberg': ["Filip Ekström", "David Delblanc", "Felix Jensen", "Markus Gerdtsson","Felix Blom", "Sebastian Palm", "Johanna Malmborg", "Pontus Svensson", "Melinda Widén", "Emelie Winquist"],
    'Felix Blom': ["Filip Ekström", "David Delblanc", "Felix Jensen","Markus Gerdtsson", "Oliver Malmberg","Cecilia Ewerlöf"],
    'Sebastian Palm': ['Emelie Winquist', "Markus Gerdtsson","Filip Ekström","Oliver Malmberg","Pontus Svensson", "Melinda Widén"],
    'Louise Öhman': ['Filip Ekström', 'David Delblanc', 'Felix Jensen', 'Sofie Löfstedt'],
    'Johanna Malmborg': ['Markus Gerdtsson', 'Oliver Malmberg','Pontus Svensson','Melinda Widén','Emelie Winquist'],
    'Pontus Svensson': ['Markus Gerdtsson', 'Oliver Malmberg','Emelie Winquist','Melinda Widén','Johanna Malmborg','Sebastian Palm'],
    'Melinda Widén': ['Emelie Winquist', 'Pontus Svensson','Johanna Malmborg','Sebastian Palm','Oliver Malmberg','Markus Gerdtsson'],
    'Cecilia Ewerlöf': ['Felix Blom'],
    'Emelie Winquist': ['Sebastian Palm', 'Melinda Widén','Pontus Svensson','Johanna Malmborg','Oliver Malmberg'],
}
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

optimal_arrangement = create_seating_arrangement(guest_list, guest_relationships)
seating_positions = get_seating_positions(guest_list, optimal_arrangement)

print("Optimal seating arrangement:")
for guest in optimal_arrangement:
    print(f"{guest}: Position - {seating_positions[guest]['Position']}, Seat - {seating_positions[guest]['Seat']}")
