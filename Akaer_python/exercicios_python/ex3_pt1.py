import pandas as pd
arquivo = 'c:/PythonPandasAkaer/Input_Teste_Python_exercicio 3.xlsx'
df = pd.read_excel(arquivo)
df['Start Time'] = pd.to_datetime(df['Start Time'], format='%d/%m/%Y %H:%M')
df['End Time'] = pd.to_datetime(df['End Time'], format='%Y-%m-%d %H:%M:%S')
dataframes_por_usuario = []
for user in df['User Name'].unique():
    df_usuario = df[df['User Name'] == user].copy()
    def diferenca_hrs(start, last):
        diferenca = last - start
        return diferenca.total_seconds() / 3600
    df_usuario['diferenca_hrs'] = df_usuario.apply(lambda row: diferenca_hrs(row['Start Time'], row['End Time']), axis=1)
    df_usuario_grouped = df_usuario.groupby(df_usuario['Start Time'].dt.date)['diferenca_hrs'].sum().reset_index()
    df_usuario_grouped['Total Horas Ativas'] = df_usuario_grouped['diferenca_hrs'].apply(lambda x: f"{x:.0f} horas ativo no total")
    df_usuario_grouped['User Name'] = user
    dataframes_por_usuario.append(df_usuario_grouped)
df_final = pd.concat(dataframes_por_usuario)
arquivo_saida = 'c:/PythonPandasAkaer/Resultados_Python_exercicio_3.xlsx'
df_final.to_excel(arquivo_saida, index=False)
print("Gerado o arquivo.")
