class GraficadoraTexto:
    COLOR_RESET = "\033[0m"
    COLOR_EJE = "\033[90m"
    COLOR_LINEA = "\033[91m"
    COLOR_SOMBRA = "\033[94m"
    COLOR_TEXTO = "\033[97m"

    def __init__(self, xmin=0, xmax=12, ymin=0, ymax=6, titulo=""):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.funciones = []  
        self.titulo = titulo
        self.sombreado_func = None
    
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
    
    def definir_sombreado(self, funcion):
        self.sombreado_func = funcion
    
    def graficar(self):
        print(f"\n{self.COLOR_TEXTO}{self.titulo}{self.COLOR_RESET}\n")
        for y in range(self.ymax, self.ymin - 1, -1):
            linea = ""
            for x in range(self.xmin, self.xmax + 1):
                simbolo = " "
                color = self.COLOR_TEXTO
                intersecciones = []

                if self.sombreado_func:
                    try:
                        if self.sombreado_func(x, y):
                            simbolo = "·"
                            color = self.COLOR_SOMBRA
                    except:
                        pass

                for expr, simb in self.funciones:
                    try:
                        y_eval = eval(expr, {"x": x})
                        if abs(y - y_eval) < 0.5:
                            intersecciones.append(simb)
                    except:
                        pass

                if len(intersecciones) > 1:
                    simbolo = "#"
                    color = self.COLOR_LINEA
                elif len(intersecciones) == 1:
                    simbolo = intersecciones[0]
                    color = self.COLOR_LINEA
                elif simbolo == " ":
                    if x == 0 and y == 0:
                        simbolo = "+"
                        color = self.COLOR_EJE
                    elif x == 0:
                        simbolo = "|"
                        color = self.COLOR_EJE
                    elif y == 0:
                        simbolo = "-"
                        color = self.COLOR_EJE

                linea += f"{color}{simbolo}{self.COLOR_RESET}"
            print(linea)
        
        print(f"\n{self.COLOR_TEXTO}Leyenda:{self.COLOR_RESET}")
        print(f"{self.COLOR_LINEA}*{self.COLOR_RESET}  frontera (5x + 10y = 50)")
        print(f"{self.COLOR_SOMBRA}·{self.COLOR_RESET}  región factible (≤ 50 unidades)")
        print(f"{self.COLOR_EJE}|, -, +{self.COLOR_RESET}  ejes coordenados\n")


if __name__ == "__main__":
    graf = GraficadoraTexto(xmin=0, xmax=12, ymin=0, ymax=6, titulo="Funcion: 5x + 10y ≤ 50")
    graf.agregar_funcion("5 - 0.5*x", "*")
    graf.definir_sombreado(lambda x, y: 5*x + 10*y <= 50 and x >= 0 and y >= 0)
    graf.graficar()