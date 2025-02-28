def get_last(items):
    if items:
        print(items[-1])
    else:
        print("List is empty")
        return None
    
    
items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)