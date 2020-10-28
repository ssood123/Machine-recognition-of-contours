%% testing initialization
clear
clc
classifierName = input('What is the name of the classifer you want to test? ','s');
load([classiferName, '.mat']);
%% test contour circle

imageNumber = 1;
resultMatrix = zeros(1,3);
for i = 1:100
    testImagePath = append('C:\Users\Owner\Desktop\SinhaLab\importantImages\contourCircleTest\zContourCircle',int2str(imageNumber),'.png');
    testImage = imread(testImagePath);
    ds = augmentedImageDatastore(imageSize, testImage, 'ColorPreprocessing', 'gray2rgb');
    testImageFeatures = activations(net, ds, featureLayer, 'MiniBatchSize', 32, 'OutputAs', 'columns');
    label = predict(classifier, testImageFeatures, 'ObservationsIn', 'columns');
    if label == 'circle1'
        resultMatrix(1,1) = resultMatrix(1,1) + 1;
    elseif label == 'square1'
        resultMatrix(1,2) = resultMatrix(1,2) + 1;
    elseif label == 'none1'
        resultMatrix(1,3) = resultMatrix(1,3) + 1;
    end
    imageNumber = imageNumber + 1;
end
disp('contour circle');
disp(resultMatrix);

%% test natural filled circle 

imageNumber = 1;
resultMatrix = zeros(1,3);
for i = 1:100
    testImagePath = append('C:\Users\Owner\Desktop\SinhaLab\importantImages\naturalFilledCircleTest\zNaturalCircle',int2str(imageNumber),'.png');
    testImage = imread(testImagePath);
    ds = augmentedImageDatastore(imageSize, testImage, 'ColorPreprocessing', 'gray2rgb');
    testImageFeatures = activations(net, ds, featureLayer, 'MiniBatchSize', 32, 'OutputAs', 'columns');
    label = predict(classifier, testImageFeatures, 'ObservationsIn', 'columns');
    if label == 'circle1'
        resultMatrix(1,1) = resultMatrix(1,1) + 1;
    elseif label == 'square1'
        resultMatrix(1,2) = resultMatrix(1,2) + 1;
    elseif label == 'none1'
        resultMatrix(1,3) = resultMatrix(1,3) + 1;
    end
    imageNumber = imageNumber + 1;
end
disp('natural filled circle');
disp(resultMatrix);

%% test natural outline circle 

imageNumber = 1;
resultMatrix = zeros(1,3);
for i = 1:100
    testImagePath = append('C:\Users\Owner\Desktop\SinhaLab\importantImages\naturalOutlineCircleTest\zNaturalCircle',int2str(imageNumber),'.png');
    testImage = imread(testImagePath);
    ds = augmentedImageDatastore(imageSize, testImage, 'ColorPreprocessing', 'gray2rgb');
    testImageFeatures = activations(net, ds, featureLayer, 'MiniBatchSize', 32, 'OutputAs', 'columns');
    label = predict(classifier, testImageFeatures, 'ObservationsIn', 'columns');
    if label == 'circle1'
        resultMatrix(1,1) = resultMatrix(1,1) + 1;
    elseif label == 'square1'
        resultMatrix(1,2) = resultMatrix(1,2) + 1;
    elseif label == 'none1'
        resultMatrix(1,3) = resultMatrix(1,3) + 1;
    end
    imageNumber = imageNumber + 1;
end
disp('natural outline circle');
disp(resultMatrix);
%% test contour square

imageNumber = 1;
resultMatrix = zeros(1,3);
for i = 1:100
    testImagePath = append('C:\Users\Owner\Desktop\SinhaLab\importantImages\contourSquareTest\zContourSquare',int2str(imageNumber),'.png');
    testImage = imread(testImagePath);
    ds = augmentedImageDatastore(imageSize, testImage, 'ColorPreprocessing', 'gray2rgb');
    testImageFeatures = activations(net, ds, featureLayer, 'MiniBatchSize', 32, 'OutputAs', 'columns');
    label = predict(classifier, testImageFeatures, 'ObservationsIn', 'columns');
    if label == 'circle1'
        resultMatrix(1,1) = resultMatrix(1,1) + 1;
    elseif label == 'square1'
        resultMatrix(1,2) = resultMatrix(1,2) + 1;
    elseif label == 'none1'
        resultMatrix(1,3) = resultMatrix(1,3) + 1;
    end
    imageNumber = imageNumber + 1;
