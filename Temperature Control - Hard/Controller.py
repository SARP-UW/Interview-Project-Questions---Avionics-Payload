from Plant_Box import Plant_Box
import time



# Implement this function.  It takes in the
# current temperature and a set point (the temperature
# that you want the object at) and returns the value
# that the control temperature should be set to.
# You are free to create external variables to preserve
# state if you wish.  Doing so will (probably) be needed.
def controller(curr_temp: float, set_point: float) -> float:
    # REPLACE THIS, your code here
    return 0
    # ----------------------------




def main():

    object = Plant_Box()
    set_point = 40#C

    # Main loop, do not change this
    while True:
        object.set_control_power(controller(object.get_temp(), set_point))
        object.update_temp()
        time.sleep(1)




if __name__ == "__main__":
    main()

