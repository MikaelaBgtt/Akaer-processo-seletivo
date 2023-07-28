import pandas as pd

arquivo_planilha1 = 'c:/PythonPandasAkaer/Input_Teste_Python_Dados Exercicio 4 I.xlsx'
arquivo_planilha2 = 'c:/PythonPandasAkaer/Input_Teste_Python_Dados Exercício 4 II.xlsx'
df_planilha1 = pd.read_excel(arquivo_planilha1)
df_planilha2 = pd.read_excel(arquivo_planilha2)
def find_and_replace_name(row):
    if pd.notna(row['End Time']):
        user_name = df_planilha2[
            (df_planilha2['Hora Inicio'] == row['Start Time'].split()[-1]) &
            (df_planilha2['Data Termino'].notnull()) &
            (df_planilha2['Hora Termino'].notnull())
        ]
        if not user_name.empty:
            return user_name['Usuario'].iloc[0]
    elif pd.isna(row['End Time']):
        user_name = df_planilha2[
            (df_planilha2['Hora Inicio'] == row['Start Time'].split()[-1]) &
            (df_planilha2['Data Termino'].isnull()) &
            (df_planilha2['Hora Termino'].isnull())
        ]
        if not user_name.empty:
            return user_name['Usuario'].iloc[0]
    return row['User Name']
df_planilha1['User Name'] = df_planilha1.apply(find_and_replace_name, axis=1)
print(df_planilha1)
df_planilha1.to_excel("c:/PythonPandasAkaer/planilha1_resultado.xlsx", index=False)

