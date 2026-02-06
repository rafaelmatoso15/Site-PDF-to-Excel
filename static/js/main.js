// Função para rolar até o formulário
function scrollToForm() {
    const formSection = document.getElementById("orcamento");
    if (formSection) {
        formSection.scrollIntoView({ 
            behavior: "smooth", 
            block: "center" 
        });
    }
}

// FAQ accordion - aguarda o DOM carregar
document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript carregado com sucesso!");

    const faqItems = document.querySelectorAll(".faq-item");
    console.log("Itens FAQ encontrados:", faqItems.length);

    faqItems.forEach(function(item) {
        const button = item.querySelector(".faq-question");

        if (button) {
            button.addEventListener("click", function() {
                const isActive = item.classList.contains("active");

                // Fecha todos os itens
                faqItems.forEach(function(otherItem) {
                    otherItem.classList.remove("active");
                });

                // Abre o item clicado (se não estava aberto)
                if (!isActive) {
                    item.classList.add("active");
                    console.log("FAQ aberto:", button.textContent.trim());
                }
            });
        }
    });
});
