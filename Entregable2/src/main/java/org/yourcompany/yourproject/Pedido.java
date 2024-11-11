package org.yourcompany.yourproject;

import java.util.concurrent.ForkJoinPool;

class Pedido implements Comparable<Pedido> {

    private static int count = 0;
    private String id;
    private boolean urgente;

    public Pedido(String id, boolean urgente) {
        this.id = id;
        this.urgente = urgente;
    }

    public String getId() {
        return id;
    }

    public boolean isUrgente() {
        return urgente;
    }

    @Override
    public int compareTo(Pedido otroPedido) {

        return Boolean.compare(otroPedido.urgente, this.urgente);
    }

    public void procesarPago() throws InterruptedException {
        System.out.println("Procesando pago para " + this.id);
        Thread.sleep(1000); // Simula el tiempo de procesamiento
    }

    public void empaquetarPedido() throws InterruptedException {
        System.out.println("Empaquetando " + this.id);
        ForkJoinPool.commonPool().submit(() -> {
            try {
                System.out.println("Imprimiendo etiquetas para " + this.id);
                Thread.sleep(500); // Simula el empaquetado
            } catch (InterruptedException ex) {
            }
        }).join();
    }

    public void enviarPedido() throws InterruptedException {
        System.out.println("Enviando " + this.id);
        Thread.sleep(1000); // Simula el envío
    }
}
