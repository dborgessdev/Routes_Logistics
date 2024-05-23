function atualizarCartoes() {
    $.get("/get_cartoes", function(data) {
        // Limpa a lista antes de atualizar
        $("#cartoes-list").empty();

        // Adiciona os cartões à lista
        $.each(data, function(key, value) {
            $("#cartoes-list").append("<li>" + value + "</li>");
        });
    });
}

// Chama a função atualizarCartoes a cada 5 segundos
var intervalId;

function startUpdate() {
    intervalId = setInterval(atualizarCartoes, 5000);
}

// Para de chamar a função quando a página for fechada
function stopUpdate() {
    clearInterval(intervalId);
}

// Chama startUpdate quando a página for carregada
$(document).ready(function() {
    atualizarCartoes();
    startUpdate();
});

// Chama stopUpdate quando a página for fechada
$(window).on("unload", function() {
    stopUpdate();
});
