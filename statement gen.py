def statement_gen(statement, decoration) :
    sides = decoration * 3
    statement = ("{} {} {}".format(sides,statement,sides))
    topbottom = decoration * len(statement)

    print(topbottom)
    print(statement)
    print(topbottom)

    return ""

hello_world = statement_gen("Hello World!!","(")

    