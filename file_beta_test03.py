sim = 0
não = 0
cu = 0
for i in range(0,5):
    question = int(input("Você gostou do filme ? \n 1-sim \n 2-não \n 3-tome no seu cu \n"))

    if question == 1:
        sim = sim +1
    if question == 2:
        não = não +1
    if question == 3:
        cu = cu +1

print("Pessoas que disseram sim: {}" .format(sim))
print("Pessoas que disseram não: {}" .format(não))
print("Pessoas que disseram pro estagiário tomar no cu: {}" .format(cu))

ask = int(input("Deseja continuar ? \n 1-sim \n 2-não \n"))

if ask == "sim" or ask == 1:
    print("Saindo...")
if ask == "não" or ask == 2:
    print("Problema seu.")
