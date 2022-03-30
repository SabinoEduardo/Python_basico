#
#? Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

taxa_population_A = float(input("Taxa de crescimento da População A: "))/100
taxa_population_B = float(input("Taxa de crescimento da População B: "))/100
population_A = 80000
population_B = 200000
ano = 0
if taxa_population_A <= taxa_population_B:
    print("A população dO país A nunca será maior que do país B")
else:
    while population_B >= population_A:
        
        population_A += population_A*taxa_population_A
        population_B += population_B*taxa_population_B
        ano += 1
    print(f"Serão necessários {ano} anos para que a população do pais A ultrapasse a população B")
