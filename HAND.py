import cv2
import mediapipe 
import pyautogui

capture_hands = mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
camera = cv2.VideoCapture(0)
x1 = y1 = x2 = y2 = 0
while True:
    _,image = camera.read()
    image_height, image_width, _ = image.shape
    image = cv2.flip(image,1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output_hands = capture_hands.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image, hand)
            one_hand_landmarks = hand.landmark
            for id, lm in enumerate(one_hand_landmarks):    
                X = int (lm.x * image_width)
                Y = int (lm.y * image_height)
               #print(X, Y)

                if id == 8:
                    mouse_X = int(screen_width / image_width * X)
                    mouse_Y = int(screen_width / image_width * Y)
                    cv2.circle(image, (X,Y), 10, (255,255,255))
                    pyautogui.moveTo(mouse_X,mouse_Y )
                    x1 = X
                    y1 = Y
                if id == 4:
                    x2 = X
                    y2 = Y
                    cv2.circle(image, (X,Y), 10, (255,255,255))
               
        dist = y2 - y1
        print(dist)
        if(dist < 40):
            pyautogui.click()

    cv2.imshow("Imagem", image)
    key = cv2.waitKey(1)
   
    if key == 27:
        break

camera.realease()
cv2.destroyAllWindows()