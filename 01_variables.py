
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


my_bool_variable = False
print(my_bool_variable)
# concatenación de variables en un print
print(type(print("Mi cadena de texto")))  # tipo "NoneType"
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Alberto", "Cabrera", "AlbeCabrera", 35
print("Me llamo:", name, surname, ". Mi edad es:", age, "Y mi alias es:", alias)


# Inputs
name = input('¿Cuál es tu nombre?: ')
age = input('¿Cuántos años tienes? ')

print(name)
print(age)
