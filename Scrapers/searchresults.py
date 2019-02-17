from webscraping import jobInfo
import json
#from mattsfile import list
userSkills = ['python', 'java']
#jobInfo = {'Job 1': ['comp1', 'linkedin', ['python']], 'Job 2': ['comp2', 'linkedin1', ['c++','python', 'java']],'Job 3': ['comp3', 'linkedin2', ['ruby', 'asp']]}
#jobstoDisplay = {}
jobstoDisplay = []
relevant = 0
for key, value in jobInfo.items():
    temL = []
    relevant = 0
    add = False
    for skill in userSkills:
        if skill in value[2]:
            add= True
            relevant+=1
            #jobstoDisplay[key] = [relevant, value[2]]
    if add==True:
        temL.append(relevant)
        temL.append(key)
        temL.append(value[0])
        temL.append(value[1])
        temL.append(value[2])
        jobstoDisplay.append(temL)

n = len(jobstoDisplay)
for i in range(n):
    for j in range(0, n-i-1):
        if jobstoDisplay[j][0] < jobstoDisplay[j+1][0] :
            temp = jobstoDisplay[j]
            jobstoDisplay[j] = jobstoDisplay[j+1]
            jobstoDisplay[j+1]  = temp
print()
jtoDisplay = {}
for i in range(n):
    '''
    print("Company: ", jobstoDisplay[i][2])
    print()
    print("Link: ", jobstoDisplay[i][3])
    print()
    print("keywords: ", jobstoDisplay[i][4])
    print("\n")
    '''
    jtoDisplay[jobstoDisplay[i][1]] = [jobstoDisplay[i][2], jobstoDisplay[i][3], jobstoDisplay[i][4]]

def writeTojsonFile(fname, data):
    #nameWext = '/.' + path + '/' + fname + '.json'
    with open(fName, 'w') as fp:
        json.dump(data, fp)

#path = './'
fName= 'formattedData.json'
#writeTojsonFile(path, fName, jtoDisplay)
writeTojsonFile(fName, jtoDisplay)
#legend:
#{key=jobtitle value:[companyname, link, keywords]}
