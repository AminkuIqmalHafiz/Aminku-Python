my_name = "Aminku Iqmal Hafiz"
current_cgpa = 3.93
age = 19
working_part_time = False
BOLD = '\033[1m'

print (f"{BOLD}INITIALIZING DATA CONFIRMATION\n")
print ("Name:",my_name,"\nIs the input given a string?",isinstance(my_name,str),"\n")
print ("Current CGPA:",current_cgpa,"\nIs the input given a float?",isinstance(current_cgpa,float),"\n")
print ("Age:",age,"\nIs the input given a integer?",isinstance(age,int),"\n")
print ("Working part time?:",working_part_time,"\nIs the input given a boolean?",isinstance(working_part_time,bool),"\n")

print("------------------------------------------------------------------------------------------")

print(f"{BOLD}Business Card")
print (f"{BOLD}Name:",my_name,)
print (f"{BOLD}Current CGPA:",current_cgpa)
print (f"{BOLD}Age:", age)
print (f"{BOLD}Working Part Time?",working_part_time)

print("------------------------------------------------------------------------------------------")


