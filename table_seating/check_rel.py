def check_relationship_consistency(relationships):
    inconsistent_relations = []
    
    for person, relations in relationships.items():
        for relation in relations:
            if person not in relationships.get(relation, []):
                inconsistent_relations.append((person, relation))
                #guest_relationships[relation] = person
    
    return inconsistent_relations

# Sample relationships dictionary
guest_relationships = {'Filip Ekström': ['David Delblanc', 'Felix Jensen', 'Sofie Löfstedt', 'Markus Gerdtsson', 'Felix Blom', 'Oliver Malmberg', 'Louise Öhman', 'Sebastian Palm'], 
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
                 'Emelie Winquist': ['Sebastian Palm', 'Melinda Widén', 'Pontus Svensson', 'Johanna Malmborg', 'Oliver Malmberg', 'Markus Gerdtsson']}

# Check relationship consistency
inconsistent = check_relationship_consistency(guest_relationships)

if inconsistent:
    #print("Inconsistent relationships found:")
    for relation in inconsistent:
        print(f"{relation[0]} and {relation[1]} do not reciprocally list each other in their relationships.")
        guest_relationships[relation[1]].append(relation[0])

else:
    print("Relationships are consistent.")

