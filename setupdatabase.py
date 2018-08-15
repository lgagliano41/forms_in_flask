from basicdata import db,Puppy
#creates all the tables
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])

db.session.commit()

print(sam.id)
print(frank.id)
