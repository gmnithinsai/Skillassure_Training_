import os
import time
import random

class Match:
    def __init__(self, overs):
        self.overs = overs
        self.team_runs = 0
        self.dot_counts = 0
        self.warnings = 0
        self.field_setting_count = 0
        self.wickets_count = 0
        self.boundary_count = 0
        self.balls = 6
        self.bowlers_overs = []
        self.fielder_guess_dir = []
        self.field_pos = []
        self.fielder_pos = []
    # options of captain
    def captain_options(self):
        bowler = input("choose bowler and enter name: ")
        self.bowlers_overs.append(bowler)
        #print(self.bowlers_overs)
        #print(self.bowlers_overs.count(bowler))
        if self.bowlers_overs.count(bowler) > 2:
            self.warnings = self.warnings + 1
            print("Umpire: Hey You exceeded your limit, warnings are added")
        size_bowlers = len(self.bowlers_overs)
        if len(self.bowlers_overs) > 1 and self.bowlers_overs[size_bowlers - 1] == bowler:
            self.warnings += 1
            print("umpire: HEy you should not bowl consecutively, warnings are added")
        return self.warnings
    # fix the fielding or change the fieliding by choosing yes
    def change_field(self):
        chng_field_set = input("Do you want to fix field setting: (enter yes/no below)\n ")
        if chng_field_set == 'yes':
            self.new_field_pos = fielding_position()
            self.field_setting_count += 1
        else:
            pass
        return self.new_field_pos
    # declare functions asks to declare match
    def declare(self):
        self.declare_game = input("Do you want to declare the game here(yes/no): ")
        return self.declare_game
    # starts the innings and returns total score (flow of innings)
    def innings(self):
        wicket_keeper()
        for i in range(self.overs):
            Match.captain_options(self)
            if i > 0:
                declared = Match.declare(self)
                if declared == 'yes':
                    print("The Match has been declared")
                    break
            if i>5:
                limit_change_field = 2
            else:
                limit_change_field = 1
            
            for j in range(self.balls):
                self.field_pos = Match.change_field(self)
                self.batsman_guess = batsman_options()
                clear()
                self.bowler_guess = bowler_options()
                self.wk_guess = wicket_keeper_options()
                self.fielders_guess = fielders_options()
                Match.wicket_scenario(self)
                if self.field_setting_count > limit_change_field:
                    print("Umpire: Hey, The limit to change the field is exceeding and I am giving you warning")
                    self.warnings += 1
                if self.wickets_count == 6:
                    break
                if self.wicket == 'not out':
                    self.score = Match.run_scenarios(self)
                else:
                    self.field_pos = Match.change_field(self)
    
                
            if self.wickets_count == 6:
                print("Umpire: ALL OUT")
                print("Commentators: Wow! what a bowling, They decided, They planned and They executed, made opposite team to ALLout Now we have to see the second innings")
                break
            if self.warnings == 6:
                print("Ummpire: Maximum warnings received please stop play")
                break
            return self.score
    # wickets decisions are taken under this
    def wicket_scenario(self):
        for i in self.fielders_guess:
            self.fielder_guess_dir.append(i[0])
        if self.bowler_guess[0] == self.batsman_guess[0] and self.bowler_guess[-1] == self.batsman_guess[-1]:
            self.wicket = 'bowled'
            self.wickets_count += 1
            print("Umpire: Its clean bowled")
            print("Commentators: OMG what a delivery it is....outstanding delivery, There is no chance for the batsman to read the ball and he has to leave the ground now")
        elif self.batsman_guess[-1] == 6 and self.bowler_guess[0] == self.batsman_guess[0] and self.wk_guess[0] == self.batsman_guess[0]:
            self.wicket = 'stumped'
            self.wickets_count += 1
            print("Umpire: Stumped out")
            print("The batsman wants to hit the ball out of the boundary, He missed it but, Wicket kipper didn't miss and did his work....\n Now the batsman has to go for pavilion")
        elif self.batsman_guess[-1] != 0 and self.batsman_guess[-1] != 1 and self.batsman_guess[-1] != 4 and self.batsman_guess[-1] != 6 and self.batsman_guess[-1] != 2:
            self.wicket = 'Hit wicket'
            self.wickets_count += 1
            print("Umpire: Its a hit wicket")
            print("Commentators: Thats a bad day for the batsman, he got out by himself and we call it as hitwicket")
        elif self.wk_guess[-1] == 2 and self.batsman_guess[-1] == 2 :
            if self.batsman_guess[0] in self.fielder_guess_dir :
                self.wicket = 'runout'
                self.wickets_count += 1
                print("Umpire: Its a runout")
                print("such a wonderful fielding by the fielders what a effort it is!! That effort made opposite team to lose wicket")
        elif self.batsman_guess[0] in self.fielder_pos:
            index = self.fielder_pos.index(self.batsman_guess[0])
            if self.batsman_guess[-1] == 6 and self.fielders_guess[index][-1] == 6:
                self.wicket = 'caught out'
                self.wickets_count += 1
                print("Umpire: Its caught out")
                print("Commentators: what a wonder ful catch it could be one of the best catches i have ever seen and wicket is gone")
        elif self.dot_counts == 3:
            self.wicket = 'LBW'
            self.wickets_count += 1
            print('Umpire: its LBW and its out')
            print("Commentators: Thats a wicket for the team and its LBW and given out by the umpire")
        else:
            self.wicket = 'not out'

    # calculate runs and return total runs to innings
    def run_scenarios(self):
        for fielder in self.field_pos:
                self.fielder_pos.append(fielder[-1])
        if self.batsman_guess[-1] == 0:
            self.dot_counts = self.dot_counts + 1
            self.team_runs = self.team_runs + 0
            
        elif self.batsman_guess[-1] == 1:
            self.dot_counts = 0
            if self.batsman_guess[0] in self.fielder_pos:
                self.team_runs = self.team_runs
            else:
                self.team_runs = self.team_runs + 1
        elif self.batsman_guess[-1] == 2:
            self.dot_counts = 0
            if self.batsman_guess[0] in self.fielder_pos and self.wicket !=  'runout':
                self.team_runs = self.team_runs + 2
            elif self.batsman_guess[0] not in self.fielder_pos and self.bowler_guess[0] == self.batsman_guess[0] or self.wk_guess[0] == self.batsman_guess[0]:
                self.team_runs = self.team_runs + 2
            elif self.batsman_guess[0] not in self.fielder_pos and self.bowler_guess[0] != self.batsman_guess[0] and self.wk_guess[0] != self.batsman_guess[0]:
                self.team_runs = self.team_runs + 3
        elif self.batsman_guess[-1] == 4:
            self.dot_counts = 0
            if self.batsman_guess[0] in self.fielder_pos:
                self.team_runs = self.team_runs + 3
            elif self.batsman_guess[0] in self.fielder_pos:
                self.boundary_count += 1
                self.team_runs = self.team_runs + 4
        elif self.batsman_guess[-1] == 6:
            self.dot_counts = 0
            if self.batsman_guess[0] in self.fielder_pos and self.wicket != 'caught out':
                self.boundary_count += 1
                self.team_runs = self.team_runs + 4
            elif self.batsman_guess[0] not in self.fielder_pos:
                self.boundary_count += 1
                self.team_runs = self.team_runs + 6
        elif self.bowler_guess[-1] > 6 or self.bowler_guess[-1] == 3 or self.bowler_guess[-1] == 5:
            print("Umpire: It's a No ball")
            self.balls += 1
            self.team_runs += 1
        print(self.team_runs)
        return self.team_runs

