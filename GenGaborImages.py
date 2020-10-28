#Note: For square contours, contourScaleFactor = 90, tolerance = 0. For circle contours, contourScaleFactor = 50, tolerance = 10.
import pygame
import math
import random

#Global variables
circleCoordinateArray = [];
squareCoordinateArray = [];

#Functions
#Records the coordinates of upper left corner of the the actual elements (which are squares) of the circle. (x,y) are relative to the origin at the bottom left corner of the screen.
def recordCoordinate(x,y,screenHeight):
  #y = screenHeight - y;
  circleCoordinateArray.append([x,y]);
  

#Bresenham's algorithm generates 1/8th of a circle (i.e., quadrant 1) and generates the rest using symmetry. This function draws quadrants 2 to 8 of the circle while quadrant 1 is being drawn
def symPlot(xc, yc, x, y,screenHeight):
  recordCoordinate(xc + x , yc + y,screenHeight);
  recordCoordinate(xc - x, yc + y,screenHeight);
  recordCoordinate(xc + x, yc - y,screenHeight);
  recordCoordinate(xc - x, yc - y,screenHeight);
  recordCoordinate(xc + y, yc + x,screenHeight);
  recordCoordinate(xc - y, yc + x,screenHeight);
  recordCoordinate(xc + y, yc - x,screenHeight);
  recordCoordinate(xc - y, yc - x,screenHeight);
  

#Bresenham's algorithm to generate a (discrete) circle
def bresenham(xc,yc,r,contourScaleFactor,screenHeight):
  x = 0;
  y = r;
  d = (3 * contourScaleFactor) - (2 * r);
  symPlot(xc,yc,x,y,screenHeight);
  while x <= y:
    if d <= 0:
      d = d + (4 * x) + (6 * contourScaleFactor);
    else:
      d = d + (4 * x) - (4 * y) + (10 * contourScaleFactor);
      y = y - contourScaleFactor;
    x = x + contourScaleFactor;
    symPlot(xc, yc, x, y,screenHeight);

#An glorithm to generate a (discrete) square and record its coordinates. All coordinates are relative to the origin in the bottom left corner of the screen.
def generateSquare(xBottomLeft,yBottomLeft,numOfElementsOnSide,contourScaleFactor):
  xTemp = xBottomLeft+contourScaleFactor;
  yTemp = yBottomLeft+contourScaleFactor;
  for i in range (0,numOfElementsOnSide-2):
    squareCoordinateArray.append([xTemp,yTemp]); #Bottom portion of square
    xTemp = xTemp + contourScaleFactor;
  
  xTemp = xBottomLeft;
  yTemp = yBottomLeft + 2*contourScaleFactor;
  for i in range (0,numOfElementsOnSide-2):
    squareCoordinateArray.append([xTemp+(numOfElementsOnSide-1)*contourScaleFactor,yTemp]); #Right portion of square
    yTemp = yTemp + contourScaleFactor;
  
  xTemp = xBottomLeft + contourScaleFactor;
  yTemp = yBottomLeft + contourScaleFactor;
  for i in range (0,numOfElementsOnSide-2):
    squareCoordinateArray.append([xTemp,yTemp+(numOfElementsOnSide-1)*contourScaleFactor]); #Top portion of square
    xTemp = xTemp + contourScaleFactor;

  xTemp = xBottomLeft;
  yTemp = yBottomLeft + 2*contourScaleFactor;
  for i in range(0,numOfElementsOnSide-2):
    squareCoordinateArray.append([xTemp,yTemp]); #Left portion of square
    yTemp = yTemp + contourScaleFactor;

 
#Takes an image, rotates it by a number of degrees, and displays the image at (x,y). (x,y) defines the center (not the upper left corner) of the image and it is relative to the origin
#at the bottom left corner of the screen. 
def rotateAndDisplayImage(image,rotationAngle,x,y,screenHeight,screen):
  img = pygame.transform.rotate(image,rotationAngle);
  centerOfimg = img.get_rect().center;
  y = screenHeight - y;
  screen.blit(img,(x-centerOfimg[0],y-centerOfimg[1]));
  pygame.display.update();


