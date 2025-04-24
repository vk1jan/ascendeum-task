import random

class SnakesAndLadders:
    def __init__(self,grid_size):
        self.grid_size = grid_size
        self.players = 3
        self.position_history = {1:[],2:[],3:[]}
        self.dice_roll_history = {1:[],2:[],3:[]}
        self.current_player_position = {1:0,2:0,3:0}
        self.winner = None
        self.game_finished = False
        
    def get_player_position(self,player_id):
        return self.current_player_position.get(player_id)
        
    def set_player_position(self,player_id,position):
        self.current_player_position[player_id] = position
        return self.current_player_position
    
    def check_move_feasibility(self,player_id,dice_roll_number):
        player_position = self.get_player_position(player_id)
        is_move_possible = player_position + dice_roll_number <= self.grid_size*self.grid_size
        if is_move_possible:
            return (True,player_position + dice_roll_number)
        return (False,None)
        
    def check_cut(self,mover_id,dice_roll_number):
        for i in range(1,self.players+1):
            if i != mover_id:
                player_position = self.get_player_position(i)
                if player_position == self.get_player_position(mover_id) + dice_roll_number:
                    return (True,i)
        return (False,None)
        
    def check_winner(self,player_id):
        if self.get_player_position(player_id) == self.grid_size*self.grid_size:
            self.winner = player_id
            self.game_finished = True
            return True
        return False
    
    def dice_roll(self,player_id):
        dice_roll_number = random.randint(1,6)
        is_move_possible = self.check_move_feasibility(player_id,dice_roll_number)
        if is_move_possible[0]:
            is_cut = self.check_cut(player_id,dice_roll_number)
            if is_cut[0]:
                self.position_history[is_cut[1]].append(0)
                self.set_player_position(is_cut[1],0)
            self.position_history[player_id].append(is_move_possible[1])
            self.dice_roll_history[player_id].append(dice_roll_number)
            self.set_player_position(player_id,is_move_possible[1])

            is_winner = self.check_winner(player_id)
            if is_winner:
                print(f"Player {player_id} has won the game!")
            else:
                print(f"Player {player_id},Dice number {dice_roll_number},Position {self.get_player_position(player_id)}")
            if is_cut[0]:
                print(f"Player {player_id} cut {is_cut[1]}")
                return
        else:
            print("skipped turn below")
            print(f"Player {player_id},Dice number {dice_roll_number},Position {self.get_player_position(player_id)}")
            self.position_history[player_id].append(self.position_history[player_id][-1])
            self.dice_roll_history[player_id].append(dice_roll_number)

        return 
    
    def modify_player_history(self,player_id):
        for idx,pos in enumerate(self.position_history[player_id]):
            if pos!=0:
                row = (pos-1)//self.grid_size
                col = (pos-1)%self.grid_size
                if row%2 == 1:
                    col = (self.grid_size - col -1 )%self.grid_size
                self.position_history[player_id][idx] = (col,row)
            else:
                self.position_history[player_id][idx] = (-1,-1)
        
    
    def simulate_gameplay(self):
        i = 1
        while not self.game_finished:
            player_id = i%self.players
            if player_id == 0:
                player_id = self.players
            self.dice_roll(player_id)
            i += 1
        for j in range(1,self.players+1):
            print(f"Player {j}")
            print("dice roll history",self.dice_roll_history[j])
            print("position history before modification",self.position_history[j])
            self.modify_player_history(j)
            print("position history after modification",self.position_history[j])
        
    
snl = SnakesAndLadders(grid_size=3)
print(snl.simulate_gameplay())


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    