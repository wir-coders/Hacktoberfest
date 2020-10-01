class Weather{
    constructor(city,country){
        this.apikey = '3da1c682366142555509d578aa67ac2b';
        this.city = city;
        this.country = country;
    }

    //fetch weather from the api 
    async getWeather(){
        const response = await fetch(`http://api.openweathermap.org/data/2.5/weather?q=${this.city},${this.country}&APPID=${this.apikey}`);

        const responseData = await response.json();

        return responseData
    }

    //change weather
    changeLocation(city,country){
        this.city = city;
        this.country = country;
    }
}