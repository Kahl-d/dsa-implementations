def final_value_after_operations(operations):
	
    tiger = 1
    for operation in operations:
        if operation == "bouncy" or operation == "flouncy":
            tiger +=1
            
        elif operation == "trouncy" or operation == "pouncy":
            tiger -=1
            
    return tiger


operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))