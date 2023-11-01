import pygame
import sys
import os

pygame.init()

CutsceneSound = pygame.mixer.Sound("Assets/MainMenu.mp3") #Gives click the value of that sound, can be called in each button.
SCREEN_WIDTH = 800  # Width of the game window
SCREEN_HEIGHT = 600  # Height of the game window
FPS = 60  # Frames per second, used to control the game's frame rate
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create a window with the specified dimensions
pygame.display.set_caption("The Good, The Bad And The Drunk")  # Set the title of the window
clock = pygame.time.Clock()  # Create a clock object to manage updates
CutsceneSound.play()

def Quit(): #Optimization so that this code doesn't need to be called several times for optimization.
    pygame.quit
    sys.exit()

def CutsceneFunc():
    enter_pressed = False #Checks if the enter key has not been pressed
    while not enter_pressed:
        for event in pygame.event.get():  # Check the event queue
            if event.type == pygame.QUIT:  # If the window's close button is clicked
                Quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # If ENTER key is pressed
                enter_pressed = True  # Set the variable to true once the enter button has been pressed to exit the loop and continue

imagecount = 0 #Gives the imagecount a starting point for the image list

def FadeIn(): #Major optimization to save on heavy amounts of code
    global imagecount  # Declare imagecount as global to ensure it works
    imagecount += 1 #Adds 1 to the imagecounter to go through the images
    fade_image(images[imagecount], fade_in=True) #Depending on the value of imagecount will be the image that shows in the list

image_files = ['Assets/MainMenuV3.png', 'Assets/image.jpg', 'Assets/image1.jpg', 'Assets/image2.jpg', 'Assets/image3.jpg', 'Assets/image4.jpg', 'Assets/image5.jpg'] #All images in the cutscene, add more here if you want to expand upon it

# Load images and scale them to the screen size
# This loop goes through each image path, loads the image, applies alpha transparency,
# and scales it to the size of the screen.
images = [pygame.transform.scale(pygame.image.load(image).convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT)) for image in image_files]

# Function to handle image fading
def fade_image(image, fade_in=False):
    # This loop gradually changes the alpha value of the image
    # from transparent to opaque or vice versa, depending on the fade_in if it's true or false
    for alpha in range(0, 256, 2):  # Alpha ranges from 0 to 255
        clock.tick(FPS)  # Control the loop speed to match the frame rate
        image.set_alpha(alpha if fade_in else (255 - alpha))  # Set the new alpha value
        screen.fill((0, 0, 0))  # Fill the screen with black to clear previous images and make the transitions seemless
        screen.blit(image, (0, 0))  # Draw the current image on the screen
        pygame.display.update()  # Update the full display surface to the screen
        pygame.time.delay(3)  # Short delay to smooth out the transition

# Main function to run the cutscene
def run_cutscene():
    # Show the first image on the screen and then updating the display
    screen.blit(images[0], (0, 0))
    pygame.display.flip()  # flip() updates the full screen with new content
    
    initial_delay = 1000  # Delay in milliseconds (1 second)
    start_ticks = pygame.time.get_ticks()  # Record the start time

    while pygame.time.get_ticks() - start_ticks < initial_delay: #Wait until delay is done
        for event in pygame.event.get():  # Process event queue
            if event.type == pygame.QUIT:  # Check for the QUIT event
                Quit()
        clock.tick(FPS)  # Ensure the program maintains the 60 FPS
    
    # Fade out the first image
    fade_image(images[0])

    FadeIn() #Fade_image function but with the fade_in=true and adds 1 to the counter so this is the second image

    CutsceneFunc() #Calls the function to allow the user to press the enter key and keeps them in a loop until they're done reading it for optimization

    fade_image(images[1]) # Fade out the second to make it look more seemless

    FadeIn() #Fades in the 3rd image

    CutsceneFunc()

    fade_image(images[2])

    FadeIn()

    CutsceneFunc()

    fade_image(images[3])

    FadeIn()

    CutsceneFunc()

    fade_image(images[4])

    FadeIn()

    CutsceneFunc()

    fade_image(images[5])

    FadeIn()

    CutsceneFunc()

    pygame.mixer.fadeout(1000)
    fade_image(images[6])

    #add CutsceneFunc() and fade_image(images[CURRENTIMAGE]) for more scenes and add a new one to the list. and a fade out mixer with pygame.quit

    os.system('python main.py') #Runs the Main.py after all cutscenes
run_cutscene() # Start the cutscene program by calling run_cutscene()

