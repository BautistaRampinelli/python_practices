#  Objetivo: Este programa tiene como objetivo calcular la cantidad de dinero que debe pagar cada persona en un grupo de amigos que se juntan a cenar, 
#            considerando el capital disponible de cada uno.
#
#  Flujo del programa:
#               - Introducir cantidad de personas, el nombre de las mismas y el capital disponible.
#               - Seleccionar la comida (El precio de la misma se dividirá entre todos).
#               - Seleccionar la bebida (Cada persona pagara su bebida).
#               - Mostrar todas las personas y el monto que debe aportar cada una.
#
#  Manejo de excepciones: 
#               - No se podrá repetir el nombre de una persona.
#               - En caso de que una o más personas superen su límite, mostrar mensaje de error.
#               - Inputs de valores inválidos (Por ejemplo, valores negativos en el capital).
#

def get_person_data(num_people):
    people = {}
    for i in range(num_people):
        while True:
            name = input(f"Introduce el nombre de la persona {i + 1}: ")
            if name in people:
                print("El nombre ya ha sido introducido. Introduce un nombre diferente.")
            else:
                break
        while True:
            try:
                capital = float(input(f"Introduce el capital disponible de {name}: "))
                if capital < 0:
                    raise ValueError("El capital no puede ser negativo.")
                break
            except ValueError as e:
                print(f"Entrada no válida: {e}")
        people[name] = {'capital': capital, 'drinks': []}
    return people

def select_items(menu, item_type):
    selected_items = []
    while True:
        print(f"\nSelecciona una {item_type}:")
        for i, item in enumerate(menu):
            print(f"{i + 1}. {item['name']} - ${item['price']}")
        print(f"{len(menu) + 1}. Finalizar selección de {item_type}")
        
        try:
            choice = int(input(f"Elige una opción de {item_type}: "))
            if choice < 1 or choice > len(menu) + 1:
                raise ValueError("Opción inválida.")
            if choice == len(menu) + 1:
                if not selected_items:
                    print(f"Debe seleccionar al menos un(a) {item_type}.")
                else:
                    break
            else:
                quantity = int(input(f"\n¿Cuántos de {menu[choice - 1]['name']} quieres?: "))
                selected_items.append((menu[choice - 1], quantity))
        except ValueError as e:
            print(f"Entrada no válida: {e}")
    return selected_items

def calculate_total(people, selected_food, drink_prices):
    food_cost = sum(item['price'] * quantity for item, quantity in selected_food)
    food_per_person = food_cost / len(people)
    
    for name, data in people.items():
        drink_cost = sum(drink_prices[drink - 1]['price'] for drink in data['drinks'])
        total_cost = food_per_person + drink_cost
        if total_cost > data['capital']:
            print(f"Problema: {name} no tiene suficiente capital para cubrir el total de ${total_cost:.2f}.")
            return False
    return True

def main():
    food_menu = [
        {'name': 'Pizza', 'price': 15},
        {'name': 'Hamburguesa', 'price': 10},
        {'name': 'Ensalada', 'price': 7},
        {'name': 'Pasta', 'price': 12},
        {'name': 'Empanadas', 'price': 8},
        {'name': 'Sushi', 'price': 20},
        {'name': 'Pollo', 'price': 18},
        {'name': 'Sanguche', 'price': 6},
        {'name': 'Burrito', 'price': 9},
        {'name': 'Sopa', 'price': 5}
    ]
    
    drink_menu = [
        {'name': 'Agua', 'price': 1},
        {'name': 'Gaseosa', 'price': 3},
        {'name': 'Jugo', 'price': 2},
        {'name': 'Cerveza', 'price': 5},
        {'name': 'Vino', 'price': 10},
        {'name': 'Café', 'price': 4},
        {'name': 'Té', 'price': 3},
        {'name': 'Limonada', 'price': 2},
        {'name': 'Whisky', 'price': 15},
        {'name': 'Cóctel', 'price': 8}
    ]
    
    while True:
        try:
            num_people = int(input("Introduce la cantidad de personas: "))
            if num_people <= 0:
                raise ValueError("Debe haber al menos una persona.")
            break
        except ValueError as e:
            print(f"Entrada no válida: {e}")
    
    people = get_person_data(num_people)
    
    selected_food = select_items(food_menu, "comida")
    
    for name in people.keys():
        print(f"\nSelecciona las bebidas para {name}:")
        drinks = select_items(drink_menu, "bebida")
        for drink, quantity in drinks:
            people[name]['drinks'].extend([drink_menu.index(drink) + 1] * quantity)
    
    if calculate_total(people, selected_food, drink_menu):
        print("*****************************************")
        print("\nResumen de pagos:")
        food_cost = sum(item['price'] * quantity for item, quantity in selected_food)
        food_per_person = food_cost / len(people)
        
        for name, data in people.items():
            drink_cost = sum(drink_menu[drink - 1]['price'] for drink in data['drinks'])
            total_cost = food_per_person + drink_cost
            print(f"{name} debe pagar ${total_cost:.2f} (Comida: ${food_per_person:.2f}, Bebida: ${drink_cost:.2f})")
        print("*****************************************")
    else:
        print("No se pudo calcular el total debido a falta de capital de uno o más participantes.")


main()
