package org.yourcompany.yourproject;

import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

class PedidoTest {

    @Test
    void testProcesarPago() throws InterruptedException {
        Pedido pedido = new Pedido("Pedido1", false);
        pedido.procesarPago();
        assertEquals("Pedido1", pedido.getId());
    }

    @Test
    void testEmpaquetarPedido() throws InterruptedException {
        Pedido pedido = new Pedido("Pedido2", false);
        pedido.empaquetarPedido();
        assertEquals("Pedido2", pedido.getId());
    }

    @Test
    void testEnviarPedido() throws InterruptedException {
        Pedido pedido = new Pedido("Pedido3", false);
        pedido.enviarPedido();
        assertEquals("Pedido3", pedido.getId());
    }

    @Test
    void testPedidoUrgentePrioridad() {
        Pedido pedidoUrgente = new Pedido("PedidoUrgente", true);
        Pedido pedidoNormal = new Pedido("PedidoNormal", false);

        assertTrue(pedidoUrgente.compareTo(pedidoNormal) < 0, "El pedido urgente debería tener prioridad.");
    }

    @Test
    void testProcesarPedidos() throws InterruptedException, ExecutionException {
        List<Pedido> pedidos = Arrays.asList(
                new Pedido("Pedido1", false),
                new Pedido("Pedido2", true),
                new Pedido("Pedido3", false)
        );

        for (Pedido pedido : pedidos) {
            PedidoProcessor.pedidosQueue.offer(pedido);
        }

        Future<String> resultado1 = PedidoProcessor.procesarPedido(pedidos.get(0));
        Future<String> resultado2 = PedidoProcessor.procesarPedido(pedidos.get(1));

        assertEquals("Pedido Pedido1 procesado", resultado1.get());
        assertEquals("Pedido Pedido2 procesado", resultado2.get());
    }
}
