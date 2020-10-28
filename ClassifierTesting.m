%% Initialization
clear
clc
typeofnet = input('What classifier do you want to use? (alexnet, resnet50, googlenet) ','s');
if strcmp(typeofnet,'alexnet')
    net = alexnet();
elseif strcmp(typeofnet,'resnet50')
    net = resnet50();
elseif strcmp(typeofnet,'googlenet')
    net = googlenet();
else
    disp('Not a valid input');
end

trainingSet = imageDatastore({'C:\Users\Owner\Desktop\SinhaLab\importantImages\circle1','C:\Users\Owner\Desktop\SinhaLab\importantImages\square1','C:\Users\Owner\Desktop\SinhaLab\importantImages\none1'},'LabelSource','foldernames');

%% training

for i = 1:2
    imageSize = net.Layers(1).InputSize;
    augmentedTrainingSet = augmentedImageDatastore(imageSize, trainingSet, 'ColorPreprocessing', 'gray2rgb');
    
    if strcmp(typeofnet,'alexnet')
        featureLayer = 'fc8';
    elseif strcmp(typeofnet,'resnet50')
        featureLayer = 'fc1000';
    elseif strcmp(typeofnet,'googlenet')
        featureLayer = 'pool5-7x7_s1';
    end
    
    
    trainingFeatures = activations(net, augmentedTrainingSet, featureLayer, 'MiniBatchSize', 32, 'OutputAs', 'columns');
    
    trainingLabels = trainingSet.Labels;
    classifier = fitcecoc(trainingFeatures, trainingLabels, 'Learner', 'Linear', 'Coding', 'onevsall', 'ObservationsIn', 'columns');
end
