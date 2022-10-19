game = input("Wybierz gierkę : 1:Number Memory   2:Reaction Time   3:Verbal Memory          ->")
if game == "1":
    import NumberMemory
elif game == "2":
    import ReactionTime 
elif game == "3":
    import VerbalMemory
else:
    print("kolezko, cos żeś sknocił!")