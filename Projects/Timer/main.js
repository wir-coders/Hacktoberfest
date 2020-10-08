var time={
    h:0,
    m:0,
    s:0
}
var temporaryTime={
    h:0,
    m:0,
    s:0
}
const numbersTimer = (el) => {
    if(el.value.length<2){
        el.value='0'+el.value;
    }else if(el.value.length>2){
        el.value=el.value.substring(1,3)
    }
    // el.value.replace()
}
var timer;

const attDivs = () =>{
    if(time.h < 10){
        document.getElementById('hoursShow').innerHTML = '0' + time.h;
    }else{
        document.getElementById('hoursShow').innerHTML=time.h;
    }
    if(time.m < 10){
        document.getElementById('minutesShow').innerHTML = '0' + time.m;
    }else{
        document.getElementById('minutesShow').innerHTML=time.m;
    }
    if(time.s < 10){
        document.getElementById('secondsShow').innerHTML = '0' + time.s;
    }else{
        document.getElementById('secondsShow').innerHTML=time.s;
    }
}

document.getElementById('hours').onkeypress = () => {
    setTimeout(() => {
        numbersTimer(document.getElementById('hours'));
        if(document.getElementById('hours').value<0){
            document.getElementById('hours').value='00'
        }
    },5)
}
document.getElementById('minutes').onkeypress = () => {
    setTimeout(() => {
        numbersTimer(document.getElementById('minutes'));
        if(document.getElementById('minutes').value>59){
            document.getElementById('minutes').value=59
        }else if(document.getElementById('minutes').value<0){
            document.getElementById('minutes').value='00'
        }
    },5)
}
document.getElementById('seconds').onkeypress = () => {
    setTimeout(() => {
        numbersTimer(document.getElementById('seconds'));
        if(document.getElementById('seconds').value>59){
            document.getElementById('seconds').value=59
        }else if(document.getElementById('seconds').value<0){
            document.getElementById('seconds').value='00'
        }
    },5)
}

document.getElementById('start').onclick = () => {
    startTimer()
}
const startTimer = () => {
    
    time={
        h:parseInt(document.getElementById('hours').value),
        m:parseInt(document.getElementById('minutes').value),
        s:parseInt(document.getElementById('seconds').value)
    }
    if(time.s === 0 && time.m === 0 && time.h ===0){
        return;
    }
    timer = setInterval(() => {
        time.s = time.s - 1;
        if(time.s === 0){
            if(time.m === 0){
                let audio = new Audio('beep-06.mp3');
                audio.play()
                document.getElementById('stop').click();
                return;
            }
            time.m = time.m - 1;
            time.s = 59
            if(time.m === 0){
                if(time.h === 0){
                    let audio = new Audio('beep-06.mp3');
                    audio.play()
                    document.getElementById('stop').click();
                    return;
                }
                time.h = time.h - 1;
                time.m = 59
            }
        }
        attDivs();
    }, 1000)
    document.getElementById('hours').style.display = 'none';
    document.getElementById('minutes').style.display = 'none';
    document.getElementById('seconds').style.display = 'none';
    attDivs();
    document.getElementById('start').innerHTML = "Stop timer";
    document.getElementById('start').id = "stop";
    document.getElementById('stop').onclick = () => {
        document.getElementById('hoursShow').innerHTML = ''
        document.getElementById('minutesShow').innerHTML = ''
        document.getElementById('secondsShow').innerHTML = ''
        document.getElementById('hours').style.display = 'block';
        document.getElementById('minutes').style.display = 'block';
        document.getElementById('seconds').style.display = 'block';
        clearInterval(timer);
        document.getElementById('stop').innerHTML = "Start timer";
        document.getElementById('stop').id = "start";
        document.getElementById('start').onclick = () => {
            startTimer()
        }
    }
}