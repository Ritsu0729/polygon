onload = function() {
    read();
}

function buttonClick(event) {
    draw(inputs.value);
}

function read(event) {
    let inputs = document.getElementById("inputs");
    let msg = document.getElementById("msg");
    
    let click = document.getElementById("button");
    click.addEventListener("click", buttonClick, false);
    return inputs.value;
}


function draw(number) {
    var canvas = document.getElementById("rectangle");
    if (!canvas || !canvas.getContext) {
        return false;
    }
    var cvs = canvas.getContext("2d");
    let linecolor = cvs.createLinearGradient(0, 0, 400, 400);

    linecolor.addColorStop(0, "#00ff00");
    linecolor.addColorStop(0.2, "#00ffff");
    linecolor.addColorStop(0.4, "#0000ff");
    linecolor.addColorStop(0.6, "#ff00ff");
    linecolor.addColorStop(0.8, "#ff0000");
    linecolor.addColorStop(1.0, "#ffff00");

    if (check.checked) {
        cvs.clearRect(0, 0, canvas.width, canvas.height);
    }

    var n = number;
    var angle = 360/n;
    var x = 0;
    var y = 0;
    var i = 1;
    var x_first = Math.cos(angle*(Math.PI/180))*200;
    var y_first = Math.sin(angle*(Math.PI/180))*200;

    //図形描画
    cvs.beginPath();
    cvs.strokeStyle = linecolor;
    cvs.lineWidth = 2;
    cvs.moveTo(200+x_first, 200-y_first);
    while (Math.floor(x) != Math.floor(x_first) || Math.floor(y) != Math.floor(y_first)) {
        x = Math.cos(angle*(i+1)*(Math.PI/180))*200;
        y = Math.sin(angle*(i+1)*(Math.PI/180))*200;
        cvs.lineTo(200+x, 200-y);
        cvs.stroke();
        i += 1;
    }
    cvs.closePath();
    cvs.stroke();

}