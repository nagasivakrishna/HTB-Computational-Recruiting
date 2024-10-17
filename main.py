import pandas as pd
import socks

weights = [0.2, 0.3, 0.1, 0.05, 0.05, 0.3]
class Candidate:
    def __init__(self, array):
        self.firstname = array[0]
        self.lastname = array[1]
        self.health = int(array[2])
        self.agility = int(array[3])
        self.charisma = int(array[4])
        self.knowledge = int(array[5])
        self.energy = int(array[6])
        self.resourcefullness = int(array[7])
        self.attributes = [self.health, self.agility, self.charisma, self.knowledge, self.energy, self.resourcefullness]
    
    def printattributes(self):
        print(self.attributes)

    def skillScore(self, attributeArray):
        skillScoreValue = []
        for i in range(len(attributeArray)):
            skillScoreValue.insert(i, (round(6*(attributeArray[i]*weights[i]))+10))
        return skillScoreValue
    
    def overAllValue(self, skillScoreValue):         
        totalValue = round(5*(((skillScoreValue[0] * 0.18) + (skillScoreValue[1] * 0.20) + (skillScoreValue[2] * 0.21) + (skillScoreValue[3] * 0.08) + (skillScoreValue[4] * 0.17) + (skillScoreValue[5] * 0.16))))
        return totalValue


def main(ip, port):
    with open('data.txt') as file:
        lines = file.readlines()

    objArray = []
    hashmap = {}
    for i in range(len(lines)):
        line = lines[i].split()
        objArray.insert(i,Candidate(line))
        hashmap[f'{objArray[i].firstname} {objArray[i].lastname}'] = objArray[i].overAllValue(objArray[i].skillScore(objArray[i].attributes))
    

    df = pd.DataFrame(list(hashmap.items()), columns=['Name', 'Value_Score']) 
    df = df.sort_values(by=['Value_Score', 'Name'], ascending=False)

    string = ''
    for i in range(14):
        string += (f" {df.iloc[i]['Name']} - {df.iloc[i]['Value_Score']},")
    cleanStr = string[:-1].strip()

    s = socks.socksocket()
    s.connect((ip,port))
    s.recv(6096)
    cleanStr = cleanStr + "\n"
    s.send(bytes(cleanStr, encoding='utf-8'))
    print(s.recv(5096).decode())
    s.close()

if __name__ == '__main__':
    # Change this
    ip = '127.0.0.1'
    port = 4444
    main(ip, port)