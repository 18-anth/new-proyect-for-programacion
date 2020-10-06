import data

def getHeroePorId(id):
    heroe = {}

    for h in data.heroes:
        if h['id'] == id:
            heroe = h

    return heroe
    
def getHeroePorSuperHero(superHero):
    result = []
    for h in data.heroes:
        if h['superhero'].lower().find(superHero.lower())>=0:
            result.append(h)
    return result

def printHeroes(heroes):
    for heroe in heroes:
        print(heroe['id'], heroe['superhero'], heroe['publisher'], heroe['alter_ego'], heroe['first_appearance'], heroe['characters'])
    