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
    
    # ~~~ SCORING TABLE ~~~
    #TODO: Implement Scores for: 
    # 1) Legal Crossing 
    # 2) Peds in lane
    # 3) You in car
    
    # CHAR_TYPES: Human = 1, Animal = 0 / Animals should not be given a higher priority than Human
    
    # ANIMAL_TYPES: Cat = 0, Dog = 0
    
    # AGE_TYPES: Child = 4, Baby = 3, Adult = 2, Eldery = 1 / 
    
    # PROF_TYPES: Docter = 5, CEO = 4, Unemployed = 3, Unkown = 2, Homeless = 1, Criminal = 0
    
    # GENDER_TYPES: Female = 2, Male = 1
    
    # PREGNANT_CHANCE: True = 1, False = 0
    
    # BODYWEIGHT_CHANCE: Average = 2, Athletic = 2, Overweight = 1
    
    
    #TODO: 1) Implement the logic using the info stated above. Be sure to add a default case for when the scores are equal.
    #TODO: 2) Explain why you programed the algorithm in this way, why did you decided to give the scores that you did.
    
    # initialize the scores
    passScore = 0
    pedScore = 0 
    
    # loop through each person in the scenario and increment the score based on the scenario info 
    for person in scenario.passengers:
        if person.charType == "human":
            passScore += 1
        elif person.charType == "animal":
            passScore += 0
            
        if person.age == "child":
            passScore += 4
        elif person.age == "baby":
            passScore += 3
        elif person.age == "adult":
            passScore += 2
        elif person.age == "elderly":
            passScore += 1
            
        if person.profession == "doctor":
            passScore += 5
        elif person.profession == "CEO":
            passScore += 4
        elif person.profession == "unemployed":
            passScore += 3
        elif person.profession == "Unkown":
            passScore += 2
        elif person.profession == "homeless":
            passScore += 1
        elif person.profession == "criminal":
            passScore += 0    
    
        if person.gender == "female":
            passScore += 2
        elif person.gender == "male":
            passScore += 1    
    
        if person.pregnant:
            passScore += 1
            
        if person.bodyType == "average":
            passScore += 2
        elif person.bodyType == "athletic":
            passScore += 2
        elif person.bodyType == "overweight":
            passScore += 1
    
    for person in scenario.pedestrians:
        if person.charType == "human":
            passScore += 1
        elif person.charType == "animal":
            passScore += 0
            
        if person.age == "child":
            passScore += 4
        elif person.age == "baby":
            passScore += 3
        elif person.age == "adult":
            passScore += 2
        elif person.age == "elderly":
            passScore += 1
            
        if person.profession == "doctor":
            passScore += 5
        elif person.profession == "CEO":
            passScore += 4
        elif person.profession == "unemployed":
            passScore += 3
        elif person.profession == "Unkown":
            passScore += 2
        elif person.profession == "homeless":
            passScore += 1
        elif person.profession == "criminal":
            passScore += 0    
    
        if person.gender == "female":
            passScore += 2
        elif person.gender == "male":
            passScore += 1    
    
        if person.pregnant:
            passScore += 1
            
        if person.bodyType == "average":
            passScore += 2
        elif person.bodyType == "athletic":
            passScore += 2
        elif person.bodyType == "overweight":
            passScore += 1
            
    if passScore > pedScore:
        print(passScore)
        print(pedScore)
        return "passengers"
    elif passScore < pedScore:
        print(passScore)
        print(pedScore)
        return "pedestrians"
    else:
        print(passScore)
        print(pedScore)
        return "pedestrians" # Because the pedestrians didnt decide to get in the vehicle
    
    # This was a default case provided by the professor
    #if len(scenario.passengers) > len(scenario.pedestrians):
     #   return "passengers"
    #else:
     #   return "pedestrians"
    