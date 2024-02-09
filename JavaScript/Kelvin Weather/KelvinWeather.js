//The constant variable never change
const kelvin = 293;
console.log(`The temperature is ${kelvin} degrees Kelvin`)
//Celsius is equal to 'kelvin' substract 273
let celsius = kelvin - 273;
Math.floor(celsius);
console.log(`The temperature is ${celsius} degrees Celsius`);
//Farenheit is celsius*(9/5) + 32
let farenheit = celsius*(9/5) + 32
//floor method
Math.floor(farenheit);
console.log(`The temperature is ${farenheit} degrees Farenheit`);

let newton = celsius*(33/100);
