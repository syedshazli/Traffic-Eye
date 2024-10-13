import numpy as np

def create_lines(state_1, state_2):
    output = []
    predict = np.array([])
    if len(state_1) != len(state_2):
        return np.array(output)
    xy1 = np.array([[x+w//2,y+h//2] for x,y,w,h,_ in state_1])
    xy2 = np.array([[x+w//2,y+h//2] for x,y,w,h,_ in state_2])
    velocity = (xy2 - xy1) * 5
    # 1 // (1/5)
    predict = 1 * velocity + xy2
    for current_pos, pred_pos in zip(state_2, predict):
        print(f"{current_pos = } {pred_pos = }")
        x1 = current_pos[0] + current_pos[2]//2
        y1 = current_pos[1] + current_pos[3]//2
        x2 = pred_pos[0]
        y2 = pred_pos[1]
        output.append([[x1,y1], [x2,y2]])
    return output









def predict_positions(state_1, state_2):
    predict = np.array([])
    max_lenth = min(len(state_1), len(state_2))
    # state_1 = state_1[:max_lenth]
    # state_2 = state_2[:max_lenth]
    if len(state_1) != len(state_2):
        return
    
    # state_1_cars = [car for car in state_1]
    # print()
    # print()
    xy1 = np.array([[x+w//2,y+h//2] for x,y,w,h,_ in state_1])
    xy2 = np.array([[x+w//2,y+h//2] for x,y,w,h,_ in state_2])
    # print(xy1)
    # print(xy2)
    # print("+"*80)


    #  (30/(n-1))
    n = 2
    velocity = (xy2 - xy1) * 3

    predict = 1 * velocity + xy2
    predict[0][0] = int(predict[0][0])
    predict[0][1] = int(predict[0][1])
    # print("-"*80)
    # print(predict)
    return predict
    # coords = []

    # for box in a:
        # coords.append()