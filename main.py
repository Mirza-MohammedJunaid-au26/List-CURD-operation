element_list = []

def elements():
    print()
    print("1 : Add Element in List")
    print("2 : Accessing Element from List")
    print("3 : Updating Element from List")
    print("4 : Removing Element from List")
    print("5 : Slicing Element from List")
    print("6 : Reversing Element from List")
    print("7 : Clearing the List")
    print()
    print("type exit to come out of Command")

    i = int(input("Enter : "))
    while i<8:
        if i==1:
            print("1 : String")
            print("2 : Int")
            print("3 : Float")
            print("4 : Boolean")
            print("5 : exit")

            insert_input = int(input("Enter : "))
            
            if insert_input==1:
                string_input=input("Enter String :")
                element_list.append(string_input)
                continue

            elif insert_input==2:
                int_input=int(input("Enter Integer :"))
                element_list.append(int_input)
                continue
            
            elif insert_input==3:
                float_input=float(input("Enter Float :"))
                element_list.append(float_input)
                continue

            elif insert_input==4:
                boolean_input=bool(input("Enter Boolean :"))
                element_list.append(boolean_input)
                continue
        
            else:
                print(element_list)
                elements()

        
        elif i==2:
            print(element_list)
            access_input=int(input("Enter Index of the Element : "))
            print("value is :",element_list[access_input])
            elements()            
        
        elif i==3:
            print(element_list)
            update_index_input=int(input("Enter Index of the Element : "))
            update_element_input=input("Enter Value of the Element : ")
            print("Before Updating : ",element_list)
            element_list[update_index_input]=update_element_input
            print("After Updating : ",element_list)
            elements()            
        
        elif i==4:
            print(element_list)
            pop_index_input=int(input("Enter Index of the Element : "))
            print("Before Deleting : ",element_list)
            element_list.pop(pop_index_input)
            print("After Deleting : ",element_list)
            elements()            
        
        elif i==5:
            print(element_list)
            slicing_starting_index_input=int(input("Enter Starting Index : "))
            slicing_ending_index_input=int(input("Enter Ending Index : "))
            print("Before Slicing : ",element_list)
            print("After Slicing : ",element_list[slicing_starting_index_input:slicing_ending_index_input])
            elements()            
        
        elif i==6:
            print(element_list)
            print("Reverse : ",element_list[::-1])
            elements()    
        
        elif i==7:
            print(element_list)
            element_list.clear()
            print("List is Cleared",element_list)
            elements()    

elements()
        