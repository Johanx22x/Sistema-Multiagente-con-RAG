import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from agents.rag_agent import get_rag_agent
from agents.tutor_agent import get_tutor_agent
from agents.ejercicios_agent import get_ejercicios_agent

def main():
    tutor = get_tutor_agent()
    rag = get_rag_agent()
    ejercicios = get_ejercicios_agent()

    concepto = input("¿Qué concepto deseas estudiar? > ")

    print("\n📚 Buscando referencias...")
    resultado_rag = rag.run(concepto)
    print(f"\n🔍 Fragmento relevante:\n{resultado_rag}")

    print("\n🧠 Explicación del Tutor:")
    explicacion = tutor.run({"concepto": concepto})
    print(explicacion)

    print("\n✏️ Ejercicio propuesto:")
    ejercicio = ejercicios.run({"tema": concepto})
    print(ejercicio)

if __name__ == "__main__":
    main()
