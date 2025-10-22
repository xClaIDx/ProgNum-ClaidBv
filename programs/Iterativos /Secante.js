
const readline = require('readline');
const math = require('mathjs'); 

//  Crear la interfaz para leer y escribir en la consola
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function runSecantConsole() {
    rl.question("Ingrese la función f(x): ", (funcStr) => {
        if (!funcStr) {
            console.log("No se ingresó ninguna función.");
            rl.close();
            return;
        }

        
        const cleanFuncStr = funcStr.replace(/\*\*/g, '^').replace(/\s/g, '');

        let f;
        try {
            const node = math.parse(cleanFuncStr);
            const code = node.compile();
            f = x => code.evaluate({ x: x });
        } catch (error) {
            console.error("Error en la función ingresada:", error.message);
            rl.close();
            return;
        }

        rl.question("¿Desea encontrar una raíz con el método de la Secante? (s/n): ", (op) => {
            if (op.toLowerCase() !== 's') {
                console.log("No se aplicó el método de la Secante.");
                rl.close();
                return;
            }

            rl.question("Ingrese el primer valor inicial x0: ", (x0_input) => {
                rl.question("Ingrese el segundo valor inicial x1: ", (x1_input) => {
                    let x0 = parseFloat(x0_input);
                    let x1 = parseFloat(x1_input);

                    if (isNaN(x0) || isNaN(x1)) {
                        console.error("Error: Los valores iniciales deben ser numéricos.");
                        rl.close();
                        return;
                    }

                    const tol = 1e-6;
                    const max_iter = 100;
                    let converged = false;

                    console.log("\nIteración |     x0      |      x1      |     f(x0)     |     f(x1)     |      x2     |    Error");
                    console.log("-----------------------------------------------------------------------------------------");

                    for (let i = 1; i <= max_iter; i++) {
                        const f0 = f(x0);
                        const f1 = f(x1);

                        if (Math.abs(f1 - f0) < 1e-15) { // Evitar división por cero
                            console.log(`\nDivisión por cero en la iteración ${i}. El método se detiene.`);
                            break;
                        }

                        const x2 = x1 - f1 * (x1 - x0) / (f1 - f0);
                        const error = Math.abs(x2 - x1);

                        const iterText = i.toString().padStart(9);
                        const x0Text = x0.toFixed(6).padStart(11);
                        const x1Text = x1.toFixed(6).padStart(11);
                        const f0Text = f0.toFixed(6).padStart(15);
                        const f1Text = f1.toFixed(6).padStart(15);
                        const x2Text = x2.toFixed(6).padStart(11);
                        const errorText = error.toExponential(2).padStart(10);

                        console.log(`${iterText} | ${x0Text} | ${x1Text} | ${f0Text} | ${f1Text} | ${x2Text} | ${errorText}`);

                        if (error < tol) {
                            console.log(`\nRaíz aproximada encontrada: ${x2.toFixed(6)}`);
                            console.log(`Iteraciones realizadas: ${i}`);
                            converged = true;
                            break;
                        }

                        x0 = x1;
                        x1 = x2;
                    }

                    if (!converged) {
                        console.warn(`\nNo se alcanzó la convergencia después de ${max_iter} iteraciones.`);
                    }

                    rl.close(); 
                });
            });
        });
    });
}

runSecantConsole();