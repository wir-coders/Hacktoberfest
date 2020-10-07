  
let APPID = "e1802879a56231bbd1806edc8ea2f601";
var currentStyle = 'default';


window.onload = function () {
  var buttonInspect = document.getElementById("button");
  buttonInspect.addEventListener("click", handler);
  var input = document.getElementById("search-city");
  input.addEventListener("keyup", function (event) {
    if (event.keyCode === 13) {
      event.preventDefault();
      document.getElementById("search-city").click();
      searchWeather(input.value);
    }
  });
}


function handler() {
  let city = document.getElementById("search-city").value;
  if (city)
    searchWeather(city);
}

async function searchWeather(city) {
  await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&APPID=${APPID}`)
    .then(result => {
      console.log('Result status: ' + result.status);

      if (result.status >= 400) {
        for (let i = 0; i <= 28; i++) {  
          document.getElementsByClassName('data')[i].innerHTML = '-';
        }

        let icon = document.getElementById("weather-icon");
        if (currentStyle === "dark") {
          icon.src = "icons/solidWhite/unknown.png";
        } else icon.src = "icons/unknown.png";

        for (let i = 1; i <= 12; i++) {
          if (currentStyle === 'dark') {
            document.getElementById("timestamp" + i + "icon").src = "icons/solidWhite/unknown.png";
          } else {
            document.getElementById("timestamp" + i + "icon").src = "icons/unknown.png";
          }
        }
        return alert('Nie znaleziono miasta');
      } else {
        return result.json();
      }

    }).then(result => {
      if (result != undefined) {
        console.log('Result: ' + result);
        init(result);
        searchWeatherForecast(city);
      } else {
        console.log('Result: ' + result);
      }
    })
}

//Fetching weather api: weather forecast;
async function searchWeatherForecast(city) {
  await fetch(`https://api.openweathermap.org/data/2.5/forecast?q=${city}&units=metric&APPID=${APPID}`)
    .then(resultForecast => {
      return resultForecast.json();
    })
    .then(resultForecast => {
      initForecast(resultForecast);
    }).catch(error => {
      console.log(error);
      throw error;
    })
}

//Parsing current weather data
function init(resultFromServer) {
  console.log(resultFromServer);

  let city1 = document.getElementById("city1");
  city1.innerHTML = resultFromServer.name;

  let temperature = document.getElementById("city1-temperature");
  temperature.innerHTML = Math.floor(resultFromServer.main.temp) + "&#176C";
  let icon = document.getElementById("weather-icon");
  if (currentStyle === "dark") {
    icon.src = "icons/solidWhite/" + resultFromServer.weather[0].icon + ".png";
  } else icon.src = "icons/" + resultFromServer.weather[0].icon + ".png";

  let pressure = document.getElementById("city1-pressure");
  pressure.innerHTML = resultFromServer.main.pressure + "&nbsphPa";

  let wind = document.getElementById("city1-wind");
  wind.innerHTML = Math.floor(resultFromServer.wind.speed) + "m/s";

  let clouds = document.getElementById("city1-clouds");
  clouds.innerHTML = resultFromServer.clouds.all + "%";

  //  Video in the background is started based on search result
  let video = document.getElementById("myVideo");
  if (resultFromServer.weather[0].icon === "03d" || resultFromServer.weather[0].icon === "04d") {
    video.src = "video/cloudy.mp4";
    video.playbackRate = 0.85;
  } else if (resultFromServer.weather[0].icon === "03n" || resultFromServer.weather[0].icon === "04n") {
    video.src = "video/cloudy-night.mp4";
    video.playbackRate = 0.75;
  } else if (resultFromServer.weather[0].icon === "09d" || resultFromServer.weather[0].icon === "10d") {
    video.src = "video/rainy.mp4";
  } else if (resultFromServer.weather[0].icon === "09n" || resultFromServer.weather[0].icon === "10n") {
    video.src = "video/rainy-night.mp4";
  } else if (resultFromServer.weather[0].icon === "01d" || resultFromServer.weather[0].icon === "02d") {
    video.src = "video/sunny.mp4";
  } else if (resultFromServer.weather[0].icon === "01n" || resultFromServer.weather[0].icon === "02n") {
    video.src = "video/clear-night.mp4";
  } else if (resultFromServer.weather[0].icon === "13d") {
    video.src = "video/snowy.mp4";
  } else if (resultFromServer.weather[0].icon === "13n") {
    video.src = "video/snowy-night.mp4";
  } else if (resultFromServer.weather[0].icon === "50d") {
    video.src = "video/foggy.mp4";
  } else if (resultFromServer.weather[0].icon === "50n") {
    video.src = "video/foggy-night.mp4";
  } else if (resultFromServer.weather[0].icon === "11d") {
    video.src = "video/thunderstorm.mp4";
  } else if (resultFromServer.weather[0].icon === "11n") {
    video.src = "video/thunderstorm-night.mp4";
  };
}

