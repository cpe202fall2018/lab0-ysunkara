def weight_on_planets():
    weight = float(input('What do you weigh on earth? '))
    marsWeight=weight*0.38
    juptierWeight= weight*2.34

    print("\nOn Mars you would weigh", marsWeight, "pounds.\nOn Jupiter you would weigh", juptierWeight, "pounds.")
if __name__ == '__main__':
   weight_on_planets()
