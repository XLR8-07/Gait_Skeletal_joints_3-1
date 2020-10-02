import json
import train
import Test

DATASET = 'UTKinect'
with open('constants.json') as constantsJSONFile:
    data = json.load(constantsJSONFile)
    datasetConst = data[DATASET]
    genConst = data['general']
    # Training using the dataset
    train.train(datasetConst['UserCount'], datasetConst, genConst)
    # Test.test('u5s2.txt', datasetConst, genConst)