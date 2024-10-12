import numpy as np

def predict_positions(state_1, state_2):
    predict = np.array([])
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
    velocity = (xy2 - xy1)/(1/29.97) 
    predict = xy2 + velocity*1
    # print("-"*80)
    # print(predict)
    return predict
    # coords = []

    # for box in a:
        # coords.append()

