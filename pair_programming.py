# FEET TO METERS HOORAY
def feet_inches_to_meters(feet, inches):
    """Convert feet and inches to meeters"""

    feetinch = feet + (inches/12) #combining the feet and inches values
    meter = feetinch/3.281  #converting to meters
    
    return meter

# . . No defensive programming
# . . No function, but inputs described
# . . Did not handle rounding, failed one test from rounding discrepancy

# . . Takes live inputs, well commented
