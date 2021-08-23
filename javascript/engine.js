// import {scenario} from './scenario.js'


function decide(scenario){
    // Properties you have access to in scenario:
    // scenario.pedsInLane (if true pedestrians are in same lane as car)
    // scenario.legalCrossing (if true pedestrians are crossing legally)
    // scenario.passengers and scenario.pedestrians (arrays of person objects)
    // attributes in each person object:
    // person.charType: human, dog, cat, you 
    // person.age: baby, child, adult, elderly 
    // person.gender: male, female 
    // person.bodyType: overweight, athletic, average  
    // person.pregnant: true, false
    // person.profession: doctor, CEO, criminal, homeless, unemployed, unknown 


    //This simply demonstrates how to access information from the scenario.
    // console.log("Are the pedestrians crossing legally?", scenario.legalCrossing)
    // console.log ("Is the car in the same lane as the pedestrians?", scenario.pedsInLane)
    // console.log("Are you in car?", scenario.youInCar)

    // console.log("Print whether each pedestrian is a human, animal, or you")
    // for(let x = 0; x < scenario.pedestrians.length; x++){
    //     let person = scenario.pedestrians[x]
    //     console.log(person.charType)
    // }



    //Your program must choose to save either pedestrians or passengers.
    //This is an overly simple rule that only saves the passengers if there are
    //more passengers than pedestrians.

    if (scenario.passengers.length > scenario.pedestrians.length){
        return "passengers"
    }else{
        return "pedestrians"
    }



}

export{decide}