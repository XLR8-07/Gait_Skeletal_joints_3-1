import matplotlib.pyplot as plt
import Test
import json


DATASET = 'UTKinect'
with open('constants.json') as constantsJSONFile:
    data = json.load(constantsJSONFile)
    datasetConst = data[DATASET]
    genConst = data['general']
    storeMismatch , detectedUser, trainDTW, testDTW = Test.test('u1s1.txt', datasetConst, genConst)
    storeMismatch = storeMismatch[1:]
    
    user = []
    for i in range(1,len(storeMismatch)+1):
        user.append(i)
    
    # plt.plot(trainDTW,label='TRAIN',color='g')
    # plt.plot(testDTW,label='TEST',color='b')
    plt.bar(user,storeMismatch,label='User Mismatch',color = 'b')
    plt.xlabel("user No")
    plt.ylabel("misMatch")
    plt.legend()
    plt.show()