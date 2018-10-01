from constraint import*
probelm=problem()
probelm.add variable ('a',range(5))
probelm.add variable ('b',range(5))
probelm.add constraint(lambda.a,b:a+b==5)
probelm.add constraint(lambda.a,b:a+b==6)
probelm.get solution()
