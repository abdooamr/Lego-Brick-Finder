# Python program to identify
#color in images

# Importing the libraries OpenCV and numpy
import cv2
import numpy as np

# Read the images
img = cv2.imread("Lego_Color_Bricks.jpg")

# Resizing the image
image = cv2.resize(img, (600, 500))

# Convert Image to Image HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Set range for red color and
# define mask
red_lower = np.array([0, 100, 20])
red_upper = np.array([10, 255, 255])
red_lower2 = np.array([160, 100, 20])
red_upper2 = np.array([180, 255, 255])
red_mask1 = cv2.inRange(hsv, red_lower, red_upper)
red_mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
full_mask = red_mask1 + red_mask2;
# Set range for green color and
# define mask
green_lower = np.array([30, 85, 20])
green_upper = np.array([80, 255, 255])
green_mask = cv2.inRange(hsv, green_lower, green_upper)
# Set range for blue color and
# define mask
blue_lower = np.array([100, 50, 50])
blue_upper = np.array([140, 255, 255])
blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
# Set range for black color and
# define mask
black_lower = np.array([0, 0, 0])
black_upper = np.array([250, 300, 72])
black_mask = cv2.inRange(hsv, black_lower, black_upper)

# Set range for yellow color and
# define mask
yellow_lower = np.array([16, 100, 100])
yellow_upper = np.array([30, 255, 255])
yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)

# Set range for white color and
# define mask
white_lower = np.array([0, 0, 0])
white_upper = np.array([97, 120, 150])
white_mask = cv2.inRange(hsv, white_lower, white_upper)



res_red = cv2.bitwise_and(image, image,  mask = full_mask)
res_green = cv2.bitwise_and(image, image, mask=green_mask)
res_blue = cv2.bitwise_and(image, image, mask=blue_mask)
res_black = cv2.bitwise_and(image, image,  mask = black_mask)
res_yellow = cv2.bitwise_and(image, image,  mask = yellow_mask)
res_white = cv2.bitwise_and(image, image,  mask = white_mask)






number_of_white_pix_red = np.sum(full_mask == 255)
if number_of_white_pix_red ==0:
    cv2.putText(full_mask, ' The shape color is not red', (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 0, 0))

else:
    cv2.putText(full_mask, 'The area is: ' + str(number_of_white_pix_red), (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 0, 0))
    cv2.putText(full_mask, ' The shape color is red', (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 0, 0))

number_of_white_pix_green = np.sum(green_mask == 255)
if number_of_white_pix_green ==0:
    cv2.putText(green_mask, ' The shape color is not green', (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 0, 0))

else:
    cv2.putText(green_mask, 'The area is: ' + str(number_of_white_pix_green), (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 0, 0))
    cv2.putText(green_mask, ' The shape color is green', (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 0, 0))

number_of_white_pix_blue = np.sum(blue_mask == 255)
if number_of_white_pix_blue ==0:
    cv2.putText(blue_mask, ' The shape color is not blue', (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 0, 0))

else:
    cv2.putText(blue_mask, 'The area is: ' + str(number_of_white_pix_blue), (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 0, 0))
    cv2.putText(blue_mask, ' The shape color is blue', (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 0, 0))

number_of_white_pix_black = np.sum(black_mask == 255)
if number_of_white_pix_black == 0:
    cv2.putText(black_mask, ' The shape color is not black', (20, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.0, (255, 0, 0))
else:
    cv2.putText(black_mask, 'The area is: ' + str(number_of_white_pix_black), (20, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.0, (255, 0, 0))
    cv2.putText(black_mask, ' The shape color is black', (20, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.0, (255, 0, 0))
number_of_white_pix_yellow = np.sum(yellow_mask == 255)
if number_of_white_pix_yellow == 0:

    cv2.putText(yellow_mask, ' The shape color is not yellow', (20, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.0, (255, 0, 0))
else:
     cv2.putText(yellow_mask, 'The area is: ' + str(number_of_white_pix_yellow), (20, 50),
     cv2.FONT_HERSHEY_SIMPLEX,
     1.0, (255, 0, 0))
     cv2.putText(yellow_mask, ' The shape color is yellow', (20, 100),
     cv2.FONT_HERSHEY_SIMPLEX,
     1.0, (255, 0, 0))
number_of_white_pix_white = np.sum(white_mask == 255)
if number_of_white_pix_white == 0:

    cv2.putText(white_mask, ' The shape color is not white', (20, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.0, (255, 0, 0))
else:
     cv2.putText(white_mask, 'The area is: ' + str(number_of_white_pix_white), (20, 50),
     cv2.FONT_HERSHEY_SIMPLEX,
     1.0, (255, 0, 0))
     cv2.putText(white_mask, ' The shape color is white', (20, 100),
     cv2.FONT_HERSHEY_SIMPLEX,
     1.0, (255, 0, 0))


# Display Image and Mask
#cv2.imshow("Image", image)
#cv2.imshow("Mask", white_mask)
#.imshow("Red_Mask", full_mask1)
#cv2.imshow("Mask", yellow_mask)
# Make python sleep for unlimited time
#cv2.waitKey(0)


def menu():
    print('(1) Red Color Detection')
    print('(2) Green Color Detection')
    print('(3) Blue Color Detection')
    print('(4) Black Color Detection')
    print('(5) Yellow Color Detection')
    print('(6) White Color Detection')
    print('(0) Exit the program')

menu()
option = int(input('Enter your option here: '))


while option != 0:

    if option == 1:
        cv2.imshow("Image", image)
        cv2.imshow("Red mask",full_mask)
        cv2.waitKey(0)
    elif option == 2:
        cv2.imshow("Image", image)
        cv2.imshow("green mask", green_mask)
        cv2.waitKey(0)
    elif option == 3:
        cv2.imshow("Image", image)
        cv2.imshow("blue mask", blue_mask)
        cv2.waitKey(0)
    elif option == 4:
        cv2.imshow("Image", image)
        cv2.imshow("black mask", black_mask)
        cv2.waitKey(0)
    elif option == 5:
        cv2.imshow("Image", image)
        cv2.imshow("yellow mask", yellow_mask)
        cv2.waitKey(0)
    elif option == 6:
        cv2.imshow("Image", image)
        cv2.imshow("white mask", white_mask)
        cv2.waitKey(0)
    else:
        print('invalid opion.')

    print()
    menu()
    option = int(input('Enter your option here: '))