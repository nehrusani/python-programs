<div id="screen1">
    <input id="text_input1" placeholder="Name">
        <input id="text_input2" placeholder="Age">
            <input id="text_input3" placeholder="Place">
                <button id="generate">Generate</button>
            </div>

            <div id="screen2" class="screen">
                <pre id="label1"></pre>
                <button id="back2">Back</button>
            </div>

            <div id="screen3" class="screen">
                <pre id="label4"></pre>
                <button id="back3">Back</button>
            </div>

            <div id="screen4" class="screen">
                <pre id="label2"></pre>
                <button id="back4">Back</button>
            </div>

            <div id="screen5" class="screen">
                <pre id="name1"></pre>
                <button id="back5">Back</button>
            </div>

            <div id="screen6" class="screen">
                <p>Generated!</p>
            </div>

            <style>
                .screen {display: none; }
            </style>


function setScreen(id) {
    document.querySelectorAll(".screen").forEach(s => s.style.display = "none");
    document.getElementById(id).style.display = "block";
}

function getUserInfo() {
    const name = document.getElementById("text_input1").value;
    const age = document.getElementById("text_input2").value;
    const place = document.getElementById("text_input3").value;

    const now = new Date();
    const date = now.toLocaleDateString();
    const time = now.toLocaleTimeString();

    return (
        "Name: " + name +
        "\nAge: " + age +
        "\nVisitingPlace: " + place +
        "\nDate: " + date +
        "\nTime: " + time
    );
}

document.getElementById("generate").addEventListener("click", () => {
    setScreen("screen6");
});

document.getElementById("button2")?.addEventListener("click", () => {
    document.getElementById("name1").textContent = getUserInfo();
    setScreen("screen5");
});

document.getElementById("button3")?.addEventListener("click", () => {
    document.getElementById("label4").textContent = getUserInfo();
    setScreen("screen3");
});

document.getElementById("button4")?.addEventListener("click", () => {
    document.getElementById("label1").textContent = getUserInfo();
    setScreen("screen2");
});

document.getElementById("button5")?.addEventListener("click", () => {
    document.getElementById("label2").textContent = getUserInfo();
    setScreen("screen4");
});

