import pygame
import math
import random
import os

def main():
  random.seed();
  typeOfContour = input("Enter the type of contour you want (circle/square/none): ");
  numberOfSavedImages = int(input("Enter the number of saved images: "));
  startingIndexOfImages = int(input("Enter the starting index of the images: "));
  filledShape = input('Do you want your superimposed shapes to be filled? (filled/outline/random) ');
  typeOfImages = input("Type of images? (train/test) ");
  locationOfSavedImage = input("Location of saved images? ");
  for i in range(0,numberOfSavedImages):
    pygame.init();
    screen = pygame.display.set_mode((256,256));
    screen.fill((255,255,255));
    imageSet = 1
    if imageSet == 1:
      imageNumber = str(random.randint(1,300)).zfill(3);
      try:
        Img = pygame.image.load("C:\\Users\\Owner\\Desktop\\ImageSet1\\imagesets\\nature\\N" + str(imageNumber) + ".jpg");
      except:
        Img = pygame.image.load("C:\\Users\\Owner\\Desktop\\ImageSet1\\imagesets\\nature\\N" + str(imageNumber) + ".bmp");
    elif imageSet == 2:
      possibleCategories = ["airplane","car","cat","dog","flower","motorbike"];
      selectedCategory = random.choice(possibleCategories);
      if selectedCategory == "airplane":
        imageNumber = str(random.randint(0,726)).zfill(4);
        Img = pygame.image.load("C:\\Users\\Owner\\Desktop\\ImageSet2\\natural_images\\airplane\\airplane_" + str(imageNumber) + ".jpg");
      elif selectedCategory == "car":
        imageNumber = str(random.randint(0,967)).zfill(4);
        Img = pygame.image.load("C:\\Users\\Owner\\Desktop\\ImageSet2\\natural_images\\car\\car_" + str(imageNumber) + ".jpg");
      elif selectedCategory == "cat":
        imageNumber = str(random.randint(0,884)).zfill(4);
        Img = pygame.image.load("C:\\Users\\Owner\\Desktop\\ImageSet2\\natural_images\\cat\\cat_" + str(imageNumber) + ".jpg");
      elif selectedCategory == "dog":
        imageNumber = str(random.randint(0,701)).zfill(4);
        Img = pygame.image.load("C:\\Users\\Owner\\Desktop\\ImageSet2\\natural_images\\dog\\dog_" + str(imageNumber) + ".jpg");
      elif selectedCategory == "flower":
        imageNumber = str(random.randint(0,842)).zfill(4);
        Img = pygame.image.load("C:\\Users\\Owner\\Desktop\\ImageSet2\\natural_images\\flower\\flower_" + str(imageNumber) + ".jpg");
      elif selectedCategory == "motorbike":
        imageNumber = str(random.randint(0,787)).zfill(4);
        Img = pygame.image.load("C:\\Users\\Owner\\Desktop\\ImageSet2\\natural_images\\motorbike\\motorbike_" + str(imageNumber) + ".jpg");      

    Img = pygame.transform.scale(Img,(256,256));
    screen.blit(Img,(0,0));

    randomColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255));
    if filledShape == 'filled':
      filled = 0;
    elif filledShape == 'outline':
      filled = 1;
    elif filledShape == 'random':
      filled = random.randint(0,1);
    
    #Coordinates are relative to the origin in the bottom left corner of the screen
    if typeOfContour == "circle":
      center = [16*random.randint(7,10),256-16*random.randint(7,10)];
      radius = 16*random.randint(3,5)
      pygame.draw.circle(screen,randomColor,center,radius,filled);
    elif typeOfContour == "square":
      xBottomLeft = random.randint(2,5);
      yBottomLeft = random.randint(2,5);
      maxNum = max([xBottomLeft,yBottomLeft]);
      lengthOfSide = 16*random.randint(7,16-maxNum-2);
      xBottomLeft = 16 * xBottomLeft;
      yBottomLeft = 16 * yBottomLeft;
      dimensions = [xBottomLeft,yBottomLeft,lengthOfSide,lengthOfSide];
      pygame.draw.rect(screen,randomColor,dimensions,filled);

    nameOfSavedImage = "Natural" + typeOfContour.capitalize() + str(startingIndexOfImages) + ".png";
    pygame.display.update();

    if typeOfImages == "train":    
      pygame.image.save(screen,"C:\\Users\\Owner\\Desktop\\SinhaLab\\importantImages\\" + locationOfSavedImage + "\\" + "a" + nameOfSavedImage);
    elif typeOfImages == "test":    
      pygame.image.save(screen,"C:\\Users\\Owner\\Desktop\\SinhaLab\\importantImages\\" + locationOfSavedImage + "\\" + "z" + nameOfSavedImage);
  
    startingIndexOfImages = startingIndexOfImages + 1;

if __name__ == "__main__":
  main();
