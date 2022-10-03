poll_talen = ["Lucas", "Maud", "Jan", "Dillan", 
              "Piet", "Joris"]

favorite_languages = {    
    "Jan": "python",    
    "Piet": "c",    
    "Joris": "ruby"}
for i in poll_talen:
    if favorite_languages.get(i):
        print("bedankt")
    else:
        print("niet bedankt")