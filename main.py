from circle import Circle

# circle = Circle(3)

# print(circle.perimeter())
# print(circle.area())

# circle.radius = 4
# print(circle.perimeter())
# radius = -3
# try:
#     circle.radius = radius
# except ValueError:
#     # print("Invalid number")
#     circle.radius = abs(radius)
# print(circle.perimeter())

def print_data(circle):
    print(f"Perimetro: {circle.perimeter()}")
    print(f"Area: {circle.area()}")

while True:
    try:
        r = int(input("Ingresa un valor para el radio "))
        if r < 0:
            # raise ValueError("Radio debe ser positivo")
            # TAREA: Implementar RadiusError
            raise RadiusError()
    except ValueError as err:
        print("Debe ser un número")
        print(err)
    except RadiusError as err:
        print("Debe ser positivo")
        print(err)
    else:
        circle = Circle(r)
        print_data(circle)
        break
    finally:
        print("Gracias por trabajar con nosotros")