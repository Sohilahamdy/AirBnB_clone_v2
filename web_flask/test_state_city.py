from models import storage
from models.state import State
from models.city import City

# Create and save new states and cities
state_1 = State(name="California")
state_1.save()
state_2 = State(name="Arizona")
state_2.save()

city_1 = City(state_id=state_1.id, name="Napa")
city_1.save()
city_2 = City(state_id=state_1.id, name="Sonoma")
city_2.save()
city_3 = City(state_id=state_2.id, name="Page")
city_3.save()

# Test the cities property
for state in storage.all(State).values():
    print("State: {}".format(state.name))
    for city in state.cities:
        print("  City: {}".format(city.name))

# Close storage and check
storage.close()
