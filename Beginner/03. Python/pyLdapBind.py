import os
from pyad import pyad
import pyad.adquery

''' Functions for colorized output '''
def prRed(msg):
    print("\033[91m{}\033[00m" .format(msg))

def prGreen(msg):
    print("\033[92m{}\033[00m" .format(msg))

def prYellow(msg):
    print("\033[93m{}\033[00m" .format(msg))
    
def getGroups(userName):
    ''' Query for logged in user AD group membership '''
    q = pyad.adquery.ADQuery()

    ''' [Update base DN for your domain] '''
    q.execute_query(
        attributes = ['memberof'],
        where_clause = "samaccountname = '" + userName + "'",
        base_dn = "DC=yourDomain,DC=local"
    )

    for r in q.get_results():
        grps = r['memberof']

    return grps

def checkGroupMembership(grps,adminGrps):
    for adGrp in adminGrps:
        if adGrp in grps:
            prYellow(adGrp)
            return True

def main():
    ''' [Update with AD approved groups] '''
    adminGroups = [
                    "CN=Admin_Group1,OU=Administrators,DC=yourDomain,DC=local",
                    "CN=Admin_Group2,OU=Administrators,DC=yourDomain,DC=local",
                    "CN=Admin_Group3,OU=Administrators,DC=yourDomain,DC=local"
                ]
    adGroups = getGroups(os.getlogin())
    print("Checking Groups:")
    print(*adminGroups,sep = "\n")
    if checkGroupMembership(adGroups,adminGroups) == True:
        prGreen("Access Granted")
    else:
        prRed("Access Denied")

main()