myDict = {
    "class":{
        "student":{
            "name":"abc",
            "marks": {
                "python" : 90,
                "web" : 95 
            }
        }
    }
}

a=myDict["class"]
b=a["student"]
c=b["marks"]
print(c)