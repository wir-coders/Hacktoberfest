//init storage
const storage = new Storage();

//get stored locationdata

const weatherLocation = storage.getLocationData();
console.log(weatherLocation);

//init weather object 

const weather = new Weather(weatherLocation.city,weatherLocation.country);




//init ui

const ui = new UI();
//get weather on dom load 
document.addEventListener('DOMContentLoaded',getWeather);

//change location event
document.getElementById('w-change-btn').addEventListener('click',(e)=>{
    const city = document.getElementById('city').value;
    const country = document.getElementById('country').value;

    weather.changeLocation(city,country);



    //set location in local storage
    storage.setLocationData(city,country);

    //call get weather again for new query
    getWeather();

    //close model
    $('#locModal').modal('hide');

});



//weather location delhi,india
function getWeather(){
weather.getWeather()
.then(results=>{
    ui.paint(results);
})
.catch(err=>console.log(err));
}