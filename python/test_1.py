


# Defines a "repeat" function that takes 2 arguments.
def repeat(s, multiple):
   

    result = s 
    if multiple:
        result = result * multiple
        print(f"Word: {result}, Multiple: {multiple} ")
    return result


def Hello(name):
    
    name = name + "!!!!"
    print("Hello", name)

repeat("hello ", 2)
Hello("Volvi")