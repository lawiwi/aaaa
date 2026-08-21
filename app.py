from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    preguntas = [
        {
            "numero": 1,
            "pregunta": "¿Qué queremos descubrir?",
            "respuesta": "Queremos descubrir en qué época del año se presenta el mayor índice de accidentalidad vial y qué características están relacionadas con ese aumento, como el mes, día, hora, condiciones climáticas, tipo de vía y gravedad del accidente."
        },
        {
            "numero": 2,
            "pregunta": "¿Cuál sería nuestra pregunta principal?",
            "respuesta": "¿En qué período del año se presenta el mayor índice de accidentalidad vial y cuáles son los principales factores asociados a este comportamiento?"
        },
        {
            "numero": 3,
            "pregunta": "¿Qué tres preguntas secundarias ayudarían a responderla?",
            "respuesta": [
                "¿Qué meses y días de la semana presentan la mayor cantidad de accidentes viales?",
                "¿En qué horarios se concentra la mayor cantidad de accidentes?",
                "¿Qué factores, como clima, tipo de vía, ubicación y tipo de accidente, están relacionados con los períodos de mayor accidentalidad?"
            ]
        },
        {
            "numero": 4,
            "pregunta": "¿Qué datos necesitaríamos?",
            "respuesta": [
                "Fecha del accidente",
                "Hora del accidente",
                "Ubicación",
                "Municipio o ciudad",
                "Tipo de vía",
                "Condiciones climáticas",
                "Número de vehículos involucrados",
                "Tipo de accidente",
                "Número de personas lesionadas",
                "Número de fallecidos",
                "Gravedad del accidente",
                "Día de la semana",
                "Mes y año"
            ]
        },
        {
            "numero": 5,
            "pregunta": "¿Qué variables serían indispensables?",
            "respuesta": [
                "Fecha: determinar meses y períodos con mayor accidentalidad.",
                "Hora: identificar los horarios de mayor riesgo.",
                "Ubicación: identificar zonas con mayor concentración de accidentes.",
                "Municipio o ciudad: comparar la accidentalidad entre diferentes zonas.",
                "Tipo de vía: determinar qué vías presentan mayor accidentalidad.",
                "Condiciones climáticas: analizar su relación con los accidentes.",
                "Tipo de accidente: identificar los accidentes más frecuentes.",
                "Número de vehículos: analizar la magnitud de los accidentes.",
                "Lesionados y fallecidos: determinar la gravedad de los accidentes."
            ]
        },
        {
            "numero": 6,
            "pregunta": "¿Dónde podríamos obtener esos datos?",
            "respuesta": [
                "Agencia Nacional de Seguridad Vial (ANSV)",
                "Datos Abiertos Colombia",
                "Observatorio Nacional de Seguridad Vial",
                "Secretarías de Movilidad",
                "Policía Nacional"
            ]
        },
        {
            "numero": 7,
            "pregunta": "¿La fuente sería primaria, secundaria o terciaria?",
            "respuesta": "Principalmente sería una fuente secundaria, porque utilizaríamos datos que ya fueron recopilados y publicados por entidades gubernamentales."
        },
        {
            "numero": 8,
            "pregunta": "¿Qué problemas de calidad anticipamos?",
            "respuesta": [
                "Datos faltantes.",
                "Datos duplicados.",
                "Inconsistencias en fechas, horas o ubicaciones.",
                "Errores de digitación.",
                "Datos desactualizados.",
                "Diferencias entre fuentes.",
                "Posible subregistro de accidentes menores."
            ]
        }
    ]

    return render_template("index.html", preguntas=preguntas)


if __name__ == "__main__":
    app.run(debug=True)