//  Parsing weather forecast data
function initForecast(resultFromServer) {
  console.log(resultFromServer);
  //Loading timestamp    
  for (let i = 1; i <= 12; i++) {
    document.getElementById("timestamp" + i).innerHTML = resultFromServer.list[i].dt_txt.slice(0, -3).slice(5)
    //If mode is dark, load solid-white weather icons    
    if (currentStyle === 'dark') {
      document.getElementById("timestamp" + i + "icon").src = "icons/solidWhite/" + resultFromServer.list[i].weather[0].icon + ".png";
    } else {
      document.getElementById("timestamp" + i + "icon").src = "icons/" + resultFromServer.list[i].weather[0].icon + ".png";
    }
    //Loading temperature        
    document.getElementById("timestamp" + i + "temperature").innerHTML = Math.floor(resultFromServer.list[i].main.temp) + "&#176C";
  }
}

//Autocomplete function - blocks the search instead of helping!!!
//function initialize() {
//  var input = document.getElementById('search-city');
//  new google.maps.places.Autocomplete(input);
//}
//google.maps.event.addDomListener(window, 'load', initialize);

/* DARK STYLING*/
function dark() {
  currentStyle = 'dark';
  const header1 = document.getElementsByTagName('h1');
  for (let i = 0; i < header1.length; i++) {
    header1[i].style.color = '#d7d7d7';
  }

  const header2 = document.getElementsByTagName('h2');
  for (let i = 0; i < header2.length; i++) {
    header2[i].style.color = '#d7d7d7';
  }
  const header3 = document.getElementsByTagName('h3');
  for (let i = 0; i < header3.length; i++) {
    header3[i].style.color = '#d7d7d7';
  }

  const header4 = document.getElementsByTagName('h4');
  for (let i = 0; i < header4.length; i++) {
    header4[i].style.color = '#d7d7d7';
  }
  const header5 = document.getElementsByTagName('h5');
  for (let i = 0; i < header5.length; i++) {
    header5[i].style.color = '#d7d7d7';
  }
  const button = document.querySelector('button')
  button.className = 'btn btn-dark';
  button.style.border = '1px solid #FFFFFF'

  const contener = document.querySelector('div.contener')
  contener.style.background = "url('img/dark.jpg')";

  //    const navi = document.getElementsByTagName('nav');
  //    navi[0].style.backgroundColor = 'rgba(70, 70, 70, 1)'; 
  //    navi[0].style.borderBottom = "solid #d7d7d7 2px";
  //    const menu = document.getElementById('menu');
  //    menu.style.color = '#d7d7d7';

  const header = document.getElementsByTagName('header');
  header[0].style.backgroundColor = 'rgba(70, 70, 70, 1)';
  header[0].style.color = '#d7d7d7';
  header[0].style.border = "solid #d7d7d7 1px";

  const formControlContainer = document.getElementsByClassName('form-control');
  formControlContainer[0].style.backgroundColor = 'rgba(70, 70, 70, 1)';
  formControlContainer[0].style.color = '#d7d7d7';

  let sliderContainer = document.getElementsByClassName('slider-container');
  sliderContainer[0].style.background = 'rgba(70, 70, 70, 1)';
  sliderContainer[0].style.color = '#d7d7d7';
  sliderContainer[0].style.border = "solid #d7d7d7 1px";

  const previous = document.getElementsByClassName('f-previous')

  for (let i = 0; i < previous.length; i++) {
    previous[i].style.backgroundColor = 'rgba(40, 40, 40, 0.6)';
  }
  const next = document.getElementsByClassName('f-next')
  for (let i = 0; i < next.length; i++) {
    next[i].style.backgroundColor = 'rgba(40, 40, 40, 0.6)';
  }

  let fContainer = document.getElementsByClassName('f-container');
  fContainer[0].style.background = 'rgba(70, 70, 70, 1)';
  fContainer[0].style.color = '#d7d7d7';
  fContainer[0].style.border = "solid #d7d7d7 1px";

  let bigWeatherIcon = document.getElementById("weather-icon");
  if (!bigWeatherIcon.src.includes('solidWhite')) {
    bigWeatherIcon.src = bigWeatherIcon.src.replace("icons/", "icons/solidWhite/");
  }


  for (let i = 1; i <= 12; i++) {
    let smallWeatherIcon = document.getElementById("timestamp" + i + "icon");
    if (!smallWeatherIcon.src.includes('solidWhite')) {
      smallWeatherIcon.src = smallWeatherIcon.src.replace("icons/", "icons/solidWhite/");
    }
  }
  if (!bigWeatherIcon.src.includes('solidWhite')) {
    bigWeatherIcon.src = bigWeatherIcon.src.replace("icons/", "icons/solidWhite/");
  }
}


