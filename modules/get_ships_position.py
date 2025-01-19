
import pygame



def get_ships_position(matrix : dict, return_position_ships = True):
    
    rotation_ships_dict = {
        "four" : 1,

        "three1" : 1,
        "three2" : 1,
        
        "two1" : 1,
        "two2" : 1,
        "two3" : 1,

        "one1" : 1,
        "one2" : 1,
        "one3" : 1,
        "one4" : 1,
    }
    
    position_ships_dict = {
        "four" : (100, 50),

        "three1" : (50, 115),
        "three2" : (210, 115),
        
        "two1" : (35, 175),
        "two2" : (155, 175),
        "two3" : (275, 175),

        "one1" : (25, 250),
        "one2" : (125, 250),
        "one3" : (225, 250),
        "one4" : (325, 250),
    }


    writed_ships = {

        "three1" : 1,
        "three2" : 1,
        
        "two1" : 1,
        "two2" : 1,
        "two3" : 1,

        "one1" : 1,
        "one2" : 1,
        "one3" : 1,
        "one4" : 1,
    }


    row_count = 0
    number_count = 0
    

    for row in matrix:
        for number in row:
            if number == 2:


                try:
                    if matrix[row_count][number_count + 1] == 2 or matrix[row_count + 1][number_count] == 2:
                        pass
                except:
                    pass
                else:

                    if writed_ships["one4"] and writed_ships["one1"] == 0 and writed_ships["one2"] == 0 and writed_ships["one3"] == 0:
                        position_ships_dict["one4"] = (row_count, number_count)
                        writed_ships["one4"] = 0

                    if writed_ships["one3"] and writed_ships["one1"] == 0 and writed_ships["one2"] == 0:
                        position_ships_dict["one3"] = (row_count, number_count)
                        writed_ships["one3"] = 0

                    if writed_ships["one2"] and writed_ships["one1"] == 0:
                        position_ships_dict["one2"] = (row_count, number_count)
                        writed_ships["one2"] = 0


                    if writed_ships["one1"]:
                        position_ships_dict["one1"] = (row_count, number_count)
                        writed_ships["one1"] = 0
                    






                try:
                    if matrix[row_count][number_count + 2] == 2 or matrix[row_count + 2][number_count] == 2:
                        pass
                except:
                    pass
                else:                    
                    try:
                        if matrix[row_count][number_count + 1] == 2:
                            pass
                    except:
                        pass

                        if writed_ships["two3"] and writed_ships["two1"] == 0 and writed_ships["two2"] == 0:
                            rotation_ships_dict["two3"] = 0
                            position_ships_dict["two3"] = (row_count, number_count)
                            writed_ships["two3"] = 1  


                        if writed_ships["two2"] and writed_ships["two1"] == 0:
                            rotation_ships_dict["two2"] = 0
                            position_ships_dict["two2"] = (row_count, number_count)
                            writed_ships["two2"] = 1
                            

                        if writed_ships["two1"]:
                            print("work")
                            rotation_ships_dict["two1"] = 0
                            position_ships_dict["two1"] = (row_count, number_count)
                            writed_ships["two1"] = 1

                    try:
                        if matrix[row_count + 1][number_count] == 2:

                            if writed_ships["two3"] and writed_ships["two1"] == 0 and writed_ships["two2"] == 0:
                                rotation_ships_dict["two3"] = 0
                                position_ships_dict["two3"] = (row_count, number_count)
                                writed_ships["two3"] = 0    


                            if writed_ships["two2"] and writed_ships["two1"] == 0:
                                rotation_ships_dict["two2"] = 0
                                position_ships_dict["two2"] = (row_count, number_count)
                                writed_ships["two2"] = 0
                                

                            if writed_ships["two1"]:
                                print("work")
                                rotation_ships_dict["two1"] = 0
                                position_ships_dict["two1"] = (row_count, number_count)
                                writed_ships["two1"] = 0
                    except:
                        pass

                        






                            
                try:
                    if matrix[row_count][number_count + 3] == 2 or matrix[row_count + 3][number_count] == 2:
                        pass
                except:
                    pass
                else:                    
                    try:
                        if matrix[row_count][number_count + 1] == 2:

                            if writed_ships["two2"] and writed_ships["two1"] == 0:
                                rotation_ships_dict["two2"] = 0
                                position_ships_dict["two2"] = (row_count, number_count)
                                writed_ships["two2"] = 1
                                

                            if writed_ships["two1"]:
                                rotation_ships_dict["two1"] = 0
                                position_ships_dict["two1"] = (row_count, number_count)
                                writed_ships["two1"] = 1
                    except:
                        pass


                    try:
                        if matrix[row_count + 1][number_count] == 2:
                            
                            if writed_ships["two3"] and writed_ships["two1"] == 0 and writed_ships["two2"] == 0:
                                rotation_ships_dict["two3"] = 0
                                position_ships_dict["two3"] = (row_count, number_count)
                                writed_ships["two3"] = 0    


                            if writed_ships["two2"] and writed_ships["two1"] == 0:
                                rotation_ships_dict["two2"] = 0
                                position_ships_dict["two2"] = (row_count, number_count)
                                writed_ships["two2"] = 0
                                

                            if writed_ships["two1"]:
                                print("work")
                                rotation_ships_dict["two1"] = 0
                                position_ships_dict["two1"] = (row_count, number_count)
                                writed_ships["two1"] = 0
                    except:
                        pass
                        

                
            
            number_count += 1 
        row_count += 1
        number_count = 0


                    




    if return_position_ships:
        return position_ships_dict
    if not return_position_ships:
        return rotation_ships_dict
    


player_matrix = [
[2, 2, 2, 2, 6, 2, 6, 2, 3, 0],
[3, 3, 3, 3, 6, 2, 6, 2, 3, 0],
[3, 6, 3, 3, 3, 2, 6, 2, 3, 0],
[2, 6, 2, 6, 6, 6, 6, 3, 3, 0],
[2, 6, 2, 6, 2, 3, 0, 0, 0, 0],
[3, 6, 3, 6, 2, 3, 0, 0, 0, 0],
[3, 3, 6, 6, 9, 6, 6, 3, 3, 0],
[3, 2, 6, 2, 6, 2, 6, 2, 3, 0],
[3, 3, 6, 3, 6, 3, 6, 3, 3, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

print(get_ships_position(matrix = player_matrix, return_position_ships= True))
print("")
print(get_ships_position(matrix = player_matrix, return_position_ships= False))
