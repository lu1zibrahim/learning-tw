/*
// == Igualdade, no JS compara os "valores" não inclui tipos
console.log(10=="10");
// !- Desigualdade
console.log(10!=3);
// === Extritamente igual, strict equal
console.log(10==="10");
// > Maior
console.log(10>10);
// >= Maior ou igual
console.log(10>=10);
// < Menor
console.log(10<10);
// <= Menor ou Igual
console.log(10<=10);

// ! NEGAR
console.log(!(10 >10));

// || OU
console.log((10 == 10) || (10 >20));

// && E
console.log((10 == 10) && (10 > 20));

console.log((10 == 10) && ((10 > 20) || (10 > 10)));
//                         (Isso Tudo Aqui vai ser verdadeiro)

*/

/* let idade = 62;

// 0 - 17 = " Sou menor de idade"
// 18 - 60 = "Sou Adulto"
// 60 = "Estou na melhor idade"
if (idade <=17){
    console.log("Sou menor de idade")
} else if (idade >17 && idade <60) {
    console.log("Sou adulto");
} else {
    console.log("Estou na melhor idade")
} */

// 1 - Cadastrar
// 2 - Listar
// 3 - Pesquisa
// 4 - Sair
/* 
let menu= 2;
switch (menu) {
    case 1:
        console.log("Cadastrar");
        break;
    case 2:
        console.log("Listar");
        break;
    case 3:
        console.log("Pesquisar");
        break;
    default:
        console.log("Sair");
}
 */
/* //for
 for (var i=0; i < 10; i++) {
     console.log("Olá mundo")
 }
 
 //While
 var j =0
 while (j < 10) {
     console.log("Olá mundo");
    j++;
 }
  */
/*  function verificarIdade(idade) {
     if (idade <=17){
        return "Sou menor de idade"
    } else if (idade >17 && idade <60) {
        return "Sou adulto";
    } else {
        return "Estou na melhor idade";
    }
 }
 
 console.log(verificarIdade(5));
 console.log(verificarIdade(25));
 console.log(verificarIdade(65));
 */
/* 

Exercicio 1 -
var velocidade = 278280;
var distancia = 570000000;
var veldia = velocidade*24;

var total = distancia / veldia;

console.log(total); */


/* Exercicio 2
function verificarEstoque(estoqueAtual,estoqueMinimo, estoqueMaximo) {
    var estoqueMedia = (estoqueMaximo + estoqueMinimo) / 2;
    if (estoqueAtual >= estoqueMedia) {
    return "Não efetuar a compra";
    } else {
    return "Efetuar a compra";
    }
}

console.log(verificarEstoque(10,2,12)); */


/* // Exercicio 3
function calcularTabuada (num) {
    for(var i = 1; i <=10; i++) {
    console.log(num*i);
    }
}

console.log(calcularTabuada(2)) */
// Exercicio 4
/* var k = 10;
var vezesPar = 0
var vezesImpar = 0
var i = 1;
while (i <= k) {
    if (i % 2 == 0) {
        vezesPar++;
        i++;
    } else {
        vezesImpar++;
        i++;
    }
}
console.log("Numeros Par " + vezesPar);
console.log("Numeros Impar " + vezesImpar); */

/* //Resolucao Professor
var numero = 10;
var vezesPar = 0
var vezesImpar = 0

while (numero >0) {
    if(numero % 2 ==0){
    vezesPar++;
    } else {
    vezesImpar++;
    }
    numero--;
}
console.log("Numeros Par " + vezesPar);
console.log("Numeros Impar " + vezesImpar); */