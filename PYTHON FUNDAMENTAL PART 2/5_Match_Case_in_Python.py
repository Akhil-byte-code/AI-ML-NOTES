# Conditional stmts 
# Match case --> alternate for if elif else 

color = input("Enter color ")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("look")
    case "Red":
        print("Stop")
    case _:  # default case 
        print("Wrong color !")