end
disp('contour square');
disp(resultMatrix);

%% test natural filled square 

imageNumber = 1;
resultMatrix = zeros(1,3);
for i = 1:100
    testImagePath = append('C:\Users\Owner\Desktop\SinhaLab\importantImages\naturalFilledSquareTest\zNaturalSquare',int2str(imageNumber),'.png');
    testImage = imread(testImagePath);
    ds = augmentedImageDatastore(imageSize, testImage, 'ColorPreprocessing', 'gray2rgb');
    testImageFeatures = activations(net, ds, featureLayer, 'MiniBatchSize', 32, 'OutputAs', 'columns');
    label = predict(classifier, testImageFeatures, 'ObservationsIn', 'columns');
    if label == 'circle1'
        resultMatrix(1,1) = resultMatrix(1,1) + 1;
    elseif label == 'square1'
        resultMatrix(1,2) = resultMatrix(1,2) + 1;
    elseif label == 'none1'
        resultMatrix(1,3) = resultMatrix(1,3) + 1;
    end
    imageNumber = imageNumber + 1;
end
disp('natural filled square');
disp(resultMatrix);

%% test natural outline square

imageNumber = 1;
resultMatrix = zeros(1,3);
for i = 1:100
    testImagePath = append('C:\Users\Owner\Desktop\SinhaLab\importantImages\naturalOutlineSquareTest\zNaturalSquare',int2str(imageNumber),'.png');
    testImage = imread(testImagePath);
    ds = augmentedImageDatastore(imageSize, testImage, 'ColorPreprocessing', 'gray2rgb');
    testImageFeatures = activations(net, ds, featureLayer, 'MiniBatchSize', 32, 'OutputAs', 'columns');
    label = predict(classifier, testImageFeatures, 'ObservationsIn', 'columns');
    if label == 'circle1'
        resultMatrix(1,1) = resultMatrix(1,1) + 1;
    elseif label == 'square1'
        resultMatrix(1,2) = resultMatrix(1,2) + 1;
    elseif label == 'none1'
        resultMatrix(1,3) = resultMatrix(1,3) + 1;
    end
    imageNumber = imageNumber + 1;
end
disp('natural outline square');
disp(resultMatrix);
%% test contour none

imageNumber = 1;
resultMatrix = zeros(1,3);
for i = 1:100
    testImagePath = append('C:\Users\Owner\Desktop\SinhaLab\importantImages\contourNoneTest\zContourNone',int2str(imageNumber),'.png');
    testImage = imread(testImagePath);
    ds = augmentedImageDatastore(imageSize, testImage, 'ColorPreprocessing', 'gray2rgb');
    testImageFeatures = activations(net, ds, featureLayer, 'MiniBatchSize', 32, 'OutputAs', 'columns');
    label = predict(classifier, testImageFeatures, 'ObservationsIn', 'columns');
    if label == 'circle1'
        resultMatrix(1,1) = resultMatrix(1,1) + 1;
    elseif label == 'square1'
        resultMatrix(1,2) = resultMatrix(1,2) + 1;
    elseif label == 'none1'
        resultMatrix(1,3) = resultMatrix(1,3) + 1;
    end
    imageNumber = imageNumber + 1;
end
disp('contour none');
disp(resultMatrix);

%% test natural none

imageNumber = 1;
resultMatrix = zeros(1,3);
for i = 1:100
    testImagePath = append('C:\Users\Owner\Desktop\SinhaLab\importantImages\naturalNoneTest\zNaturalNone',int2str(imageNumber),'.png');
    testImage = imread(testImagePath);
    ds = augmentedImageDatastore(imageSize, testImage, 'ColorPreprocessing', 'gray2rgb');
    testImageFeatures = activations(net, ds, featureLayer, 'MiniBatchSize', 32, 'OutputAs', 'columns');
    label = predict(classifier, testImageFeatures, 'ObservationsIn', 'columns');
    if label == 'circle1'
        resultMatrix(1,1) = resultMatrix(1,1) + 1;
    elseif label == 'square1'
        resultMatrix(1,2) = resultMatrix(1,2) + 1;
    elseif label == 'none1'
        resultMatrix(1,3) = resultMatrix(1,3) + 1;
    end
    imageNumber = imageNumber + 1;
end
disp('natural none');
disp(resultMatrix);
