class Calc:
    def mostrar_menu(self):
        print("Selecciona una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Potencia")
        print("5. Dividir")
        print("0. Salir")
        print()
        opcion = int(input("Ingrese su opción: "))
        print()
        return opcion
    
    def obtener_operandos(self):
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el segundo valor: "))
        return a, b

    def sum(self, a, b):
        return a + b

    def res(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "No se puede dividir por 0"
        return a / b

    def pot(self, a, b):
        return a ** b
    
    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu()

            if opcion == 0:
                print("Saliendo del programa...")
                break

            # Obtener operandos para cualquier operación
            a, b = self.obtener_operandos()

            # Ejecutar la operación según la opción seleccionada
            if opcion == 1:
                resultado = self.sum(a, b)
            elif opcion == 2:
                resultado = self.res(a, b)
            elif opcion == 3:
                resultado = self.mult(a, b)
            elif opcion == 4:
                resultado = self.pot(a, b)
            elif opcion == 5:
                resultado = self.div(a, b)
            else:
                print("Opción no válida. Intente de nuevo.")
                continue

            # Mostrar el resultado
            print(f"El resultado de la operación es: {resultado}")
            print()