/* BRIGHT STYLING*/
function bright() {
  currentStyle = 'bright';
  const header1 = document.getElementsByTagName('h1');
  for (var i = 0; i < header1.length; i++) {
    header1[i].style.color = 'rgb(24, 24, 24)';
  }

  const header2 = document.getElementsByTagName('h2');
  for (var i = 0; i < header2.length; i++) {
    header2[i].style.color = 'rgb(24, 24, 24)';
  }
  const header3 = document.getElementsByTagName('h3');
  for (let i = 0; i < header3.length; i++) {
    header3[i].style.color = 'rgb(24, 24, 24)';
  }

  const header4 = document.getElementsByTagName('h4');
  for (let i = 0; i < header4.length; i++) {
    header4[i].style.color = 'rgb(24, 24, 24)';
  }
  const header5 = document.getElementsByTagName('h5');
  for (let i = 0; i < header5.length; i++) {
    header5[i].style.color = 'rgb(24, 24, 24)';
  }
  const button = document.querySelector('button')
  button.className = 'btn btn-primary';
  button.style.border = '1px solid #FFFFFF'

  const contener = document.querySelector('div.contener')
  contener.style.background = "url('img/bright.jpg')";
  contener.style.backgroundSize = 'cover';

  //  const navi = document.getElementsByTagName('nav');
  //  navi[0].style.backgroundColor = 'rgb(255, 255, 255)';
  //  navi[0].style.borderBottom = "solid rgba(255, 255, 0, 0.6) 1px";
  //  const menu = document.getElementById('menu');
  //  menu.style.color = 'rgb(24, 24, 24)';

  const header = document.getElementsByTagName('header');
  header[0].style.backgroundColor = 'rgb(255, 255, 255)';
  header[0].style.color = 'rgb(24, 24, 24)';
  header[0].style.border = "solid rgba(255, 255, 0, 0.6) 1px";
  header[0].style.boxShadow = "0px 3px 3px rgba(0, 0, 0, 0.2)"

  const formControlContainer = document.getElementsByClassName('form-control');
  formControlContainer[0].style.backgroundColor = 'rgb(255, 255, 255)';
  formControlContainer[0].style.color = 'rgb(24, 24, 24)';


  const sliderContainer = document.getElementsByClassName('slider-container');
  sliderContainer[0].style.backgroundColor = 'rgb(255, 255, 255)';
  sliderContainer[0].style.color = 'rgb(24, 24, 24)';
  sliderContainer[0].style.border = "solid rgba(255, 255, 0, 0.6) 1px";

  const previous = document.getElementsByClassName('f-previous')
  for (let i = 0; i < previous.length; i++) {
    previous[i].style.backgroundColor = 'rgba(255, 225, 0, 0.6)';
  }
  const next = document.getElementsByClassName('f-next')
  for (let i = 0; i < next.length; i++) {
    next[i].style.backgroundColor = 'rgba(255, 225, 0, 0.6)';
  }
  let fContainer = document.getElementsByClassName('f-container');
  fContainer[0].style.background = 'rgb(255, 255, 255)';
  fContainer[0].style.color = 'rgb(24, 24, 24)';
  fContainer[0].style.border = "solid rgba(255, 255, 0, 0.6) 1px";


  for (let i = 1; i <= 12; i++) {
    let smallWeatherIcon = document.getElementById("timestamp" + i + "icon");
    if (smallWeatherIcon.src.includes('solidWhite')) {
      smallWeatherIcon.src = smallWeatherIcon.src.replace("icons/solidWhite/", "icons/");
    }
  }
  let bigWeatherIcon = document.getElementById("weather-icon");
  if (bigWeatherIcon.src.includes('solidWhite')) {
    {
      bigWeatherIcon.src = bigWeatherIcon.src.replace("icons/solidWhite/", "icons/");
    }
  }
}


