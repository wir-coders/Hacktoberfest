# This program searches within an xml file to find information,
# in this example the information of file "Users.xml" will be used to implement an SQL statement.
# Hope this will useful for you! - ernecto-ca

# Imports to read a xml and time 
import defusedxml.cElementTree as goodET
from datetime import datetime

# Create the "tree" element of the xml
tree = goodET.parse('Users.xml')
goodET.iterparse('Users.xml')

# Get the information of the xml 
root = tree.getroot()

# To check how long it took
now = datetime.now()
print(now)

# The main part of the sql
sql = "INSERT INTO users VALUES ("

# ***when it will insert in a data base**** try:
for user in root:
    sql = sql +"'"+str(user.get('Id')).replace("'","´")+"',"
    sql = sql +"'"+str(user.get('Reputation')).replace("'","´")+"',"
    sql = sql +"'"+str(user.get('CreationDate')).replace("'","´")+"',"
    sql = sql +"'"+str(user.get('DisplayName')).replace("'","´")+"',"
    sql = sql +"'"+str(user.get('LastAccessDate')).replace("'","´")+"',"
    sql = sql +"'"+str(user.get('WebsiteUrl')).replace("'","´")+"',"
    sql = sql +"'"+str(user.get('Location')).replace("'","´").replace("\\","")+"',"
    sql = sql +"'"+str(user.get('AboutMe')).replace("'","´")+"',"
    sql = sql +"'"+str(user.get('Views')).replace("'","´")+"',"
    sql = sql +"'"+str(user.get('UpVotes')).replace("'","´")+"',"
    sql = sql +"'"+str(user.get('DownVotes')).replace("'","´")+"',"
    sql = sql +"'"+str(user.get('ProfileImageUrl')).replace("'","´")+"',"
    sql = sql +"'"+str(user.get('AccountId')).replace("'","´").replace("None","0")+"'"
    sql=sql+");"
    # then you need to execute the sql sentence with pymysql 
    print(sql)
# If an error from the pymysql    
#***change it to the appropriate error*** except e: 
#    print(sql)
 
# Commit your connection mith pymysql 
# Close the connection 

# Check the final time (this depends of the data size in the xml file and inserting in the data base)
now = datetime.now()
print(now)

