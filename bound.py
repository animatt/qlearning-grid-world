#!/usr/local/bin/python3

def bound(image, position, new_pos) :
    position = tuple(position)
    new_pos = tuple(new_pos)
    if new_pos[0] < image.shape[0] :
        if image[new_pos[0], new_pos[1]] == 1 :
            state_not_terminal = True
            return (state_not_terminal, new_pos)
        elif image[new_pos[0], new_pos[1]] == 0 :
            state_not_terminal = True
            return (state_not_terminal, position)
        elif new_pos[0] == 0 :
            state_not_terminal = False
            return (state_not_terminal, new_pos)
        else : # back to start line
            state_not_terminal = True
            return (state_not_terminal, new_pos)
    else : # out of bounds
        state_not_terminal = True
        return (state_not_terminal, position)
