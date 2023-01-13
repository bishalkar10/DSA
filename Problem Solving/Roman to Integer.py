def romanToDecimal(self, s): 
        # Hashmap for storing key value pair
        roman = {
                 'I' : 1, 
                 'V' : 5,
                 'X' : 10,
                 'L' : 50,
                 'C' : 100,
                 'D' : 500,
                 'M' : 1000 
                 } 

        # sum variable for storing sum 
        sum = 0
        # size of string
        n = len(s)

         
        # indice for iteration
        i = 0
        while i < n :

            # if it's not the last char of string if less than right char
            if (i != n - 1 and roman[s[i]] < roman[s[i + 1]]):
                sum += roman[s[i + 1]] - roman[s[i]]
                i += 2  # increase indice by 2 and skip the iteration
                continue
            else: # else just add char value
                sum += roman[s[i]]
                i += 1
 
        # return sum 
        return sum
