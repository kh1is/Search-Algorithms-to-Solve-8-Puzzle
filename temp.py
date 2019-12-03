movement = Movment(start_state)

movement.right_movment()
movement.left_movment()
movement.up_movment()
movement.down_movment()

if(movement.right_state != None):
    print_method(movement.right_state.puzzle)
    print("-------------------------")
else:
    print("No Child")

if(movement.left_state != None):
    print_method(movement.left_state.puzzle)
    print("-------------------------")
else:
    print("No Child")

if(movement.up_state != None):
    print_method(movement.up_state.puzzle)
    print("-------------------------")
else:
    print("No Child")

if(movement.down_state != None):
    print_method(movement.down_state.puzzle)
else:
    print("No Child")