#the function that generates the images
def generateImages(typeOfContour,xc,yc,r,xBottomLeft,yBottomLeft,numOfElementsOnSide,nameOfSavedImage, displayGridLines, displayContour, displayNoise, typeOfImages, locationOfSavedImage):
  #Reset  the coordinate array lists
  circleCoordinateArray.clear();
  squareCoordinateArray.clear();
  #Adjustable settings used for contour generation
  #General settings
  screenWidth = 256;
  screenHeight = 256;
  contourScaleFactor = 16; #the length of the side of the element of a contour
  backgroundColor = (128,128,128);
  #Noise Settings
  Gabor_image1 = pygame.image.load("C:\\Users\\Owner\\Desktop\\SinhaLab\\importantImages\\Gabor1.png"); #By default, the orientation of this gabor element (and all other images) is 0 degrees
  Gabor_image2 = pygame.image.load("C:\\Users\\Owner\\Desktop\\SinhaLab\\importantImages\\Gabor2.png");
  Gabor_image3 = pygame.image.load("C:\\Users\\Owner\\Desktop\\SinhaLab\\importantImages\\Gabor3.png");
  Gabor_image4 = pygame.image.load("C:\\Users\\Owner\\Desktop\\SinhaLab\\importantImages\\Gabor4.png");
  percentDisplayed = 60;
  wobble = 1;

  #Intialize pygame and the background
  pygame.init();
  screen = pygame.display.set_mode((screenWidth,screenHeight));
  screen.fill(backgroundColor);
  pygame.display.update();

  #Generate the noise (a 2d field of a set number of randomly oriented Gabor elements). Each noise element lies in the center of a grid element
  possibleNoiseXs = [];
  possibleNoiseYs = [];
  noiseCoordinates = []; #A 2d array that stores information for each gabor element in the noise. It stores [x position, y position, orientation, image number]
  temp = contourScaleFactor/2;
  while temp < screenWidth:
    possibleNoiseXs.append(temp);
    temp = temp + contourScaleFactor
  temp = contourScaleFactor/2;
  while temp < screenHeight:
    possibleNoiseYs.append(temp);
    temp = temp + contourScaleFactor;
  
  NumElementsToBeAdded= round(256*percentDisplayed/100);
  possibleNoise = [];
  for i in possibleNoiseXs:
    for j in possibleNoiseYs:
      possibleNoise.append([i,j]);
  for i in range(0,10):
    random.shuffle(possibleNoise);
  for i in range(0,NumElementsToBeAdded):
    noiseCoordinates.append([possibleNoise[i][0],possibleNoise[i][1],random.randint(0,360),random.randint(1,4)]);



  if typeOfContour == "circle":
    #Generate the discrete circle using bresenham's algorithm
    bresenham(xc,yc,r,contourScaleFactor,screenHeight);

    #As of now, each noise element has a random orientation. We must check to see with elements are within the contour and set their orientation to that of the slope of the contour.
    #In other words, they must be aligned with the contour.
    count = 0;
    for a in noiseCoordinates:
      for b in circleCoordinateArray:
        if ((b[0] < a[0]) and (b[0] + contourScaleFactor > a[0]) and (b[1] - contourScaleFactor < a[1]) and (b[1]  > a[1])):
          xDist = (b[0] + b[0] + contourScaleFactor)/2 - xc;
          yDist = (b[1] + b[1] - contourScaleFactor)/2 - yc;
          #In calculus, the slope of an origin-centered circle at a point (x,y) on the circle's diameter is -x/y
          slope = -xDist/yDist;
          angle = math.atan(slope)*180/math.pi;
          noiseCoordinates[count][2] = angle;
          break;
      count = count + 1;

  elif typeOfContour == "square":
    #Generate the discrete square
    generateSquare(xBottomLeft,yBottomLeft,numOfElementsOnSide,contourScaleFactor);

    #As of now, each noise element has a random orientation. We must check to see with elements are within the contour and set their orientation to that of the slope of the contour.
    #In other words, they must be aligned with the contour.
    count = 0;
    for a in noiseCoordinates:
      for b in squareCoordinateArray:
        if ((b[0] < a[0]) and (b[0] + contourScaleFactor > a[0] ) and (b[1] - contourScaleFactor < a[1]) and (b[1] > a[1])):
            if b[1] == yBottomLeft+contourScaleFactor: #If the element lies along the bottom side of the square contour
              angle = 0;
            elif b[0] == xBottomLeft+(numOfElementsOnSide-1)*contourScaleFactor:  #If the element lies along the right side of the square contour
              angle = 90;
            elif b[1] == yBottomLeft+contourScaleFactor+(numOfElementsOnSide-1)*contourScaleFactor: #If the element lies along the top side of the square contour
              angle = 0;
            elif b[0] == xBottomLeft: #If the element lies along the left side of the square contour
              angle = 90;
            noiseCoordinates[count][2] = angle;
            #noiseCoordinates[count][3] = 2;
            break;
      count = count + 1;
   

  #Now, each noise element should have a slight wobble. That is, there should potentially be a 1 or 2 pixel offset from its orginal position.
  for a in range(0,len(noiseCoordinates)):
    noiseCoordinates[a][0] = noiseCoordinates[a][0] + random.randint(-1*wobble,wobble);
    noiseCoordinates[a][1] = noiseCoordinates[a][1] + random.randint(-1*wobble,wobble);


  #Possibly generate and draw the grid lines
  if displayGridLines == True:
    x = 0;
    while x*contourScaleFactor < screenWidth:
      pygame.draw.line(screen,(0,0,0),(x*contourScaleFactor,0),(x*contourScaleFactor,screenHeight));
      x = x + 1;
    pygame.display.update();
    y = 0;
    while y*contourScaleFactor < screenHeight:
      pygame.draw.line(screen,(0,0,0),(0,screenHeight-y*contourScaleFactor),(screenWidth,screenHeight-y*contourScaleFactor));
      y = y + 1;
    pygame.display.update();

  #Possibly draw the contour
  if displayContour == True:
    if typeOfContour == "circle":
      for i in circleCoordinateArray:
        pygame.draw.rect(screen,(255,255,255),[i[0],screenHeight-i[1],contourScaleFactor,contourScaleFactor]);
    elif typeOfContour == "square":
      for i in squareCoordinateArray:
        pygame.draw.rect(screen,(255,255,255),[i[0],screenHeight-i[1],contourScaleFactor,contourScaleFactor]);
    pygame.display.update();

  #Possible display the noise gabor elements on the screen according to the information in noiseCoordinates
  if displayNoise == True:
    for i in noiseCoordinates:
      if i[3] == 1:
        rotateAndDisplayImage(Gabor_image1,i[2],i[0],i[1],screenHeight,screen);
      elif i[3] == 2:
        rotateAndDisplayImage(Gabor_image2,i[2],i[0],i[1],screenHeight,screen);
      elif i[3] == 3:
        rotateAndDisplayImage(Gabor_image3,i[2],i[0],i[1],screenHeight,screen);
      elif i[3] == 4:
        rotateAndDisplayImage(Gabor_image4,i[2],i[0],i[1],screenHeight,screen);
  
  if typeOfImages == "train":    
    pygame.image.save(screen,"C:\\Users\\Owner\\Desktop\\SinhaLab\\importantImages\\" + locationOfSavedImage + "\\" + "a" + nameOfSavedImage);
  elif typeOfImages == "test":    
    pygame.image.save(screen,"C:\\Users\\Owner\\Desktop\\SinhaLab\\importantImages\\" + locationOfSavedImage +  "\\" + "z" + nameOfSavedImage);

