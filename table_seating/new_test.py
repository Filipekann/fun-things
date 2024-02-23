import random

guest_list = ["Filip Ekström", "David Delblanc", "Felix Jensen", "Sofie Löfstedt", "Markus Gerdtsson", "Oliver Malmberg", "Felix Blom", "Sebastian Palm", 
          "Louise Öhman", "Johanna Malmborg", "Pontus Svensson", "Melinda Widén", "Cecilia Ewerlöf", "Emelie Winquist"]
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

sorted_guest_relationships = {
'Markus Gerdtsson': ['Melinda Widén', 'Oliver Malmberg', 'Filip Ekström', 'Sebastian Palm', 'Pontus Svensson', 'David Delblanc', 'Felix Jensen', 'Felix Blom', 'Johanna Malmborg', 'Emelie Winquist'], 
'Oliver Malmberg': ['Filip Ekström', 'David Delblanc', 'Felix Jensen', 'Markus Gerdtsson', 'Felix Blom', 'Sebastian Palm', 'Johanna Malmborg', 'Pontus Svensson', 'Melinda Widén', 'Emelie Winquist'], 
'Filip Ekström': ['David Delblanc', 'Felix Jensen', 'Sofie Löfstedt', 'Markus Gerdtsson', 'Felix Blom', 'Oliver Malmberg', 'Louise Öhman', 'Sebastian Palm'], 
'David Delblanc': ['Filip Ekström', 'Felix Jensen', 'Louise Öhman', 'Felix Blom', 'Markus Gerdtsson', 'Oliver Malmberg', 'Sofie Löfstedt'], 
'Felix Jensen': ['Filip Ekström', 'David Delblanc', 'Markus Gerdtsson', 'Felix Blom', 'Sofie Löfstedt', 'Oliver Malmberg', 'Louise Öhman'], 
'Felix Blom': ['Filip Ekström', 'David Delblanc', 'Felix Jensen', 'Markus Gerdtsson', 'Oliver Malmberg', 'Cecilia Ewerlöf'], 
'Sebastian Palm': ['Emelie Winquist', 'Markus Gerdtsson', 'Filip Ekström', 'Oliver Malmberg', 'Pontus Svensson', 'Melinda Widén'], 
'Pontus Svensson': ['Markus Gerdtsson', 'Oliver Malmberg', 'Emelie Winquist', 'Melinda Widén', 'Johanna Malmborg', 'Sebastian Palm'], 
'Melinda Widén': ['Emelie Winquist', 'Pontus Svensson', 'Johanna Malmborg', 'Sebastian Palm', 'Oliver Malmberg', 'Markus Gerdtsson'], 
'Emelie Winquist': ['Sebastian Palm', 'Melinda Widén', 'Pontus Svensson', 'Johanna Malmborg', 'Oliver Malmberg', 'Markus Gerdtsson'], 
'Johanna Malmborg': ['Markus Gerdtsson', 'Oliver Malmberg', 'Pontus Svensson', 'Melinda Widén', 'Emelie Winquist'], 
'Sofie Löfstedt': ['Filip Ekström', 'David Delblanc', 'Felix Jensen', 'Louise Öhman'], 
'Louise Öhman': ['Filip Ekström', 'David Delblanc', 'Felix Jensen', 'Sofie Löfstedt'], 
'Cecilia Ewerlöf': ['Felix Blom']
} 


l_s_table = []
r_s_table = []
table = [l_s_table,r_s_table]


def sort_relationships_by_length(relationships):
    sorted_relationships = dict(sorted(relationships.items(), key=lambda x: len(x[1]), reverse=True))
    return sorted_relationships

    
#sorted_guest_relationships = sort_relationships_by_length(guest_relationships)


