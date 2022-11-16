# Change dataset

import csv
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


def save_csv(rows):
    with open('resources/data.csv', 'a', newline='') as file:
        write = csv.writer(file)
        write.writerow(rows)


def save_gesture(name, size=200):
    frames_saved = 0
    print('Prepare your gesture')
    print('Wait until the webcam window get close')

    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
            max_num_hands=1,
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Save landmarks
            if results.multi_hand_landmarks:
                points = []
                for hand in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style()
                    )

                    for hand_point in hand.landmark:
                        points.append(hand_point.x)
                        points.append(hand_point.y)

                points.append(name)
                save_csv(points)
                frames_saved += 1

            # Flip the image horizontally for a selfie-view display.
            cv2.imshow('Wait until this window get close', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break

            # Count data
            if size == frames_saved:
                break
        cap.release()