#Main function
def main():
  #Enter settings for the generated images
  typeOfContour = input("Enter the type of contour you want (circle/square/none): ");
  numberOfSavedImages = int(input("Enter the number of saved images: "));
  startingIndexOfImages = int(input("Enter the starting index of the images: "));
  typeOfImages = input("Type of images? (train/test) ");
  locationOfSavedImage = input("Location of saved images? ");
  displayGridLines = input("Display grid lines? (yes/no) ");
  if displayGridLines == "yes":
    displayGridLines = True;
  else:
    displayGridLines = False;
  displayContour = input("Display the contour? (yes/no) ");
  if displayContour == "yes":
    displayContour = True;
  else:
    displayContour = False;
  displayNoise = input("Display the noise? (yes/no) ");
  if displayNoise == "yes":
    displayNoise = True;
  else:
    displayNoise = False;
  
  #Based on the entered settings, generate images. If a certain type of contour is specified, the contour will have a random position and random dimensions in each image.
  #It is ensured that the contour is not too big for the image, too.
  random.seed();
  contourScaleFactor = 16;
  nameOfSavedImage = "";
  xc = 0;
  yc = 0;
  r = 0;
  xBottomLeft = 0;
  yBottomLeft = 0;
  numOfElementsOnSide = 0;
  for i in range(0,numberOfSavedImages):
    nameOfSavedImage = "Contour" + typeOfContour.capitalize() + str(startingIndexOfImages) + ".png";
    if typeOfContour == "circle":
      xc = contourScaleFactor*random.randint(7,10);
      yc = contourScaleFactor*random.randint(7,10);
      r = contourScaleFactor*random.randint(3,5);
    elif typeOfContour == "square":
      xBottomLeft = random.randint(2,5);
      yBottomLeft = random.randint(2,5);
      maxNum = max([xBottomLeft,yBottomLeft]);
      numOfElementsOnSide = random.randint(7,16-maxNum-2);
      xBottomLeft = contourScaleFactor * xBottomLeft;
      yBottomLeft = contourScaleFactor * yBottomLeft;
    elif typeOfContour == "none":
      displayContour = False;
    generateImages(typeOfContour,xc,yc,r,xBottomLeft,yBottomLeft,numOfElementsOnSide,nameOfSavedImage, displayGridLines, displayContour, displayNoise, typeOfImages, locationOfSavedImage);
    startingIndexOfImages = startingIndexOfImages + 1;


if __name__ == "__main__":
  main();



