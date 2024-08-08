import re

def replace_words(string):
    string= string.replace("CASOTON", "CA").replace("SCAHBASLE", "SC").replace("SCAH", "SC").replace("SCA", "SC").replace("SOTONOQ", "SOTONO").replace("STONO", "SOTONO").replace("SOPP", "SOP").replace("FCC", "FC").replace("AS 4DIGITS", "A 4DIGITS").replace("PPP", "PP")
    return string.replace("SCBASLE", "SC")
 
# Function to separate the numbers 
# and alphabets from the given string
def separateNumbersAlphabets(string):
    numbers = "".join(re.findall(r'[0-9]+', string)).strip()
    alphabets = "".join(re.findall(r'[a-zA-Z]+', string)).strip()
    length_num = str(len(numbers)) + "DIGITS"
    return alphabets + " " + length_num

def clean_ticket(string):
    string = string.replace(".", "").replace("/", "")
    string = separateNumbersAlphabets(string)
    string = replace_words(string)
    return string.upper()

"""    df['AgeFill'] = df['Age']
    df['AgeFill'] = df['AgeFill'].groupby([df['Sex'], df['Pclass']], group_keys=False).apply(lambda x: x.fillna(x.median()))
    
    df['Cabin'] = df['Cabin'].fillna('missing').apply(lambda x : cabin_clean(x))
    df['Fare'] = df['Fare'].groupby([df['Sex'], df['Pclass'], df['Ticket']], group_keys=False).apply(lambda x: x.fillna(x.mean()))"""

def preprocess(df):
    
    df["AgeFill"] = df["Age"]
    # df["Ticket"] = df["Ticket"].apply(lambda x : clean_ticket(x))
    # df["Ticket1"] = df["Ticket"].apply(lambda x : x.split(" ")[0].strip().replace("SCBASLE", "SC"))
    df["Ticket2"] = df["Ticket"].apply(lambda x : x.split(" ")[1].strip())
    df["Ticket2"] = df["Ticket2"].apply(lambda x: [int(s) for s in x if s.isdigit()][0])

    df["Sex"] = df["Sex"].apply(lambda x : x.lower())
    df["Sex"] = df["Sex"].map({"male":1, "female":0})
    df = df[["Pclass", "Sex", "AgeFill", "SibSp", "Parch", "Fare", "Ticket2"]]
    
    return df
