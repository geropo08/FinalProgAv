package org.yourcompany.yourproject;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.PriorityBlockingQueue;

public class PedidoProcessor {

    private static final int N_HILOS = 10;
    public static final ExecutorService executorService = Executors.newFixedThreadPool(N_HILOS);
    public static final PriorityBlockingQueue<Pedido> pedidosQueue = new PriorityBlockingQueue<>();

    // Simulación de las etapas del procesamiento del pedido
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        // Crear algunos pedidos para procesar

        List<Pedido> pedidos = Arrays.asList(
                new Pedido("Pedido1", false),
                new Pedido("Pedido2", true),
                new Pedido("Pedido3", true),
                new Pedido("Pedido4", true),
                new Pedido("Pedido5", true),
                new Pedido("Pedido6", true),
                new Pedido("Pedido7", true),
                new Pedido("Pedido8", true),
                new Pedido("Pedido9", true),
                new Pedido("Pedido10", true),
                new Pedido("Pedido11", true),
                new Pedido("Pedido12", true),
                new Pedido("Pedido13", true),
                new Pedido("Pedido14", true),
                new Pedido("Pedido15", true),
                new Pedido("Pedido16", true),
                new Pedido("Pedido17", true),
                new Pedido("Pedido18", true),
                new Pedido("Pedido19", true),
                new Pedido("Pedido20", true),
                new Pedido("Pedido21", true),
                new Pedido("Pedido22", true),
                new Pedido("Pedido23", true),
                new Pedido("Pedido24", true),
                new Pedido("Pedido25", true),
                new Pedido("Pedido26", true),
                new Pedido("Pedido27", true),
                new Pedido("Pedido28", true),
                new Pedido("Pedido29", true),
                new Pedido("Pedido30", true),
                new Pedido("Pedido31", true),
                new Pedido("Pedido32", true),
                new Pedido("Pedido33", true),
                new Pedido("Pedido34", true),
                new Pedido("Pedido35", true),
                new Pedido("Pedido36", true),
                new Pedido("Pedido37", true),
                new Pedido("Pedido38", true),
                new Pedido("Pedido39", true),
                new Pedido("Pedido40", true),
                new Pedido("Pedido41", true),
                new Pedido("Pedido42", true),
                new Pedido("Pedido43", true),
                new Pedido("Pedido44", true),
                new Pedido("Pedido45", true),
                new Pedido("Pedido46", true),
                new Pedido("Pedido47", true),
                new Pedido("Pedido48", true),
                new Pedido("Pedido49", true),
                new Pedido("Pedido50", true),
                new Pedido("Pedido51", true)
        );

        // Encolar pedidos
        for (Pedido pedido : pedidos) {
            pedidosQueue.offer(pedido);
        }

        // Procesar pedidos concurrentemente
        List<Future<String>> resultados = new ArrayList<>();
        while (!pedidosQueue.isEmpty()) {
            Pedido pedido = pedidosQueue.poll();
            Future<String> resultado = procesarPedido(pedido);
            resultados.add(resultado);
        }

        // Esperar a que todos los pedidos se procesen y mostrar resultados
        for (Future<String> resultado : resultados) {
            System.out.println("Resultado: " + resultado.get());
        }

        // Apagar el pool de hilos
        executorService.shutdown();
    }

    // Procesamiento de un pedido, que incluye las tres etapas.
    static Future<String> procesarPedido(Pedido pedido) {
        return executorService.submit(() -> {
            pedido.procesarPago();
            pedido.empaquetarPedido();
            pedido.enviarPedido();
            return "Pedido " + pedido.getId() + " procesado";
        });
    }

    // Simulaciones de las etapas del pedido
}
