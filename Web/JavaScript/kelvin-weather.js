//stores current temperature in kelvin
const kelvin = 0; 

//converts kelvin to celsius
const celsius = kelvin - 273; 

//converts celsius to fahrenheit
let fahrenheit = celsius * (9/5) + 32; 
//removes decimal point
fahrenheit = Math.floor(fahrenheit); 

//Output results
console.log("Kelvin: " + kelvin);
console.log("\nCelsius: " + celsius);
console.log("\nFahrenheit: " + fahrenheit);