smooth_factor = 0.7
prev_x, prev_y = 0, 0

def smooth_point(x, y):
    global prev_x, prev_y
    new_x = prev_x * smooth_factor + x * (1 - smooth_factor)
    new_y = prev_y * smooth_factor + y * (1 - smooth_factor)
    prev_x, prev_y = new_x, new_y
    return int(new_x), int(new_y)
