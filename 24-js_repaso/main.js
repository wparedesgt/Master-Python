alert('Hola Mundo');

var nombre = "William Paredes";
var altura = 173;
var contatenacion = nombre + " " + altura;

document.write(nombre);
document.write(altura);
document.write(contatenacion);

var datos = document.getElementById("datos");



datos.innerHTML = `
    <h1>Soy una caja de datos<h1/>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>Mido: ${altura} cm<h3/>
`;

if(altura >= 190){
    datos.innerHTML += '<h1>Eres una persona Alta<h1>';    
}else{
    datos.innerHTML += '<h1>Eres una persona Baja<h1/>'
}

for(var i = 2015; i <= 2021; i++){
    //Bloque de instrucciones
    datos.innerHTML += "<h2>estamos en el año:</h2>"+i;

}

function MuestraMiNombre(nombre, altura){
    var misDatos = `
    <h1>Soy una caja de datos<h1/>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>Mido: ${altura} cm<h3/>
    `;

    return misDatos;
}

function imprimir(){
    var datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre("William Paredes", 173)
}

imprimir();

var nombres = ['Victor','Antonio', 'Joaquin'];

alert(nombres[1]);

nombres.forEach((nombre) => {
    document.write(nombre + '<br/>')
})

