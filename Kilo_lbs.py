weight = input("what is you weight? ")
kilo_lbs = input("(L)bs or (K)ilo: ").lower()

if kilo_lbs == "l":
    lbs_weight = int(weight) * 0.4535924
    print(f"Lbs - {weight} \nKilo - {lbs_weight}")
elif kilo_lbs == "k":
    kilo_weight = int(weight) * 2.204623
    print(f"Lbs - {kilo_weight} \nKilo - {weight}")
