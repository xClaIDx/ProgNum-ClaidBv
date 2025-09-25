class GraficadoraTexto:
    def __init__(self, xmin=0, xmax=12, ymin=0, ymax=12):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.funciones = []  
    
    def preparar_expresion(self, expr: str) -> str:
        expr = expr.replace(" ", "")
        expr = expr.replace("^", "**")
        if expr.startswith("x"):
            expr = "1*" + expr
        expr = expr.replace("-x", "-1*x")
        expr = expr.replace("+x", "+1*x")
        expr = expr.replace("x", "*x")
        expr = expr.replace("**x", "*x")
        return expr
    
    def agregar_funcion(self, expresion: str, simbolo: str):
        expr_preparada = self.preparar_expresion(expresion)
        self.funciones.append((expr_preparada, simbolo))
    
    def graficar(self, sombrear=False):
        print("\nGráfico en Plano Cartesiano\n")
        for y in range(self.ymax, self.ymin - 1, -1):
            linea = ""
            for x in range(self.xmin, self.xmax + 1):
                simbolo = " "
                intersecciones = []

                # Sombrear región factible
                if sombrear:
                    if x >= 4 and y >= 6 and x + y <= 12:
                        simbolo = "."

                # Dibujar líneas de frontera
                for expr, simb in self.funciones:
                    try:
                        y_eval = eval(expr, {"x": x})
                        if abs(y - y_eval) < 0.5:
                            intersecciones.append(simb)
                    except:
                        pass

                # Prioridad: sombreado > intersecciones > ejes
                if len(intersecciones) > 1:
                    simbolo = "#"
                elif len(intersecciones) == 1:
                    simbolo = intersecciones[0]
                elif simbolo == " ":
                    if x == 0 and y == 0:
                        simbolo = "+"
                    elif x == 0:
                        simbolo = "|"
                    elif y == 0:
                        simbolo = "-"

                linea += simbolo
            print(linea)


if __name__ == "__main__":
    graf = GraficadoraTexto(xmin=0, xmax=12, ymin=0, ymax=12)

    # Restricciones de frontera
    graf.agregar_funcion("4", "*")          # x >= 4 (línea vertical)
    graf.agregar_funcion("6", "@")          # y >= 6 (línea horizontal)
    graf.agregar_funcion("12 - x", "#")     # x + y <= 12 (línea diagonal)

    graf.graficar(sombrear=True)