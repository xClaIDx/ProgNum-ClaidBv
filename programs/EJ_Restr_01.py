class GraficadoraTexto:
    def __init__(self, xmin=-1, xmax=20, ymin=-1, ymax=15):
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
    
    def graficar(self):
        for y in range(self.ymax, self.ymin - 1, -1):
            linea = ""
            for x in range(self.xmin, self.xmax + 1):
                simbolo = " "
                intersecciones = []
                for expr, simb in self.funciones:
                    try:
                        y_eval = eval(expr, {"x": x, "y": y})
                        if abs(y - y_eval) < 0.5:
                            intersecciones.append(simb)
                    except:
                        pass
                if len(intersecciones) > 1:
                    simbolo = "#"
                elif len(intersecciones) == 1:
                    simbolo = intersecciones[0]
                elif x == 0 and y == 0:
                    simbolo = "+"
                elif x == 0:
                    simbolo = "|"
                elif y == 0:
                    simbolo = "-"
                linea += simbolo
            print(linea)


# EJERCICIO 1 - DOS ECUACIONES PRINCIPALES
if __name__ == "__main__":
    print("Ecuación 1: x = 5 (tiempo min Front)")
    print("Ecuación 2: y = 15 - x ( tiempo total)")
    print()
    
    graf = GraficadoraTexto()
    graf.agregar_funcion("(x==5)*y", "*")   # Ecuación 1: x = 5
    graf.agregar_funcion("15-x", "@")        # Ecuación 2: y = 15 - x
    graf.graficar()