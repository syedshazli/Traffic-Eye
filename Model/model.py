import cv2

cap = cv2.VideoCapture(0)



def webcam_photo():
    print(1)
    ret, f = cap.read()
    if not ret:
        raise ValueError("Camera error :(")
    return f


prev_frames = []
while True:
    img = webcam_photo()
    print(img)
    img = rescale(img)
#     prev_frames.append(make_frame(img))
#     sound_alarm = predict(prev_frames[-24])
#     if sound_alarm:
#         alarm()