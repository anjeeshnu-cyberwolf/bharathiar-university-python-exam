import pandas as pd
student_data=pd.DataFrame(
    {"Student_Name": ["yoyo", "frank", "don", "demon", "modi", "yogi", "amit shah", "indianrailway", "batman", "superman"],
     "Age": [20,20,20,20,20,20,20,20,20,20],
     "DOB(year)": [2001,2001,2001,2001,2001,2001,2001,2001,2001,2001],
     "Weight(kg)" : [60,62,75,80,49,67,83,66,73,72],
     "Height(cm)" : [150,120,135,177,156,188,199,154,177,133]}
)

student_data["BMI"]=student_data["Weight(kg)"]/student_data["Height(cm)"]*student_data["Height(cm)"]

student_data["Status"]=student_data["BMI"].apply(lambda x: "Normal" if x>50 and x<80 else "Underweight")
print(student_data)


student_data.to_csv("student_data.csv")
student_data=pd.read_csv("/content/student_data.csv")
student_data