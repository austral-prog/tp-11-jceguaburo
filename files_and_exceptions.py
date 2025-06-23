def read_file_to_dict(filename):
    sales_dict = {}
    with open(filename, 'r') as file:
        content = file.read().strip()
        sales = content.split(';')
        for entry in sales:
            if entry:  # Evita procesar cadenas vacías si hay un ; final
                try:
                    product, value = entry.split(':')
                    value = float(value)
                    if product in sales_dict:
                        sales_dict[product].append(value)
                    else:
                        sales_dict[product] = [value]
                except ValueError:
                    print(f"Entrada inválida ignorada: {entry}")
    return sales_dict


def process_dict(sales_dict):
    for product, values in sales_dict.items():
        total = sum(values)
        avg = total / len(values)
        print(f"{product}: ventas totales ${total:.2f}, promedio ${avg:.2f}")
