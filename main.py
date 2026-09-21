from pyscript import display, document

#SEATWORK1
#String
Name = "Student name: Jose Mateo M. Salacup"
Age = "Age: 15"
Height1 =  172
#List
Countries_list = ["Hong Kong", "Singapore", "Taiwan"]
#String
Student_type = False
#Dictionary
Student_info = {
    "color": "Pink",
    "car_brand": "Honda",
    "shoe_size": 12.5,
    "best_friend": "Ivanna Mortel"
}
#Set
Favorite_fruits = {"Mango", "Blueberry", "Dragonfruit", "Banana", "Grapes"}
#Tuple
Days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

#Displays
display(f"Name: {Name}")
display(f"Age: {Age}")
display(f"Height: {Height1} cm")
display(f"Countries I want to visit again: {', '.join(Countries_list)}")
display(f"New student: {'Yes' if Student_type else 'No'}")
display(f"Student information: {Student_info}")
display(f"Favorite fruits: {', '.join(Favorite_fruits)}")
display(f"Days of the week: {', '.join(Days)}")


#DRILL2
def adding_numbers(e):
    document.getElementById("output1").innerHTML = ""

    no1 = float(document.getElementById("input1").value)
    no2 = float(document.getElementById("input2").value)

    #Addition
    addition = no1 + no2

    #Subtraction
    subtraction = no1 - no2

    #Multiplication
    multiplication = no1 * no2
    
    #Floating-point Division
    division = no1 / no2

    #Floor Division
    floor_division = no1 // no2

    #Modulus
    modulus = no1 % no2

    #Exponentiation
    exponentiation = no1 ** no2

    #Displaying
    display(f"Addition: {addition}", target="output1")
    display(f"Subtraction: {subtraction}", target="output1")
    display(f"Multiplication: {multiplication}", target="output1")
    display(f"Floating-point Division: {division}", target="output1")
    display(f"Floor Division: {floor_division}", target="output1")
    display(f"Modulus: {modulus}", target="output1")
    display(f"Exponentiation: {exponentiation}", target="output1")