def arrange_optimal_seating(sorted_relationships):
    guests = list(sorted_relationships.keys())
    table_length = len(guests) // 2

    # Initialize left and right sides of the table
    left_side = guests[:table_length]
    right_side = guests[table_length:]

    # Function to check if two guests are close
    def are_close(guest1, guest2):
        return (guest1 in sorted_relationships[guest2] or
                guest2 in sorted_relationships[guest1] or
                abs(guests.index(guest1) - guests.index(guest2)) <= 1)

    # Iterate through guests to seat them close to their relations
    for _ in range(len(guests)):
        for guest in guests:
            side = left_side if guest in left_side else right_side
            opposite_side = right_side if side is left_side else left_side

            relations = sorted_relationships[guest]

            for relation in relations:
                if relation in opposite_side:
                    index = opposite_side.index(relation)
                    potential_positions = [index - 1, index, index + 1]
                    for pos in potential_positions:
                        if 0 <= pos < len(side) and not are_close(side[pos], guest):
                            side.remove(guest)
                            side.insert(pos, guest)
                            break

    return left_side, right_side


def check_happines(left_side,right_side):
    tot_happines = 0
    average_happines = 0
    l_s_h = []
    r_s_h = []
    e_has_one_friend = True

    for i in range(len(left_side)-1):
        l_s_h.append(0)
        if not i-1 < 0:
            if left_side[i-1] in sorted_guest_relationships[left_side[i]]:
                tot_happines += 1
                l_s_h[i]+= 1
            if right_side[i-1] in sorted_guest_relationships[left_side[i]]:
                tot_happines += 1
                l_s_h[i]+= 1
        if right_side[i] in sorted_guest_relationships[left_side[i]]:
            tot_happines += 1
            l_s_h[i]+= 1
        if not i + 1 >= len(left_side):
            if left_side[i+1] in sorted_guest_relationships[left_side[i]]:
                tot_happines += 1
                l_s_h[i]+= 1
            if right_side[i+1] in sorted_guest_relationships[left_side[i]]:
                tot_happines += 1
                l_s_h[i]+= 1
        if e_has_one_friend and l_s_h[i] != 0:
            pass
        else:
            e_has_one_friend = False

    i = 0
    for i in range(len(right_side)-1):
        r_s_h.append(0)
        if not i-1 < 0:
            if right_side[i-1] in sorted_guest_relationships[right_side[i]]:
                tot_happines += 1
                r_s_h[i]+= 1
            if left_side[i-1] in sorted_guest_relationships[right_side[i]]:
                tot_happines += 1
                r_s_h[i]+= 1
        if left_side[i] in sorted_guest_relationships[right_side[i]]:
            tot_happines += 1
            r_s_h[i]+= 1
        if not i + 1 >= len(right_side):
            if right_side[i+1] in sorted_guest_relationships[right_side[i]]:
                tot_happines += 1
                r_s_h[i]+= 1
            if left_side[i+1] in sorted_guest_relationships[right_side[i]]:
                tot_happines += 1
                r_s_h[i]+= 1
        
        if e_has_one_friend and r_s_h[i] != 0:
            pass
        else:
            e_has_one_friend = False

    return tot_happines, l_s_h, r_s_h, e_has_one_friend

def randomize_guest_lists(guest_list):
    # Shuffle the original guest list
    random.shuffle(guest_list)
    
    # Calculate the midpoint to split the list into two equal parts
    midpoint = len(guest_list) // 2
    
    # Split the shuffled list into two randomized lists
    randomized_list_1 = guest_list[:midpoint]
    randomized_list_2 = guest_list[midpoint:]
    
    return randomized_list_1, randomized_list_2



def create_random_good():
    bolean = True
    while bolean:
        rand_l_guest_l, rand_r_guest_l = randomize_guest_lists(guest_list)

        total_happines, left_side_happines, right_side_happines, everyone_happy = check_happines(rand_l_guest_l, rand_r_guest_l)


        if everyone_happy and total_happines <= 14:
            return rand_l_guest_l, rand_r_guest_l
            
  
if __name__ == '__main__':
    # Create optimal seating arrangement
    #l_s_table, r_s_table = arrange_optimal_seating(sorted_guest_relationships)

    l_s_table, r_s_table = create_random_good()

    total_happines, left_side_happines, right_side_happines, everyone_happy = check_happines(l_s_table,r_s_table)

    print(f"Tot happines: {total_happines} \nEveryone happy: {everyone_happy}\n{left_side_happines} \n{right_side_happines}")