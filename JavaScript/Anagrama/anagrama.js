function anagrama(pal1, pal2)
{
    if(pal1.toLowerCase() === pal2.toLowerCase())
    {
        return false;
    }
    else {
        let palabra1 = pal1.toLowerCase().split("").sort().join("");
        let palabra2 = pal2.toLowerCase().split("").sort().join("");
        //console.log(palabra1, palabra2)
        if(palabra1 == palabra2)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

console.log(anagrama("iman","iman"));