
#Clase CodeGenerator
class CodeGenerator:

    #Todas la cosas para remplazar
    
    code = '''
using System.Collections;
using system;
using UnityEngine;

public class ${Class} : MonoBehaviour {
    _Variables_
    >Start()
    >Update()
    >LateUpdate()
    >OnCollisionEnter()
    >OnCollisionEnter2D()
    >OnCollisionStay()
    >OnCollisionStay2D()
    >OnCollisionExit()
    >OnCollisionExit2D()
    >OnTriggerEnter()
    >OnTriggerEnter2D()
    >OnTriggerStay()
    >OnTriggerStay2D()
    >OnTriggerExit()
    >OnTriggerExit2D()

}
'''

    generatedCode = code

    variables = '''
    public int XD;'''

    start = '''
    void Start(){
    }'''

    update = '''
    void Update(){
    }'''

    lateUpdate = '''
    void LateUpdate(){
    }'''

    onCollisionEnter = '''
    void OnCollisionEnter(Collision col){
    }'''

    onCollisionEnter2D = '''
    void OnCollisionEnter2D(Collision2D col){
    }'''

    onCollisionStay = '''
    void OnCollisionStay(Collision col){
    }'''

    onCollisionStay2D = '''
    void OnCollisionStay2D(Collision2D col){
    }'''

    onCollisionExit = '''
    void OnCollisionExit(Collision col){
    }'''

    onCollisionExit2D = '''
    void OnCollisionExit2D(Collision2D col){
    }'''

    onTriggerEnter = '''
    void OnCollisionEnter(Collider col){
    }'''

    onTriggerEnter2D = '''
    void OnCollisionEnter2D(Collider2D col){
    }'''

    onTriggerStay = '''
    void OnCollisionStay(Collider col){
    }'''

    onTriggerStay2D = '''
    void OnCollisionStay2D(Collider2D col){
    }'''

    onTriggerExit = '''
    void OnCollisionExit(Collider col){
    }'''

    onTriggerExit2D = '''
    void OnCollisionExit2D(Collider2D col){
    }'''

    #Aqui es donde se genera el codigo
    #
    #Funciona de tal manera que remplaza cada metodo remplazable (de self.code) por los metodos hechos (EJ: self.start, self.lateUpdate)
    #
    def GenerateCodeDefault(self,className = "Class"):
        #El codigo generado vuelve a ser remplazable para remplazar los metodos
        self.generatedCode = self.code

        #Remplazacion de nombre, metodos, variables
        self.generatedCode = self.generatedCode.replace("${Class}",className)
        self.generatedCode = self.generatedCode.replace("_Variables_",self.variables)
        self.generatedCode = self.generatedCode.replace(">Start()",self.start)
        self.generatedCode = self.generatedCode.replace(">Update()",self.update)
        self.generatedCode = self.generatedCode.replace(">LateUpdate()",self.lateUpdate)
        self.generatedCode = self.generatedCode.replace(">OnCollisionEnter()",self.onCollisionEnter)
        self.generatedCode = self.generatedCode.replace(">OnCollisionEnter2D()",self.onCollisionEnter2D)
        self.generatedCode = self.generatedCode.replace(">OnCollisionStay()",self.onCollisionStay)
        self.generatedCode = self.generatedCode.replace(">OnCollisionStay2D()",self.onCollisionStay2D)
        self.generatedCode = self.generatedCode.replace(">OnCollisionExit()",self.onCollisionExit)
        self.generatedCode = self.generatedCode.replace(">OnCollisionExit2D()",self.onCollisionExit2D)
        self.generatedCode = self.generatedCode.replace(">OnTriggerEnter()",self.onTriggerEnter)
        self.generatedCode = self.generatedCode.replace(">OnTriggerEnter2D()",self.onTriggerEnter2D)
        self.generatedCode = self.generatedCode.replace(">OnTriggerStay()",self.onTriggerStay)
        self.generatedCode = self.generatedCode.replace(">OnTriggerStay2D()",self.onTriggerStay2D)
        self.generatedCode = self.generatedCode.replace(">OnTriggerExit()",self.onTriggerExit)
        self.generatedCode = self.generatedCode.replace(">OnTriggerExit2D()",self.onTriggerExit2D)

#Lo que pasa cuando se inicia el programa
if __name__ == "__main__":
    cg = CodeGenerator()
    cg.variables = '''
    Vector3 pos;
'''
    cg.start = '''
    void Start(){
        pos = GetComponent<Transform>().position;
    }'''
    cg.GenerateCodeDefault("Movement")
    print(cg.generatedCode)
    
    
