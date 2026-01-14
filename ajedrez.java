import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Ajedrez extends JPanel implements MouseListener {

    private static final int TAM = 60;
    private static final String BLANCO = "white";
    private static final String NEGRO = "black";

    private Pieza[][] tablero = new Pieza[8][8];
    private String turno = BLANCO;

    private int selF = -1, selC = -1;
    private java.util.List<Point> movimientos = new java.util.ArrayList<>();

    public Ajedrez() {
        inicializarTablero();
        addMouseListener(this);
        setPreferredSize(new Dimension(480, 480));
    }

    private void inicializarTablero() {
        String[] orden = {"torre", "caballo", "alfil", "reina", "rey", "alfil", "caballo", "torre"};

        for (int i = 0; i < 8; i++) {
            tablero[0][i] = new Pieza(orden[i], NEGRO);
            tablero[1][i] = new Pieza("peon", NEGRO);
            tablero[6][i] = new Pieza("peon", BLANCO);
            tablero[7][i] = new Pieza(orden[i], BLANCO);
        }
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Dibujar casillas
        for (int f = 0; f < 8; f++) {
            for (int c = 0; c < 8; c++) {
                boolean claro = (f + c) % 2 == 0;
                g.setColor(claro ? new Color(238, 238, 210) : new Color(118, 150, 86));
                g.fillRect(c * TAM, f * TAM, TAM, TAM);
            }
        }

        // Movimientos posibles
        g.setColor(Color.BLUE);
        for (Point p : movimientos) {
            g.drawRect(p.y * TAM, p.x * TAM, TAM, TAM);
            g.drawRect(p.y * TAM + 1, p.x * TAM + 1, TAM - 2, TAM - 2);
        }

        // Dibujar piezas
        g.setFont(new Font("Arial", Font.PLAIN, 40));
        for (int f = 0; f < 8; f++) {
            for (int c = 0; c < 8; c++) {
                Pieza p = tablero[f][c];
                if (p != null) {
                    g.drawString(simbolo(p), c * TAM + 15, f * TAM + 45);
                }
            }
        }
    }

    private String simbolo(Pieza p) {
        return switch (p.tipo + p.color) {
            case "reywhite" -> "♔";
            case "reinawhite" -> "♕";
            case "torrewhite" -> "♖";
            case "alfilwhite" -> "♗";
            case "caballowhite" -> "♘";
            case "peonwhite" -> "♙";

            case "reyblack" -> "♚";
            case "reinablack" -> "♛";
            case "torreblack" -> "♜";
            case "alfilblack" -> "♝";
            case "caballoblack" -> "♞";
            case "peonblack" -> "♟";

            default -> "?";
        };
    }

    // ------------------ MOVIMIENTO ------------------

    @Override
    public void mouseClicked(MouseEvent e) {
        int f = e.getY() / TAM;
        int c = e.getX() / TAM;

        if (selF != -1) {
            // Intentar mover
            if (movimientos.contains(new Point(f, c))) {
                mover(selF, selC, f, c);
                turno = turno.equals(BLANCO) ? NEGRO : BLANCO;
            }
            selF = selC = -1;
            movimientos.clear();
        } else {
            Pieza p = tablero[f][c];
            if (p != null && p.color.equals(turno)) {
                selF = f;
                selC = c;
                movimientos = obtenerMovimientosValidos(f, c);
            }
        }

        repaint();
    }

    private void mover(int f0, int c0, int f1, int c1) {
        Pieza pieza = tablero[f0][c0];
        Pieza destino = tablero[f1][c1];

        if (destino != null && destino.tipo.equals("rey")) {
            JOptionPane.showMessageDialog(this, "¡Has ganado!\nPiezas " + pieza.color.toUpperCase());
            System.exit(0);
        }

        tablero[f1][c1] = pieza;
        tablero[f0][c0] = null;

        // Promoción
        if (pieza.tipo.equals("peon") && (f1 == 0 || f1 == 7)) {
            promocionar(f1, c1, pieza.color);
        }
    }

    private void promocionar(int f, int c, String color) {
        String[] opciones = {"reina", "torre", "alfil", "caballo"};
        String tipo = (String) JOptionPane.showInputDialog(
                this, "Promociona tu peón", "Promoción",
                JOptionPane.PLAIN_MESSAGE, null, opciones, opciones[0]
        );
        tablero[f][c] = new Pieza(tipo, color);
    }

    // ------------------ MOVIMIENTOS ------------------

    private java.util.List<Point> obtenerMovimientosValidos(int f, int c) {
        java.util.List<Point> lista = new java.util.ArrayList<>();

        for (int f1 = 0; f1 < 8; f1++) {
            for (int c1 = 0; c1 < 8; c1++) {
                if (movimientoValido(f, c, f1, c1)) {
                    lista.add(new Point(f1, c1));
                }
            }
        }
        return lista;
    }

    private boolean movimientoValido(int f0, int c0, int f1, int c1) {
        Pieza p = tablero[f0][c0];
        Pieza destino = tablero[f1][c1];

        if (destino != null && destino.color.equals(p.color))
            return false;

        int df = f1 - f0;
        int dc = c1 - c0;

        switch (p.tipo) {

            case "peon" -> {
                int d = p.color.equals(BLANCO) ? -1 : 1;
                int filaInicio = p.color.equals(BLANCO) ? 6 : 1;

                if (dc == 0 && df == d && destino == null)
                    return true;

                if (f0 == filaInicio && dc == 0 && df == 2 * d &&
                        destino == null && tablero[f0 + d][c0] == null)
                    return true;

                if (Math.abs(dc) == 1 && df == d && destino != null)
                    return true;
            }

            case "torre" -> {
                if (df == 0 || dc == 0)
                    return caminoLibre(f0, c0, f1, c1);
            }

            case "alfil" -> {
                if (Math.abs(df) == Math.abs(dc))
                    return caminoLibre(f0, c0, f1, c1);
            }

            case "reina" -> {
                if (df == 0 || dc == 0 || Math.abs(df) == Math.abs(dc))
                    return caminoLibre(f0, c0, f1, c1);
            }

            case "caballo" -> {
                return (Math.abs(df) == 1 && Math.abs(dc) == 2) ||
                       (Math.abs(df) == 2 && Math.abs(dc) == 1);
            }

            case "rey" -> {
                return Math.max(Math.abs(df), Math.abs(dc)) == 1;
            }
        }

        return false;
    }

    private boolean caminoLibre(int f0, int c0, int f1, int c1) {
        int df = Integer.compare(f1, f0);
        int dc = Integer.compare(c1, c0);

        int pasos = Math.max(Math.abs(f1 - f0), Math.abs(c1 - c0));

        for (int i = 1; i < pasos; i++) {
            if (tablero[f0 + df * i][c0 + dc * i] != null)
                return false;
        }
        return true;
    }

    // ------------------ MAIN ------------------

    public static void main(String[] args) {
        JFrame ventana = new JFrame("Ajedrez - 2 Jugadores");
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.add(new Ajedrez());
        ventana.pack();
        ventana.setVisible(true);
    }

    // Métodos vacíos del MouseListener
    public void mousePressed(MouseEvent e) {}
    public void mouseReleased(MouseEvent e) {}
    public void mouseEntered(MouseEvent e) {}
    public void mouseExited(MouseEvent e) {}
}
