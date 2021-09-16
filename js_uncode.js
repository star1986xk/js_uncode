// AST stuff
var esprima = require('esprima');
var escodegen = require('escodegen');
var esmangle = require('esmangle');

// Jstillery / Custom AST
var esdeob = require('../src/jstiller.js');
var pass = require("../src/custom_esmangle_pipeline.js").createPipeline;

function uncode(source) {
    try {
        var ast = esprima.parse(source);
        try {
            ast = esmangle.optimize(ast, pass(), {
                destructive: true
            });
        } catch (e) {
            console.error("[EE] Problem in mangling", e);
            console.error("[II] Mangle normalization were not performed due to errors. the code is going to be passed as it is to JSTillery");
        }
        esdeob.init();
        ast = esdeob.deobfuscate(ast, null, true);

        var reduced = escodegen.generate(ast, {
            comment: true
        });
        return reduced
    } catch (e) {
        console.log(e);
    }
}
