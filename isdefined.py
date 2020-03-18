def isdefined(variable):

    try:
        variable
    except NameError:
        var_exists = False
    else:
        var_exists = True
    return(var_exists)
