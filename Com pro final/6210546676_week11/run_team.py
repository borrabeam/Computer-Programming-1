from team import *

def find_winner(first_player, second_player):
    hand1 = first_player.get_hand()
    hand2 = second_player.get_hand()
    if hand1 == hand2:
        return 0
    elif hand1 == "Rock" :
        if hand2 == "Scissors":
            return 1
        else :
            return 2
    elif hand1 == "Scissors":
        if hand2 == "Paper":
            return 1
        else: 
            return 2
    elif hand1 =="Paper":
        if hand2 == "Rock":
            return 1
        else:
            return 2

def update_points(winning_team, first_team, second_team):
    if winning_team == 1:
        print("A wins")
        first_team.update_team_points("win")
        second_team.update_team_points("lose")
        
    elif winning_team == 2:
        print("B wins")
        second_team.update_team_points("win")
        first_team.update_team_points("lose")

team_a = Team('team_a.txt','A') 
print(team_a)
team_b = Team('team_b.txt','B') 
print(team_b)

while team_a.get_team_point()< 5 and team_b.get_team_point()<5 :
    team_a.select_player() 
    print(team_a.current_player)
    team_b.select_player() 
    print(team_b.current_player)
    winning_team = find_winner(team_a.current_player, team_b.current_player)
    print(winning_team)

    update_points(winning_team, team_a, team_b)
    print(team_a)
    print(team_b)
if team_a.get_team_point() == 5:
    print("Team A wins!")
elif team_b.get_team_point() == 5:
    print("Team B wins!")