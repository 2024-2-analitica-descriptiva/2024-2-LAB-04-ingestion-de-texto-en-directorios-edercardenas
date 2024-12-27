# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    import os
    import pandas as pd

    # # Descomprima el archivo
    # os.system("unzip -o files/input.zip -d files/")

    # Listar los archivos
    files = [
        "files/input/train/negative",
        "files/input/train/positive",
        "files/input/train/neutral",
        "files/input/test/negative",
        "files/input/test/positive",
        "files/input/test/neutral",
    ]

    # Crear los dataframes
    train_dataset = pd.DataFrame(columns=["phrase", "target"])
    test_dataset = pd.DataFrame(columns=["phrase", "target"])

    for file in files:
        sentiment = file.split("/")[-1]
        for txt in os.listdir(file):
            with open(f"{file}/{txt}") as f:
                phrase = f.read()
                nuevo_registro = pd.DataFrame([{"phrase": phrase, "target": sentiment}])
            if "train" in file:
                train_dataset = pd.concat([train_dataset, nuevo_registro], ignore_index=True)
            else:
                test_dataset = pd.concat([test_dataset, nuevo_registro], ignore_index=True)

    # Guardar los dataframes
    os.makedirs('files/output', exist_ok=True)
    train_dataset.to_csv("files/output/train_dataset.csv", index=False)
    test_dataset.to_csv("files/output/test_dataset.csv", index=False)

    return print('listo')

pregunta_01()
