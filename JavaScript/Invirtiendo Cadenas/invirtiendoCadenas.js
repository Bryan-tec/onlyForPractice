let palabra = prompt("Escribe unqa palabra: ");
var separarCadena = palabra.split("");
var voltearCadena = separarCadena.reverse();
var unirCadena = voltearCadena.join("");

console.log(unirCadena);