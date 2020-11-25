// Sleep Debt Calculator

const getSleepHours = (day) => {
  switch(day){
    case 'monday' : return 8;
    break;
    case 'tuesday' : return 7;
    break;
    case 'wednesday' : return 9;
    break;
    case 'thursday' : return 8;
    break;
    case 'friday' : return 8;
    break;
    case 'saturday' : return 9;
    break;
    case 'sunday' : return 9;
    break;
  }
};
const getActualSleepHours = () => {
  const sleepHours = getSleepHours('monday') + getSleepHours('tuesday') + getSleepHours('wednesday') + getSleepHours('thursday') + getSleepHours('friday') + getSleepHours('saturday') + getSleepHours('sunday');
  return sleepHours;
};

const getIdealSleepHours = () => {
  const idealHours = 8 * 7; //8 is ideal sleep hours
  return idealHours;
};

const calculateSleepDebt = () => {
  const actualSleepHours = getActualSleepHours();
  const idealSleepHours = getIdealSleepHours();
  if(actualSleepHours === idealSleepHours){
    console.log('Perfect Amount of Sleep!');
  }
  else if(actualSleepHours > idealSleepHours){
    console.log(`You got ${actualSleepHours - idealSleepHours} hours more sleep than needed...`);
  }
  else{
    console.log(`You got ${idealSleepHours - actualSleepHours} hours of sleep and should get some sleep...`);
  }
};
calculateSleepDebt();
