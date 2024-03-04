
import torch
from torch.distributions import multivariate_normal
import matplotlib.pyplot as plt



class Generador_Datos():

    def generar_datos(self, numberSamplesPerClass = 2, mean1 = [2, 2], mean2 = [26, 26], stds1 = [3, 3], stds2 = [2, 1]):
        """
        Creates the data to be used for training, using a GMM distribution
        @param numberSamplesPerClass, the number of samples per class
        @param mean1, means for samples from the class 1
        @param mean2, means for samples from the class 2
        @param stds1, standard deviation for samples, class 1
        @param stds2, standard deviation for samples, class 2    """
        means = torch.zeros(2)
        # Ones to concatenate for bias
        ones = torch.ones(numberSamplesPerClass, 1)
        means[0] = mean1[0]
        means[1] = mean1[1]
        # Covariance matrix creation with identity
        covarianceMatrix = torch.eye(2)
        covarianceMatrix[0, 0] = stds1[0]
        covarianceMatrix[1, 1] = stds1[1]
        samplesClass1 = self.__generar_datos_una_clase(means, covarianceMatrix, numberSamplesPerClass)
        means[0] = mean2[0]
        means[1] = mean2[1]
        covarianceMatrix[0, 0] = stds2[0]
        covarianceMatrix[1, 1] = stds2[1]
        samplesClass2 = self.__generar_datos_una_clase(means, covarianceMatrix, numberSamplesPerClass)
        # Concatenates the ones for the bias
       
        samplesAll = torch.cat((samplesClass1, samplesClass2), 0)       
        #Create targets
        targetsClass1 = torch.ones(numberSamplesPerClass, 1)
        targetsClass2 = 0 * torch.ones(numberSamplesPerClass, 1)
        targetsAll = torch.cat((targetsClass1, targetsClass2), 0)

        return (targetsAll.numpy(), samplesAll.numpy())


    '''
    Creates data with gaussian distribution
    '''
    def __generar_datos_una_clase(self, means, covarianceMatrix, numberSamples):
        # Inits the bi gaussian data generator
        multiGaussGenerator = multivariate_normal.MultivariateNormal(means, covarianceMatrix)
        # Takes the samples
        samples = multiGaussGenerator.sample(torch.Size([numberSamples]))

        return samples
    


