'''
Provides template code to automatically make decisions for the autonomous
car.
'''
from scenario import Scenario
from scenario import Person

def decide(scenario):
    """ Decides whether your car will save the passengers or pedestrians

    Args:
        scenario: a Scenario object defined in scenario.py. This object contains
            all of the information about the scenario. You can see some
            examples below in the sample code.

    Returns:
        A string indicating whether you are saving "passengers" or
        "pedestrians". Note that your method MUST make a decision for
        ANY potential scenario.
    """

    # NOTE: YOU NEED TO REPLACE ALL OF THE CODE BELOW!!!
    # This simply demonstrates how to access information from the scenario.
    # print("Are the pedestrians crossing legally?", scenario.legalCrossing)
    # print("Is the car in the same lane as the pedestrians?", scenario.pedsInLane)
    # print("Are you in car?", scenario.youInCar)
    #
    # print("Print whether each pedestrian is a human, animal, or you")
    # for person in scenario.pedestrians:
    #     print(person.charType)


    # Your program must choose to save either pedestrians or passengers.
    # This is an overly simple rule that only saves the passengers if there are
    # more passengers than pedestrians.
    
    # CHAR_TYPES: Human = 1, Animal = 0
    
    # ANIMAL_TYPES: Cat = 0, Dog = 0
    
    # AGE_TYPES: Child = 4, Baby = 3, Adult = 2, Eldery = 1
    
    # PROF_TYPES: Docter = 5, CEO = 4, Unemployed = 3, Unkown = 2, Homeless = 1, Criminal = 0
    
    # GENDER_TYPES: Female = 2, Male = 1
    
    # PREGNANT_CHANCE: True = 1, False = 0
    
    # BODYWEIGHT_CHANCE: Average = 2, Athletic = 2, Overweight = 1
    
    
    #TODO: #1 Implement the logic using the info stated above. Be sure to add a default case for when the scores are equal.
    #TODO: #2 Explain why you programed the algorithm in this way, why did you decided to give the scores that you did.
    
    # initialize the scores
    passScore = 0
    pedScore = 0 
    
    # loop through each person in the scenario and increment the score based on the scenario info 
    for person in scenario.passengers:
        if person.charType == "human":
            passScore += 1
        elif person.age == "baby" or person.age == "child" or person.age == "adult":
            passScore += 1
        elif person.profession == "doctor" or person.profession == "CEO":
            passScore += 1
        elif person.bodyType == "athletic":
            passScore += 1
        elif person.pregnant:
            passScore += 1
    
    for person in scenario.pedestrians:
        if person.charType == "human":
            pedScore += 1
        elif person.age == "baby" or person.age == "child" or person.age == "adult":
            pedScore += 1
        elif person.profession == "doctor" or person.profession == "CEO":
            pedScore += 1
        elif person.bodyType == "athletic":
            pedScore += 1
        elif person.pregnant:
            pedScore += 1
            
    if passScore > pedScore:
        print(passScore)
        print(pedScore)
        return "passengers"
    else:
        print(passScore)
        print(pedScore)
        return "pedestrians"
    
    # This was a default case provided by the professor
    #if len(scenario.passengers) > len(scenario.pedestrians):
     #   return "passengers"
    #else:
     #   return "pedestrians"
    