from Interface import Interface


interface = Interface()

try:
    system = int(input("Hello. Choose coordinate system:\n" \
                    "1. Cartesian\n" \
                    "2. Polar\n" \
                    "Your choice: "))
except:
    raise Exception("Wrong input. Input only number")


if system == 1:
    interface.draw_cartesian(input("Input file: "))
elif system == 2:
    interface.draw_polar(input("Input file: "))

print("Goodbye")




# r = c * sqrt(exp(arctg(2*tg(phi)) + pi*k) / (1 + 3*(sin(phi))**2))
# ln((x**2 + 4*y**2) / (c**2)) = arctg(2*y / x) + pi*k
