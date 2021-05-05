let fermentables = {}
//input fermentable, uses the fermentable dry basis extraction value and humidity
//output Points per Kilo Liter
function calcExtractedSugar(fermentable){
    moisture = fermentable.humidity
    dryBasisExtraction =fermentable.dryBasis
    estimatedExtraction = (dryBasisExtraction-1)*(1-moisture);
    return estimatedExtraction
}

//input estimated extracton rate, homebrewunit
//output expected homebre units
function calcPKL (estimatedExtraction,homebrewUnit) {
     var sucrose = none
    if (homebrewUnit=="pgg"){
        sucrose = 46;
    } else {
        sucrose = 384;
    }
    homebrewUnitsExtracted = sucrose * estimatedExtraction;
    return homebrewUnitsExtracted;
}

function calcSG (fermentables,preBoilVolume,brewhouseEfficiency){
    var gravityPoints= 0
    for (fermentable of fermentables){
        var fermentableGravityPoints = calcPKL(calcPKL(fermentable.fermentable))*fermentable.amount*brewhouseEfficiency/preBoilVolume;
        gravityPoints += fermentableGravityPoints;
    }
    var startingGravity = 1;
    startingGravity += gravityPoints/100
    return startingGravity
}

function calcOG (fermentables,postBoilVolume,brewhouseEfficiency){
    var gravityPoints= 0
    for (fermentable of fermentables){
        var fermentableGravityPoints = calcPKL(calcPKL(fermentable.fermentable))*fermentable.amount*brewhouseEfficiency/postBoilVolume;
        gravityPoints += fermentableGravityPoints;
    }
    var originalGravity = 1;
    originalGravity += gravityPoints/100
    return originalGravity
}

function calcFG (originalGravity,yeast){
    let pointsOG = (originalGravity-1)*100;
    let pointsFG = pointsOG - pointsOG*yeast.attenuation;
    let finalGravity = 1+(pointsFG/100)
    return finalGravity
}

function calcABV (originalGravity, finalGravity){
    let alcoholByVolume = (originalGravity-finalGravity)*131.25;
    return alcoholByVolume
}

function findHopUtiliation(time){
    //TooDo look up hop utilization timings
    return utilization
}

function calcIBU (hops,postBoilVolume,originalGravity) {
    let totalIBU = 0;
    for (hop of hops){
        let utilization = hopUtilization(hop.time);
        let hopIBU = (hop.ammount*hop.alphaacid*utilization*1000)/(postBoilVolume*originalGravity);
        totalIBU += hopIBU;
    }
    return totalIBU
}