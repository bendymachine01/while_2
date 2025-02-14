
print("--------------------------------------")
print("----- SIMULACIÓN DE REBOTES ---------")
print("--------------------------------------")

# imput 
h = float(input("Ingrese la altura inicial de la pelota (metros): "))

# Variables
q = h / 5
n = 0


# procssing:
# calcular el número de rebotes hasta que h < q
while h >= q:
    h *= 0.9  # La pelota sube un 10% menos en cada rebote
    n += 1

# output
print(f"La pelota no alcanza a subir la quinta parte de la altura inicial en el rebote número {n}.")