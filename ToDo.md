# Flujo del proyecto:
### Detección de cara a determinada distancia de la cámara
* Definir la distancia y el area de cara promedio a esa distancia.
* Definir que la cara que esté viendo sea la unica para el programa (ignorar otras caras)
* Si la cara se aleja o desaparece, volver al estado 0 del programa.
### Interfaz gráfica
* Función de movimiento de la cara en función de input x,y
* Animación de emociones basicas predeterminadas (copiar forma de emoji como referencia)
    * Hablando
    * Felicidad
    * Sorpresa
    * Nojao
    * Interes
    * tristeza
    * Confusion
### Speech-to-text
* Recibir un input de audio y transformarlo a texto para ser procesado
* (Idea) Recibir audio solo cuando la cara de la persona mueva los labios
### Procesamiento de la información
* Capacidad de responder preguntas básicas - Encargado: Andrés
     * FAISS - Vector store local para almacenar embeddings asociados a fragmentos de documentación del capitulo
     * Retriever de Langchain busca fragmento (embedding) más cercano a la pregunta
     * Utiliza GPT Turbo 3.5 cómo LLM para responder
* Pequeña base de datos de la UC
* Generar una emoción asociada a la información y darsela como input a la interfáz
### Text-to-speech 
* Transformar la respuesta generada a un archivo de audio y reproducirlo
