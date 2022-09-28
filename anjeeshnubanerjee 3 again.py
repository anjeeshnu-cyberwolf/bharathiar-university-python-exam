import pandas as pd
crime=pd.DataFrame(
    {"Offense": ["Sending threatning messages by email", "Sending Defarmatory messages by email", "Forgery of electronic records", "Bogus websites,Cyber frauds", "Email Spoofing", "Web-Jacking", "E-Mail Abuse", "Online sale drugs", "Online sale of arms"],
     "IP Section(law)": [503,499,463,420,463,383,500,1985,1959],
     "Penalty(Rs)": [15000,15000,100000,20000,15000,30000,25000,200000,500000],
     "Crime in Popular apps" : ["Gmail,Outlook","Gmail,Outlook","OLX,Flipkart,Amazon","Gpay,Phonepe", "Gmail,Outlook", "Facebook,Instagram", "Gmail,Outlook","OLX,Facebook,Instagram","Flipkart,Amazon,Shop101"]}
)


crime
