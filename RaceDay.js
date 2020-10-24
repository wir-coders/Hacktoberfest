// Race Day Project

let raceNumber = Math.floor(Math.random() * 1000);
const registeredEarly = false;
const runnerAge = 18;
if(runnerAge>18 && registeredEarly){
  raceNumber += 1000;
}
if(runnerAge > 18 && registeredEarly){
  console.log(`Hey ${raceNumber}!, your race will start at 9:30 am`);
}
else if(runnerAge > 18 && !registeredEarly){
  console.log(`Hey ${raceNumber}!, your race will start at 11:00`);
}
else if(runnerAge < 18 ){
  console.log(`Hey ${raceNumber}!, your race will start at 12:30pm`);
}
else{
  console.log('See Registration Desk');
}
