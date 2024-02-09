let raceNumber = Math.floor(Math.random() * 1000);

let registeredEarly = false;
let runnerAge = 13;

if (runnerAge > 17 && registeredEarly == true){
  console.log(`Tu carrera comienza a las 9:30am y tu numero corredor es: ${raceNumber}`)
} else if (runnerAge > 17 && registeredEarly == false){
   console.log(`Tu carrera comienza a las 11:00am y tu numero corredor es: ${raceNumber}`)
} else if (runnerAge < 18){
  console.log(`Tu carrera comienza a las 12:30am y tu numero corredor es: ${raceNumber}`)
} else {
  console.log('Revisa tu registro con la secretaria.')
}