# fix fielding positon
def fielding_position():
    positions_field = []
    print("""Fielding positions: Slip, Gully, Point,Cover, Mid-off, Mid-on, Long-off, Long-on, Mid-wicket,SquareLeg, FineLeg, ThirdMan""")
    for i in range(4):
        positions_field.append(input(f"Enter fielder {i+1} position and name with space separated values: ").split())
    #print(positions_field)
    return positions_field

# options for batsman
def batsman_options():
    batsman_dir = input("Hey batsman Enter the direction of shot: ")
    batsman_runs = int(input("also, Enter runs you are aiming: "))
    #print(batsman_runs, batsman_dir)
    return batsman_dir, batsman_runs

# options for bowler
def bowler_options():
    bowler_dir = input("Hey bowler, Enter the direction of shot that batsman aim: ")
    bowler_runs = int(input("also guess and Enter runs aiming: "))
    #print(bowler_runs, bowler_dir)
    return bowler_dir, bowler_runs
# options for wicket keeper
def wicket_keeper_options():
    wk_dir = input("Wicket keeper Enter the direction of shot batsman aiming: ")
    wk_runs = int(input("also, Enter runs aiming: "))
    #print(wk_dir,wk_runs)
    return wk_dir, wk_runs
# options for fielder
def fielders_options():
    fielder_opts = []
    for i in range(4):
        fielder_dir = input(f"Hey fielder {i+1} Enter the direction of shot that batsman aiming: ")
        fielder_runs = int(input("also, guess and enter runs aiming: "))
        fielder_opts.append([fielder_dir, fielder_runs])
    #print(fielder_opts)
    return fielder_opts


def wicket_keeper():
    wk = input("Enter wicket keeper name: ")