function byDefault() {
  currentStyle = 'default';
  const header1 = document.getElementsByTagName('h1');
  for (var i = 0; i < header1.length; i++) {
    header1[i].style.color = null;
  }

  const header2 = document.getElementsByTagName('h2');
  for (var i = 0; i < header2.length; i++) {
    header2[i].style.color = null;
  }

  const header3 = document.getElementsByTagName('h3');
  for (let i = 0; i < header3.length; i++) {
    header3[i].style.color = null;
  }

  const header4 = document.getElementsByTagName('h4');
  for (let i = 0; i < header4.length; i++) {
    header4[i].style.color = null;
  }
  const header5 = document.getElementsByTagName('h5');
  for (let i = 0; i < header5.length; i++) {
    header5[i].style.color = null;
  }
  const button = document.querySelector('button')
  button.className = 'btn btn-secondary';
  button.style.border = null

  const contener = document.querySelector('div.contener')
  contener.style.background = null;


  const header = document.getElementsByTagName('header');
  header[0].style.backgroundColor = null;
  header[0].style.color = null;
  header[0].style.border = null;
  //  header[0].style.boxShadow = "0px 3px 3px rgba(0, 0, 0, 0.2)"

  const formControlContainer = document.getElementsByClassName('form-control');
  formControlContainer[0].style.backgroundColor = null;
  formControlContainer[0].style.color = null;

  const sliderContainer = document.getElementsByClassName('slider-container');
  sliderContainer[0].style.backgroundColor = null;
  sliderContainer[0].style.color = null;
  sliderContainer[0].style.border = null;

  const previous = document.getElementsByClassName('f-previous')
  for (let i = 0; i < previous.length; i++) {
    previous[i].style.backgroundColor = null;;
  }
  const next = document.getElementsByClassName('f-next')
  for (let i = 0; i < next.length; i++) {
    next[i].style.backgroundColor = null;;
  }
  let fContainer = document.getElementsByClassName('f-container');
  fContainer[0].style.background = null;
  fContainer[0].style.color = null;;
  fContainer[0].style.border = null;


  for (let i = 1; i <= 12; i++) {
    let smallWeatherIcon = document.getElementById("timestamp" + i + "icon");
    if (smallWeatherIcon.src.includes('solidWhite')) {
      smallWeatherIcon.src = smallWeatherIcon.src.replace("icons/solidWhite/", "icons/");
    }
  }
  let bigWeatherIcon = document.getElementById("weather-icon");
  if (bigWeatherIcon.src.includes('solidWhite')) {
    {
      bigWeatherIcon.src = bigWeatherIcon.src.replace("icons/solidWhite/", "icons/");
    }
  }
}