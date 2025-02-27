import itertools
import random
import string

def generate_passwords(name, surname1, surname2, birth_year, children):
    passwords = set()
    
    birth_suffix = birth_year[-2:]
    name_variants = [name[:2].capitalize(), name[:3].capitalize()]
    surname1_variants = [surname1[:2].lower(), surname1[:3].lower()]
    surname2_variants = [surname2[:2].lower(), surname2[:3].lower()]
    
    for n in name_variants:
        for s1 in surname1_variants:
            for s2 in surname2_variants:
                passwords.add(n + s1 + s2 + birth_suffix)
                passwords.add(n + s1.capitalize() + s2.capitalize() + birth_suffix)
    
    if children and len(children) > 1:
        child_initials = [child["name"][:2].lower() for child in children] + [child["name"][:3].lower() for child in children]
        for r in range(2, min(4, len(child_initials) + 1)):
            child_combinations = list(itertools.permutations(child_initials, r))
            for combo in child_combinations:
                combined = "".join(combo)
                passwords.add(combined.capitalize() + birth_suffix)
                passwords.add(combined + birth_suffix)
    
    special_chars = ['!', '"', '·', '$', '%', '&', '/', '(', ')', '=', '?', '¿']
    extra_variations = set()
    for pwd in passwords:
        for char in special_chars:
            extra_variations.add(pwd + char)
    
    passwords.update(extra_variations)
    return passwords

def main():
    name = input("Nombre: ").strip()
    surname1 = input("Primer apellido: ").strip()
    surname2 = input("Segundo apellido: ").strip()
    birth_year = input("Año de nacimiento (YYYY): ").strip()
    
    children = []
    has_children = input("¿Tiene hijos? (s/n): ").strip().lower()
    if has_children == 's':
        while True:
            try:
                num_children = int(input("¿Cuántos hijos tiene?: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        for _ in range(num_children):
            child_name = input("Nombre del hijo: ").strip()
            children.append({"name": child_name})
    
    passwords = generate_passwords(name, surname1, surname2, birth_year, children)
    
    filename = "diccionario.txt"
    with open(filename, "w") as file:
        for password in sorted(passwords):
            file.write(password + "\n")
    
    print(f"Diccionario generado y guardado en {filename} con {len(passwords)} combinaciones.")
    
if __name__ == "__main__":
    main()
