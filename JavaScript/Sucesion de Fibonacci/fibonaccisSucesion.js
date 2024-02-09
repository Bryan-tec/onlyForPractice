let lista = [];

for (let i = 0; i <= 50; i ++){
    if (i != 0 && i!=1) {
        lista[i] = lista[i-2] + lista[i-1];
    } else {
        lista[i] = i   
    }
}
console.log(lista)