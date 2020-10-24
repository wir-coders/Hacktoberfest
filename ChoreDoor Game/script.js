const doorImage1 = document.getElementById("door1");
const doorImage2 = document.getElementById('door2');
const doorImage3 = document.getElementById('door3');
const botDoorPath = 'https://content.codecademy.com/projects/chore-door/images/robot.svg';
const beachDoorPath = 'https://content.codecademy.com/projects/chore-door/images/beach.svg';
const spaceDoorPath = 'https://content.codecademy.com/projects/chore-door/images/space.svg';
const numClosedDoors = 3;
let openDoor1;
let openDoor2;
let openDoor3;
const closedDoorPath = 'https://content.codecademy.com/projects/chore-door/images/closed_door.svg';
let startButton = document.getElementById('start');

const isClicked = (door) =>{
    if(door.src === closedDoorPath){
        return false;
    }
    else{
        return true;
    }
}

const playDoor = () => {
    numClosedDoors--;
    if(numClosedDoors === 0){
        gameOver('win');
    }
}

const randomChoreDoorGenerator = () => {
    const chorDoor = Math.floor(Math.random() * numClosedDoors);
    if(chorDoor === 0){
        openDoor1 = botDoorPath; 
        openDoor3 = beachDoorPath;
        openDoor2 = spaceDoorPath;
    }
    else if(chorDoor === 1){
        openDoor1 = beachDoorPath;
        openDoor2 = botDoorPath;
        openDoor3 = spaceDoorPath;
    }
    else if(chorDoor === 2){
        openDoor3 = botDoorPath;
        openDoor2 = beachDoorPath;
        openDoor1 = spaceDoorPath;
    }
}

doorImage1.onclick = () => {
    if(!isClicked(doorImage1)){
        doorImage1.src = openDoor1;
        playDoor();
    }
    
}

doorImage2.onclick = () => {
    if(!isClicked(doorImage2)){
        doorImage2.src = openDoor2;
        playDoor();
    }
    
}

doorImage3.onclick = () => {
    if(!isClicked(doorImage3)){
        doorImage3.src = openDoor3;
        playDoor();
    }
    
}

const gameOver = (status) => {
    if(status === 'win'){
        startButton.innerHTML = 'You Win! Play again?'
    }
}

randomChoreDoorGenerator();