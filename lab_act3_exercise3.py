#Lab Activity 3 Exercise 3

def vowelsToUpper(s: str) -> str:
    # Using list comprehension to convert vowels to uppercase and keep other characters unchanged
    return ''.join([char.upper() if char in 'aeiouAEIOU' else char for char in s])

# Sample calls
print(vowelsToUpper(""))                  
print(vowelsToUpper("Hello, world!"))     
print(vowelsToUpper("hello hi bye"))      
