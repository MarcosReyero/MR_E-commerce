function agregarAlCarrito(productoId) {
    alert(`Producto ${productoId} añadido al carrito.`);
    //Acá podrias hacer una llamada AJAX para añadir el producto al carrito en el servidor.
}

function removerDelCarrito(productoId) {
    alert(`Producto ${productoId} removido del carrito.`);
    // Acá podrias hacer una llamada AJAX para remover el producto del carrito en el servidor.
}

document.getElementById('checkout-form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Pedido realizado con éxito.');
    // Acá podrías hacer una llamada AJAX para enviar los datos del pedido al servidor.
});
