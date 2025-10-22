const readline = require('readline');
const math = require('mathjs');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function runFixedPointConsole() {
    console.log("--- MÉTODO DEL PUNTO FIJO ---");
    console.log("Recuerde que f(x) = 0 se reescribe como x = g(x)");

    rl.question("Ingrese la función original f(x): ", (funcStr) => {
        rl.question("Ingrese la función iterativa g(x): ", (gStr) => {
            if (!funcStr || !gStr) {
                console.log("Debe ingresar ambas funciones, f(x) y g(x).");
                rl.close();
                return;
            }

            // Limpia la entrada del usuario para eliminar "f(x) =" o "g(x) ="
            let finalFuncStr = funcStr.includes('=') ? funcStr.split('=')[1] : funcStr;
            let finalGStr = gStr.includes('=') ? gStr.split('=')[1] : gStr;


            const cleanFuncStr = finalFuncStr.replace(/\*\*/g, '^').replace(/\s/g, '');
            const cleanGStr = finalGStr.replace(/\*\*/g, '^').replace(/\s/g, '');

            let f, g;
            try {
                const fNode = math.parse(cleanFuncStr);
                const gNode = math.parse(cleanGStr);
                const fCode = fNode.compile();
                const gCode = gNode.compile();
                f = x => fCode.evaluate({ x: x });
                g = x => gCode.evaluate({ x: x });
            } catch (error) {
                console.error("Error en la sintaxis de una de las funciones:", error.message);
                rl.close();
                return;
            }

            rl.question("¿Desea aplicar el método de Punto Fijo? (s/n): ", (op) => {
                if (op.toLowerCase() !== 's') {
                    console.log("No se aplicó el método de Punto Fijo.");
                    rl.close();
                    return;
                }

                rl.question("Ingrese el valor inicial x0: ", (x0_input) => {
                    let x0 = parseFloat(x0_input);

                    if (isNaN(x0)) {
                        console.error("Error: El valor inicial debe ser numérico.");
                        rl.close();
                        return;
                    }

                    const tol = 1e-6;
                    const max_iter = 100;
                    let converged = false;

                    console.log("\nIteración |     x0      |     g(x0)     |     f(x0)     |    Error");
                    console.log("----------------------------------------------------------------------");

                    for (let i = 1; i <= max_iter; i++) {
                        const x1 = g(x0);
                        const error = Math.abs(x1 - x0);
                        const f_val = f(x0);

                        const iterText = i.toString().padStart(9);
                        const x0Text = x0.toFixed(6).padStart(11);
                        const x1Text = x1.toFixed(6).padStart(13);
                        const fText = f_val.toFixed(6).padStart(15);
                        const errorText = error.toExponential(2).padStart(10);
                        
                        console.log(`${iterText} | ${x0Text} | ${x1Text} | ${fText} | ${errorText}`);

                        if (error < tol) {
                            console.log(`\nRaíz aproximada encontrada: ${x1.toFixed(6)}`);
                            console.log(`Iteraciones realizadas: ${i}`);
                            converged = true;
                            break;
                        }

                        x0 = x1;
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

runFixedPointConsole();