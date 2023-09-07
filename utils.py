class utils:

    def reversed(self, value:int):

        if not isinstance(value, int):
            return("TypeError")
        
        value_numerical_list = list(str(value))
        reversed_value = 0
        
        for i in range(len(value_numerical_list)):
            reversed_value += int(value_numerical_list[i]) * pow(10, i)
        
        return reversed_value
    
    def formatter(self, value:int):

        if not isinstance(value, int):
            return("TypeError")
        
        val_in_binary = bin(value)
        val_in_octal = oct(value)

        return val_in_binary, val_in_octal