# Toss function shows who wins the toss
def Toss():
    print("Umpire: Welcome captains")
    time.sleep(1)
    choice = input("Umpire: Team1 choose heads or tails....(Enter below)\n")
    clear()
    result = random.randint(0,1)
    if choice == 'heads':
        choice_int = 0
    else:
        choice_int = 1

    if choice_int == result:
        Toss_win = 'Team1'
        print("Team 1 win the Toss")
    else:
        Toss_win = 'Team2'
        print("Team 2 win the toss")

    innings_choice = input(f"Umpire: okay {Toss_win} which one would you choose bat or bowl: (Enter below) \n")
    return innings_choice, Toss_win

# function  to clear the screen
def clear():
    #print('\033c')
    os.system('cls')

# flow of game
def main():
    Team1 = input("Enter Team name: ")
    Team2  = input("Enter Team name: ")
    overs = int(input("Enter overs: "))
    clear()
    print("Welcome to Gamify")
    time.sleep(1)
    print(f"{Team1} vs {Team2}")
    time.sleep(2)
    clear()
    Toss_summary = Toss()
    clear()
    if Toss_summary[-1] == 'Team1':
        Team = Team1
    else:
        Team = Team2
    if Toss_summary[0] == 'bat':
        Team_first_bat = Team
        if Team != Team1:
            Team_second_bat = Team1
        else:
            Team_second_bat = Team2
    else:
        if Team != Team1:
            Team_first_bat = Team1
            Team_second_bat = Team2
        else:
            Team_first_bat = Team2
            Team_second_bat = Team1
    print(f"Commentators: Hello viewers {Team} won the toss and elected to {Toss_summary[0]} first ")
    print("First Innings Starts............")
    match = Match(overs)
    score_team1 = match.innings()
    if score_team1 != None or match.warnings < 6:
        print("End of first innings....")
        time.sleep(1)
        print("Commentators: so that is the end of the first innings, we need to move on  to second innings")
        print(f"Total score: {score_team1}")
        Team1_boundary_count = match.boundary_count
        time.sleep(5)
        time.sleep(2)
        print("Second Innings starts...............")
        match = Match(overs)
        score_team2 = match.innings()
        print("End of second Innings.......")
        print(f"Total score:{score_team2}")
        Team2_boundary_count = match.boundary_count
        print("Commentators we need to wait for few seconds to declare the winning team")
        time.sleep(4)
        clear()
        if score_team1 > score_team2:
            print(f"Umpire: Team 1 {Team_first_bat}won the match")
            print(f"Congratulations {Team_first_bat}...What a match!! we enjoyed a lot....")
        elif score_team1 < score_team2:
            print(f"Umpire:{Team_second_bat}  won the match")
            print(f"congratulations {Team_second_bat}..........what a match!! we enjoyed a lot.....")
        else:
            print("Umpire: The match has been drawn Now its time for super over")
            super_over = 1
            match = Match(super_over)
            match.innings()
            print("End of first innings....")
            time.sleep(1)
            print("Commentators: so that is the end of the first innings, we need to move on  to second innings")
            print(f"Total score: {score_team1}")
            Team1_boundary_count += match.boundary_count
            time.sleep(4)
            time.sleep(2)
            clear()
            print("Second Innings starts...............")
            match = Match(super_over)
            score_team2 = match.innings()
            print("End of second Innings.......")
            print(f"Total score:{score_team2}")
            Team2_boundary_count += match.boundary_count
            print("Commentators we need to wait for few seconds to declare the winning team")
            time.sleep(6)
            clear()
            if score_team1 > score_team2:
                print(f"Umpire: {Team_first_bat} won the match")
                print(f"Congratulations {Team_first_bat}...What a match!! we enjoyed a lot....")
            elif score_team1 < score_team2:
                print(f"Umpire: Team 2 {Team_second_bat} won the match")
                print(f"Congratulations {Team_second_bat}...What a match!! we enjoyed a lot....")
            else:
                print("Umpire: The match has been drawn")
                print("Commentators: Unbelievable!!! Even the superover is drawn Now its time for boundary counts")
                if Team1_boundary_count < Team2_boundary_count:
                    print(f"Umpire: {Team_second_bat} won the match")
                elif Team1_boundary_count > Team2_boundary_count:
                    print(f" Umpire: {Team_first_bat} won the match")
                else:
                    print("Umpire: The Match has been drawn")
                    print("Commentators: Its unbelievable even the boundaries count is same Now we dont have any option other than Draw")
                    print("Thus the match is draw")
    else:
        if match.warnings >= 6:
            print(f"Umpire: As the warnings exceeded {Team_second_bat} won the match")
            print(f"Commentators bad day for {Team_first_bat}, I think they have learnt about discipline and congratulations to {Team_second_bat}")
        else:
            print(f"Umpire: {Team_second_bat} won the match")
            print()
            print(f"Commentators: Due to unavoidable situations {Team_first_bat} declared the match and good day for {Team_second_bat} and congratulations")

if __name__ == '__main__':
    main()